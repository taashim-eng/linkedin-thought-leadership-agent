#!/usr/bin/env python3
"""Basic structural regression checks for skill markdown files."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_FILES = [
    f"skill_{i}_{name}.md"
    for i, name in [
        (0, "master_orchestrator"),
        (1, "intent_discovery"),
        (2, "content_strategist"),
        (3, "draft_architect"),
        (4, "voice_tone_refiner"),
        (5, "engagement_optimizer"),
        (6, "quality_reviewer"),
        (7, "archive_manager"),
        (8, "poster_reviewer"),
    ]
]

REQUIRED_SECTIONS = {
    "skill_0_master_orchestrator.md": ["## Overview", "## Pipeline Sequence", "## State Management"],
    "skill_1_intent_discovery.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_2_content_strategist.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_3_draft_architect.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_4_voice_tone_refiner.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_5_engagement_optimizer.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_6_quality_reviewer.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_7_archive_manager.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
    "skill_8_poster_reviewer.md": ["## Overview", "## Inputs", "## Outputs", "## Workflow"],
}

REQUIRED_PHRASES = {
    "skill_0_master_orchestrator.md": [
        "checkpoint 5a",
        "checkpoint 6a",
        "state management",
    ],
    "skill_1_intent_discovery.md": ["5-question", "strategic intent document"],
    "skill_2_content_strategist.md": ["6-week", "narrative"],
    "skill_3_draft_architect.md": ["anti-ai", "constraints"],
    "skill_4_voice_tone_refiner.md": ["workflow", "ai"],
    "skill_5_engagement_optimizer.md": ["hitl 5a", "linkedin"],
    "skill_6_quality_reviewer.md": ["checkpoint 6a", "1-5"],
    "skill_7_archive_manager.md": ["archive", "md-to-pdf"],
    "skill_8_poster_reviewer.md": ["option a", "option b"],
}


def main() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.exists():
        errors.append(f"Missing skills directory: {SKILLS_DIR}")
        report(errors)
        return 1

    for file_name in REQUIRED_FILES:
        file_path = SKILLS_DIR / file_name
        if not file_path.exists():
            errors.append(f"Missing required skill file: {file_name}")
            continue

        content = file_path.read_text(encoding="utf-8")
        lower = content.lower()

        for section in REQUIRED_SECTIONS.get(file_name, []):
            if section not in content:
                errors.append(f"{file_name}: missing required section '{section}'")

        for phrase in REQUIRED_PHRASES.get(file_name, []):
            if phrase.lower() not in lower:
                errors.append(f"{file_name}: missing required phrase '{phrase}'")

    if errors:
        report(errors)
        return 1

    print("Skill regression checks passed: all required files, sections, and anchor phrases found.")
    return 0


def report(errors: list[str]) -> None:
    print("Skill regression checks failed:")
    for err in errors:
        print(f" - {err}")


if __name__ == "__main__":
    sys.exit(main())
