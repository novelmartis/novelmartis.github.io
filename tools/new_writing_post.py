#!/usr/bin/env python3
from __future__ import annotations
import re
from datetime import date
from pathlib import Path
import sys

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s or "note"

def main():
    if len(sys.argv) < 2:
        print('Usage: python tools/new_writing_post.py "Post title"')
        sys.exit(1)

    title = sys.argv[1].strip()
    today = date.today().isoformat()
    slug = slugify(title)

    out_dir = Path("_writing")
    out_dir.mkdir(exist_ok=True)

    path = out_dir / f"{today}-{slug}.md"
    if path.exists():
        print(f"Already exists: {path}")
        sys.exit(1)

    path.write_text(
f"""---
layout: page
title: "{title}"
date: {today}
---

Write here.
""",
        encoding="utf-8"
    )
    print(f"Created: {path}")

if __name__ == "__main__":
    main()
