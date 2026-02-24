#!/usr/bin/env python3
"""Validate local markdown links in repository markdown files.

Checks only relative links to keep CI deterministic and network-independent.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def iter_markdown_files() -> list[Path]:
    return [
        p
        for p in ROOT.rglob("*.md")
        if ".git/" not in p.as_posix() and "node_modules/" not in p.as_posix()
    ]


def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:", "#"))


def normalize_target(raw: str) -> str:
    target = raw.strip().strip("<>")
    if " " in target and not target.startswith("./") and not target.startswith("../"):
        return target  # likely URL with spaces (rare); handled elsewhere
    return target


def main() -> int:
    errors: list[str] = []

    for md_file in iter_markdown_files():
        content = md_file.read_text(encoding="utf-8")
        for line_no, line in enumerate(content.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                raw_link = match.group(1).strip()
                link = normalize_target(raw_link)

                if not link or is_external(link):
                    continue

                path_part = unquote(link.split("#", 1)[0].split("?", 1)[0])
                if not path_part:
                    continue

                target_path = (md_file.parent / path_part).resolve()
                if not target_path.exists():
                    rel = md_file.relative_to(ROOT)
                    errors.append(
                        f"{rel}:{line_no} -> broken local link '{raw_link}' (resolved: {target_path})"
                    )

    if errors:
        print("Markdown local link checks failed:")
        for err in errors:
            print(f" - {err}")
        return 1

    print("Markdown local link checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
