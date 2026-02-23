# Setup Guide

This guide provides portable setup and run instructions for the **LinkedIn Thought Leadership Agent** skills pack.

## 1) Prerequisites

### Required
- Git
- A markdown-capable AI coding/chat environment that supports skill files
- Node.js 18+ and npm (recommended for optional PDF export and link checks)

### Optional
- `md-to-pdf` for archive PDF generation
- LinkedIn MCP integration for automated posting

## 2) Clone the Repository

```bash
git clone https://github.com/taashim-eng/linkedin-thought-leadership-agent.git
cd linkedin-thought-leadership-agent
```

## 3) Install Skill Files

Copy the `skills/` directory into your assistant's local skills folder.

Example (Linux/macOS):

```bash
mkdir -p ~/.claude/skills/linkedin-thought-leadership-agent
cp -R skills ~/.claude/skills/linkedin-thought-leadership-agent/
```

> If your environment uses a different skills path, copy the same folder structure there.

## 4) Run the Workflow

Start a new session in your AI assistant and provide an initial prompt such as:

> "I want to create a LinkedIn thought leadership series about [TOPIC]."

The orchestrator should progress through:
1. Intent Discovery
2. Content Strategy
3. Draft Generation
4. Voice/Tone Refinement
5. Engagement Optimization
6. Quality Review
7. Archive
8. (Optional) Posting

## 5) Optional Tools

### A) PDF export for archives

```bash
npm install -g md-to-pdf
```

Then:

```bash
md-to-pdf archive/<topic_slug>_<yyyy-mm-dd>.md
```

### B) LinkedIn MCP automation

Automated posting depends on your local MCP host configuration and OAuth credentials.
Keep credentials in local secrets/config only (never commit tokens to this repository).

## 6) Local Quality Checks (Recommended)

Run the repository skill-regression checks:

```bash
python3 scripts/check_skill_regressions.py
```

For markdown linting (optional locally, enforced in CI):

```bash
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

## 7) Troubleshooting

- **Skills not loading**: verify copied path and restart your assistant session.
- **Inconsistent outputs**: re-run from Skill 1 with complete audience/message/anecdote/CTA inputs.
- **PDF generation fails**: use markdown viewer + print to PDF as fallback.
- **Automated posting unavailable**: use manual posting flow in `skills/skill_8_poster_reviewer.md`.
