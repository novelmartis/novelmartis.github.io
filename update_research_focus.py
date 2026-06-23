#!/usr/bin/env python3
"""Best-effort multi-source profile summarizer for the static landing page."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from itertools import combinations


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "research-focus.json"
AUTHOR_NAME = os.environ.get("RESEARCH_PROFILE_NAME", "Sushrut Thorat").strip()
AUTHOR_ORCID = os.environ.get("RESEARCH_PROFILE_ORCID", "0000-0003-2276-5621").strip()
AUTHOR_ID = os.environ.get("OPENALEX_AUTHOR_ID", "A5034511642").strip()
AUTHOR_URL = f"https://api.openalex.org/authors/{AUTHOR_ID}"
WORKS_URL = f"https://api.openalex.org/works?filter=author.id:{AUTHOR_ID}&sort=publication_year:desc&per-page=200"
ORCID_RECORD_URL = f"https://pub.orcid.org/v3.0/{AUTHOR_ORCID}/record"
ORCID_WORKS_URL = f"https://pub.orcid.org/v3.0/{AUTHOR_ORCID}/works"
SEMANTIC_SCHOLAR_AUTHOR_ID = os.environ.get("SEMANTIC_SCHOLAR_AUTHOR_ID", "1967895").strip()
SEMANTIC_SCHOLAR_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
SEMANTIC_SCHOLAR_SEARCH_URL = (
    "https://api.semanticscholar.org/graph/v1/author/search"
    f"?query={urllib.parse.quote(AUTHOR_NAME)}&limit=3&fields=name,paperCount,externalIds"
)
SOURCE_PRIORITY = tuple(
    source.strip()
    for source in os.environ.get(
        "RESEARCH_PROFILE_SOURCE_PRIORITY",
        "openalex,orcid,semantic_scholar",
    ).split(",")
    if source.strip()
)
FALLBACK_SUMMARY = (
    "Active vision, brain-aligned predictive agents, developmental visual curricula, "
    "continual learning, visual search, and the structure of human object and scene representations."
)
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "based", "between", "by", "for", "from",
    "in", "into", "is", "of", "on", "or", "the", "to", "toward", "towards", "under",
    "using", "via", "with", "without", "within", "across", "after", "before", "beyond",
    "during", "how", "if", "into", "it", "its", "more", "new", "than", "that", "this",
    "these", "those", "through", "toward", "up", "when", "where", "while",
}
GENERIC_WORDS = {
    "analysis", "applications", "approach", "approaches", "architecture", "behavioral",
    "brain", "characterization", "characterizing", "cognitive", "computation",
    "computational", "data", "dynamics", "features", "function", "functions", "guide",
    "guides", "human", "information", "mechanisms", "models", "nature", "networks",
    "neural", "object", "objects", "perception", "processing", "psychology", "research",
    "response", "role", "scene", "studies", "study", "tasks", "theory", "using",
    "visual", "works",
}
BAD_TITLE_TOKENS = {
    "accounted", "adopting", "alleviates", "catalyzing", "characterising", "characterizing",
    "computational", "diagnosing", "disentangling", "facilitates", "guide", "guides", "implementing",
    "keep", "learned", "maximise", "misuse", "modulation", "models", "moving", "predicting",
    "recommendations", "searching", "self-guided", "solving", "sparks", "statistical", "trained",
    "trainees", "using", "yields",
}
TITLE_ONLY_MIN_RECURRENCE = 2
TITLE_ONLY_MIN_YEAR_SPAN = 2
LOW_SIGNAL_LABELS = {
    "information processing",
    "visual information",
    "human behavior",
    "brain function",
}


def fetch_json(url: str) -> dict:
    headers = {
        "User-Agent": "novelmartis.github.io research summary bot/1.0",
        "Accept": "application/json",
    }
    if "semanticscholar.org" in url and SEMANTIC_SCHOLAR_API_KEY:
        headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY
    request = urllib.request.Request(
        url,
        headers=headers,
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def normalize_title(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(
        r"\s*[—:-]\s*(data and code|code and data|supplementary material|author response|data|code|essential data and analysis code)\s*$",
        "",
        title,
    )
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def dedupe_works(works: list[dict]) -> list[dict]:
    seen: set[str] = set()
    deduped: list[dict] = []
    for item in works:
        title = (item.get("display_name") or "").strip()
        if not title:
            continue
        normalized = normalize_title(title)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(item)
    return deduped


def fetch_openalex_author_and_works() -> tuple[dict, list[dict], dict]:
    author = fetch_json(AUTHOR_URL)
    works = fetch_json(WORKS_URL)
    deduped = dedupe_works(works.get("results", []))
    confidence = 0.99 if author.get("orcid", "").endswith(AUTHOR_ORCID) else 0.94
    return author, deduped, {
        "provider": "openalex",
        "source": AUTHOR_URL,
        "confidence_score": confidence,
        "confidence_label": confidence_label(confidence),
        "confidence_reason": "Matched configured OpenAlex author id and ORCID."
        if confidence >= 0.99
        else "Matched configured OpenAlex author id.",
    }


def pick_orcid_name(record: dict) -> str:
    person = record.get("person", {})
    name = person.get("name", {})
    given = ((name.get("given-names") or {}).get("value") or "").strip()
    family = ((name.get("family-name") or {}).get("value") or "").strip()
    full = " ".join(part for part in (given, family) if part)
    return full or AUTHOR_NAME


def pick_orcid_work_id(summary: dict) -> str:
    external_ids = ((summary.get("external-ids") or {}).get("external-id") or [])
    for item in external_ids:
        value = (item.get("external-id-value") or "").strip()
        if value:
            return value
    put_code = summary.get("put-code")
    return str(put_code) if put_code is not None else ""


def standardize_orcid_works(groups: list[dict]) -> list[dict]:
    works: list[dict] = []
    for group in groups:
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        summary = summaries[0]
        title = ((((summary.get("title") or {}).get("title")) or {}).get("value") or "").strip()
        year = ((((summary.get("publication-date") or {}).get("year")) or {}).get("value") or "").strip()
        works.append(
            {
                "id": pick_orcid_work_id(summary) or title,
                "display_name": title,
                "publication_year": int(year) if year.isdigit() else None,
                "primary_topic": {},
                "topics": [],
            }
        )
    return dedupe_works(works)


def fetch_orcid_author_and_works() -> tuple[dict, list[dict], dict]:
    record = fetch_json(ORCID_RECORD_URL)
    works_payload = fetch_json(ORCID_WORKS_URL)
    works = standardize_orcid_works(works_payload.get("group", []))
    author = {
        "id": f"https://orcid.org/{AUTHOR_ORCID}",
        "display_name": pick_orcid_name(record),
        "orcid": f"https://orcid.org/{AUTHOR_ORCID}",
        "works_count": len(works),
        "topics": [],
    }
    confidence = 0.97
    return author, works, {
        "provider": "orcid",
        "source": ORCID_WORKS_URL,
        "confidence_score": confidence,
        "confidence_label": confidence_label(confidence),
        "confidence_reason": "Matched configured ORCID record exactly.",
    }


def standardize_semantic_scholar_works(papers: list[dict]) -> list[dict]:
    works: list[dict] = []
    for paper in papers:
        fields = [
            {"display_name": field}
            for field in (paper.get("fieldsOfStudy") or [])
            if isinstance(field, str) and field.strip()
        ]
        works.append(
            {
                "id": paper.get("paperId") or paper.get("externalIds", {}).get("DOI") or paper.get("title"),
                "display_name": (paper.get("title") or "").strip(),
                "publication_year": paper.get("year"),
                "primary_topic": fields[0] if fields else {},
                "topics": fields[:5],
            }
        )
    return dedupe_works(works)


def search_semantic_scholar_author() -> dict:
    payload = fetch_json(SEMANTIC_SCHOLAR_SEARCH_URL)
    candidates = payload.get("data") or []
    if not candidates:
        raise RuntimeError("Semantic Scholar returned no author candidates.")
    return candidates[0]


def fetch_semantic_scholar_author_and_works() -> tuple[dict, list[dict], dict]:
    if not SEMANTIC_SCHOLAR_API_KEY and not SEMANTIC_SCHOLAR_AUTHOR_ID:
        raise RuntimeError("Semantic Scholar skipped: no API key configured.")

    exact = bool(SEMANTIC_SCHOLAR_AUTHOR_ID)
    author_id = SEMANTIC_SCHOLAR_AUTHOR_ID
    author_meta: dict
    if exact:
        author_meta = fetch_json(
            "https://api.semanticscholar.org/graph/v1/author/"
            f"{author_id}?fields=name,paperCount,externalIds"
        )
    else:
        author_meta = search_semantic_scholar_author()
        author_id = author_meta.get("authorId", "")
        if not author_id:
            raise RuntimeError("Semantic Scholar search result did not include an author id.")

    papers_payload = fetch_json(
        "https://api.semanticscholar.org/graph/v1/author/"
        f"{author_id}/papers?limit=1000&fields=title,year,fieldsOfStudy,externalIds"
    )
    works = standardize_semantic_scholar_works(papers_payload.get("data", []))
    author = {
        "id": f"https://www.semanticscholar.org/author/{author_id}",
        "display_name": author_meta.get("name") or AUTHOR_NAME,
        "orcid": ((author_meta.get("externalIds") or {}).get("ORCID") or ""),
        "works_count": author_meta.get("paperCount", len(works)),
        "topics": [],
    }
    confidence = 0.91 if exact else 0.62
    reason = (
        "Matched configured Semantic Scholar author id."
        if exact
        else "Matched Semantic Scholar author search by name only."
    )
    return author, works, {
        "provider": "semantic_scholar",
        "source": f"https://api.semanticscholar.org/graph/v1/author/{author_id}",
        "confidence_score": confidence,
        "confidence_label": confidence_label(confidence),
        "confidence_reason": reason,
    }


def normalize_topic_name(name: str) -> str:
    name = re.sub(r"\s+", " ", name).strip()
    replacements = {
        "Studies": "research",
        "Applications": "applications",
        "Mechanisms": "mechanisms",
    }
    words = name.split()
    if words and words[-1] in replacements:
        words[-1] = replacements[words[-1]]
    name = " ".join(words).lower()
    return re.sub(r"\bai\b", "AI", name)


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z-]*", text.lower())


def stem_word(word: str) -> str:
    for suffix in ("ational", "ition", "tion", "ment", "ness", "ality", "ality", "ical", "ical", "ally", "ally", "ual", "ing", "ers", "ies", "ied", "ism", "ist", "ous", "ive", "ied", "ed", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            if suffix == "ies":
                return word[:-3] + "y"
            return word[: -len(suffix)]
    return word


def support_key(word: str) -> str:
    return stem_word(word)[:5]


def content_words(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOPWORDS and len(token) > 2]


def candidate_phrases(title: str) -> list[str]:
    tokens = tokenize(title)
    phrases: set[str] = set()
    trigram_prefixes: set[tuple[str, str]] = set()

    for idx in range(len(tokens) - 3 + 1):
        window = tokens[idx : idx + 3]
        if any(token in STOPWORDS for token in window):
            continue
        if any(len(token) <= 2 for token in window):
            continue
        if any(token in BAD_TITLE_TOKENS for token in window):
            continue
        if window[2] not in {"applications", "mechanisms", "research", "study", "studies"}:
            trigram_prefixes.add((window[0], window[1]))

    for size in (2, 3):
        for idx in range(len(tokens) - size + 1):
            window = tokens[idx : idx + size]
            if any(token in STOPWORDS for token in window):
                continue
            if any(len(token) <= 2 for token in window):
                continue
            if any(token in BAD_TITLE_TOKENS for token in window):
                continue
            if size == 2 and window[1] in GENERIC_WORDS and (window[0], window[1]) in trigram_prefixes:
                continue
            phrase = " ".join(window)
            if phrase in STOPWORDS:
                continue
            phrases.add(phrase)

    return sorted(phrases)


def title_word_counts_from_works(works: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for work in works:
        title = work.get("display_name") or ""
        for word in {support_key(word) for word in content_words(tokenize(title))}:
            counts[word] = counts.get(word, 0) + 1
    return counts


def candidate_units_for_work(work: dict) -> dict[str, set[str]]:
    units: dict[str, set[str]] = {}
    title = work.get("display_name") or ""
    for phrase in candidate_phrases(title):
        units.setdefault(phrase, set()).add("title")

    primary_topic = work.get("primary_topic") or {}
    if primary_topic.get("display_name"):
        units.setdefault(normalize_topic_name(primary_topic["display_name"]), set()).add("primary_topic")

    for topic in work.get("topics", [])[:5]:
        name = normalize_topic_name(topic.get("display_name", ""))
        if name:
            units.setdefault(name, set()).add("topic")

    return units


def lexical_support_ratio(text: str, title_word_counts: dict[str, int]) -> float:
    words = [support_key(word) for word in content_words(tokenize(text)) if word not in GENERIC_WORDS]
    if not words:
        return 0.0
    supported = sum(1 for word in words if title_word_counts.get(word, 0) > 0)
    return supported / len(words)


def topic_vocabulary(author: dict, works: list[dict]) -> set[str]:
    vocab: set[str] = set()
    for topic in author.get("topics", []):
        vocab.update(content_words(tokenize(normalize_topic_name(topic.get("display_name", "")))))

    for work in works:
        primary_topic = work.get("primary_topic") or {}
        if primary_topic.get("display_name"):
            vocab.update(content_words(tokenize(normalize_topic_name(primary_topic["display_name"]))))
        for topic in work.get("topics", [])[:5]:
            if topic.get("display_name"):
                vocab.update(content_words(tokenize(normalize_topic_name(topic["display_name"]))))
    return vocab


def broad_topics(author: dict, title_word_counts: dict[str, int], limit: int = 3) -> list[str]:
    selected: list[str] = []
    selected_words: list[set[str]] = []

    for topic in sorted(author.get("topics", []), key=lambda item: item.get("count", 0), reverse=True):
        name = normalize_topic_name(topic.get("display_name", ""))
        if not name:
            continue
        words = [support_key(word) for word in content_words(tokenize(name)) if word not in {"research", "applications"}]
        if len(words) < 2:
            continue
        absent = [word for word in words if title_word_counts.get(word, 0) == 0]
        if words[0] in absent:
            continue
        if len(absent) / len(words) > 0.30:
            continue
        word_set = set(words)
        if any(word_set and len(word_set & prior) / min(len(word_set), len(prior)) >= 0.6 for prior in selected_words):
            continue
        selected.append(name)
        selected_words.append(word_set)
        if len(selected) == limit:
            break

    return selected


def concise_label(text: str) -> str:
    raw_tokens = tokenize(text)
    words = content_words(tokenize(text))
    if not words:
        return text

    trailing_noise = {
        "applications", "mechanisms", "research", "function", "functions",
        "processing", "studies", "study",
    }
    while len(words) > 2 and words[-1] in trailing_noise:
        words.pop()

    if (
        len(words) >= 3
        and words[1] in GENERIC_WORDS
        and words[2] not in trailing_noise
        and "and" not in raw_tokens[:4]
    ):
        return " ".join(words[:3])
    if len(words) >= 2:
        return " ".join(words[:2])
    return words[0]


def confidence_label(score: float) -> str:
    if score >= 0.9:
        return "high"
    if score >= 0.7:
        return "medium"
    return "low"


def attempt_record(provider: str, status: str, detail: str, **extra: object) -> dict:
    payload = {"provider": provider, "status": status, "detail": detail}
    payload.update({key: value for key, value in extra.items() if value not in (None, "", [])})
    return payload


def resolve_profile() -> tuple[dict, list[dict], dict, list[dict]]:
    attempts: list[dict] = []
    available_resolvers = {
        "openalex": fetch_openalex_author_and_works,
        "orcid": fetch_orcid_author_and_works,
        "semantic_scholar": fetch_semantic_scholar_author_and_works,
    }
    resolvers: list[tuple[str, object]] = []
    for provider in SOURCE_PRIORITY:
        resolver = available_resolvers.get(provider)
        if resolver is None:
            attempts.append(attempt_record(provider, "skipped", "Unknown provider in source priority list."))
            continue
        resolvers.append((provider, resolver))

    last_error: Exception | None = None
    for provider, resolver in resolvers:
        try:
            author, works, metadata = resolver()
            if not works:
                attempts.append(attempt_record(provider, "empty", "Source returned no usable works."))
                continue
            attempts.append(
                attempt_record(
                    provider,
                    "selected",
                    metadata["confidence_reason"],
                    usable_works_count=len(works),
                    reported_works_count=author.get("works_count"),
                    confidence_score=metadata["confidence_score"],
                    confidence_label=metadata["confidence_label"],
                    source=metadata["source"],
                )
            )
            return author, works, metadata, attempts
        except (urllib.error.URLError, TimeoutError, RuntimeError, ValueError, KeyError) as exc:
            last_error = exc
            attempts.append(attempt_record(provider, "failed", str(exc)))

    if last_error is None:
        raise RuntimeError("No publication sources configured.")
    raise RuntimeError(
        "All source fallbacks failed. "
        + "; ".join(f"{item['provider']}: {item['detail']}" for item in attempts)
    ) from last_error


def build_theme_clusters(author: dict, works: list[dict], limit: int = 4) -> list[dict]:
    if not works:
        return []

    candidate_stats: dict[str, dict] = {}
    cooccurrence: dict[frozenset[str], int] = {}
    title_word_counts = title_word_counts_from_works(works)
    topic_vocab = topic_vocabulary(author, works)
    max_year = max((work.get("publication_year") or 0) for work in works) or dt.date.today().year

    for work in works:
        title = work.get("display_name") or ""
        year = work.get("publication_year")
        work_key = work.get("id") or title
        year_weight = 1.0 / (1.0 + max(0, max_year - (year or max_year)) * 0.18)

        work_units = candidate_units_for_work(work)
        for text, sources in work_units.items():
            stats = candidate_stats.setdefault(
                text, {"works": set(), "years": set(), "sources": set(), "weighted": 0.0}
            )
            stats["works"].add(work_key)
            if year:
                stats["years"].add(year)
            stats["sources"].update(sources)
            stats["weighted"] += year_weight

        texts = sorted(work_units)
        for left, right in combinations(texts, 2):
            key = frozenset((left, right))
            cooccurrence[key] = cooccurrence.get(key, 0) + year_weight

    if not candidate_stats:
        return []

    scored: list[dict] = []
    for text, stats in candidate_stats.items():
        words = set(content_words(tokenize(text)))
        recurrence = len(stats["works"])
        weighted = stats["weighted"]
        year_span = len(stats["years"])
        source_count = len(stats["sources"])
        support = lexical_support_ratio(text, title_word_counts)
        centrality = sum(weight for pair, weight in cooccurrence.items() if text in pair)
        specificity = max(1.0, math.sqrt(sum(1 for word in words if word not in GENERIC_WORDS)))
        score = (
            weighted * 3.1
            + year_span * 1.1
            + centrality * 0.45
            + source_count * 1.5
            + support * 3.0
            + specificity
        )
        scored.append(
            {
                "text": text,
                "words": words,
                "score": score,
                "recurrence": recurrence,
                "weighted": weighted,
                "year_span": year_span,
                "support": support,
                "sources": stats["sources"],
            }
        )

    scored.sort(key=lambda item: (item["score"], item["weighted"], item["year_span"]), reverse=True)

    selected: list[dict] = []
    for candidate in scored:
        words = candidate["words"]
        if len(words) < 2:
            continue
        word_list = [support_key(word) for word in content_words(tokenize(candidate["text"])) if word not in {"research", "applications"}]
        absent_ratio = (
            sum(1 for word in word_list if title_word_counts.get(word, 0) == 0) / len(word_list)
            if word_list
            else 1.0
        )
        if "title" not in candidate["sources"]:
            if not word_list or title_word_counts.get(word_list[0], 0) == 0:
                continue
            if absent_ratio > 0.30:
                continue
        else:
            anchored = [word for word in content_words(tokenize(candidate["text"])) if word in topic_vocab]
            if (
                candidate["recurrence"] < TITLE_ONLY_MIN_RECURRENCE
                and candidate["year_span"] < TITLE_ONLY_MIN_YEAR_SPAN
            ):
                continue
            if len(anchored) < max(1, len(candidate["words"]) - 1):
                continue
        if candidate["support"] < 0.34 and "title" not in candidate["sources"]:
            continue
        if any(
            words
            and (
                len(words & prior["words"]) / min(len(words), len(prior["words"])) >= 0.6
                or len(words & prior["words"]) / len(words) > 0.75
            )
            for prior in selected
        ):
            continue
        selected.append(candidate)
        if len(selected) == limit:
            break

    return selected


def infer_theme_records(author: dict, works: list[dict], limit: int = 4) -> list[dict]:
    title_word_counts = title_word_counts_from_works(works)
    broad = broad_topics(author, title_word_counts)
    broad_records = [
        {"text": theme, "label": concise_label(theme), "source": "author_topic", "score": 100 - idx}
        for idx, theme in enumerate(broad)
    ]
    cluster_records = [
        {
            "text": theme["text"],
            "label": concise_label(theme["text"]),
            "source": "+".join(sorted(theme["sources"])),
            "score": round(theme["score"], 3),
        }
        for theme in build_theme_clusters(author, works, limit=max(1, 5 - len(broad)))
    ]
    themes = broad_records + cluster_records
    deduped: list[dict] = []
    seen_words: list[set[str]] = []
    for theme in themes:
        if theme["label"] in LOW_SIGNAL_LABELS:
            continue
        words = set(content_words(tokenize(theme["label"])))
        if any(words and len(words & prior) / min(len(words), len(prior)) >= 0.6 for prior in seen_words):
            continue
        deduped.append(theme)
        seen_words.append(words)
        if len(deduped) == limit:
            break
    return deduped


def summarize(author: dict, works: list[dict]) -> tuple[str, list[dict]]:
    themes = infer_theme_records(author, works)
    if not themes:
        return FALLBACK_SUMMARY, []

    if len(themes) == 1:
        joined = themes[0]["label"]
    elif len(themes) == 2:
        joined = f"{themes[0]['label']} and {themes[1]['label']}"
    else:
        joined = ", ".join(theme["label"] for theme in themes[:-1]) + f", and {themes[-1]['label']}"
    return f"Current work clusters around {joined}.", themes


def existing_payload() -> dict:
    if not OUT.exists():
        return {}
    try:
        return json.loads(OUT.read_text())
    except json.JSONDecodeError:
        return {}


def build_payload(today: str) -> dict:
    author, works, source_metadata, attempts = resolve_profile()
    titles = [work.get("display_name", "").strip() for work in works if work.get("display_name")]
    if not titles:
        raise RuntimeError("No publication titles found in selected source response.")
    summary, theme_records = summarize(author, works)
    return {
        "updated_at": today,
        "summary": summary,
        "source": source_metadata["source"],
        "source_available": True,
        "profile_source": source_metadata["provider"],
        "profile_confidence": {
            "score": source_metadata["confidence_score"],
            "label": source_metadata["confidence_label"],
            "reason": source_metadata["confidence_reason"],
        },
        "source_attempts": attempts,
        "author": {
            "id": author.get("id"),
            "display_name": author.get("display_name"),
            "orcid": author.get("orcid"),
            "works_count": author.get("works_count", len(works)),
            "usable_works_count": len(works),
        },
        "topics": [topic.get("display_name") for topic in author.get("topics", [])[:8]],
        "candidate_themes": theme_records,
        "sample_titles": titles[:12],
        "pipeline": {
            "version": 1,
            "source_priority": list(SOURCE_PRIORITY),
        },
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stdout-only",
        action="store_true",
        help="Print the payload without writing research-focus.json.",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    today = dt.date.today().isoformat()
    payload = existing_payload()

    try:
        payload = build_payload(today)
    except (urllib.error.URLError, TimeoutError, RuntimeError, ValueError, KeyError) as exc:
        payload = {
            "updated_at": payload.get("updated_at", today),
            "summary": payload.get("summary", FALLBACK_SUMMARY),
            "source": payload.get("source", AUTHOR_URL),
            "source_available": False,
            "error": str(exc),
            "profile_source": payload.get("profile_source", "openalex"),
            "profile_confidence": payload.get(
                "profile_confidence",
                {
                    "score": 0.0,
                    "label": "low",
                    "reason": "All configured sources failed during this refresh.",
                },
            ),
            "author": payload.get("author"),
            "topics": payload.get("topics", []),
            "candidate_themes": payload.get("candidate_themes", []),
            "sample_titles": payload.get("sample_titles", []),
            "source_attempts": payload.get("source_attempts", []),
            "pipeline": payload.get(
                "pipeline",
                {
                    "version": 1,
                    "source_priority": list(SOURCE_PRIORITY),
                },
            ),
        }

    if not args.stdout_only:
        OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
