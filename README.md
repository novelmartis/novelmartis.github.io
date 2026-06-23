# novelmartis.github.io

Minimal landing page plus an automated research-focus updater.

## What lives here

- `index.html`: the public landing page
- `research-focus.json`: generated summary data consumed by the page
- `update_research_focus.py`: multi-source updater
- `.github/workflows/research-focus.yml`: scheduled daily refresh
- `.github/workflows/validate-site.yml`: compile, test, and dry-run validation
- `misc/`: local-only archive space for older site material (ignored by git)

## Data pipeline

The updater resolves publications in this order by default:

1. `openalex`
2. `orcid`
3. `semantic_scholar`

It writes:

- a short summary
- candidate themes
- source and confidence metadata
- source-attempt logs

## Local usage

Refresh the generated JSON:

```bash
python3 update_research_focus.py
```

Dry-run without writing the file:

```bash
python3 update_research_focus.py --stdout-only
```

Run validation locally:

```bash
python3 -m py_compile update_research_focus.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Serve the site locally:

```bash
python3 -m http.server 4000
```

Then open [http://127.0.0.1:4000](http://127.0.0.1:4000).

## Configuration

Optional environment variables:

- `RESEARCH_PROFILE_NAME`
- `RESEARCH_PROFILE_ORCID`
- `OPENALEX_AUTHOR_ID`
- `RESEARCH_PROFILE_SOURCE_PRIORITY`
- `SEMANTIC_SCHOLAR_API_KEY`
- `SEMANTIC_SCHOLAR_AUTHOR_ID` (optional override; defaults to `1967895`)

Example source priority:

```bash
export RESEARCH_PROFILE_SOURCE_PRIORITY="openalex,orcid,semantic_scholar"
```

## GitHub Actions secrets

Optional, only needed for the Semantic Scholar fallback:

- `SEMANTIC_SCHOLAR_API_KEY`

Without those, the updater still works through OpenAlex and ORCID.
