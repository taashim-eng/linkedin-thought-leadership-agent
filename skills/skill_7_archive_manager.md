---
name: archive-manager
description: Formats the complete session (intent, roadmap, posts, feedback, and benchmark scores) into a structured Markdown archive file AND a human-readable PDF for future reference and reproducibility.
---

# Skill 7: Archive Manager

## Overview
Acts as a digital librarian. Packages the entire session — from the initial interview through the final approved posts — into a Markdown archive file AND a clean PDF version for easy human readability. Both files are saved to the `archive/` directory.

## Inputs
- **Strategic Intent Document**: Output from Skill 1.
- **6-Week Roadmap**: Output from Skill 2.
- **Final Approved Posts**: Output from Skill 5 (after HITL 5a approval).
- **Benchmark Scorecard**: Output from Skill 6 (after HITL 6a approval).
- **Feedback Log**: All user feedback from HITL checkpoints.

## Outputs
- **Archive Markdown File**: `archive/[Topic_Slug]_[YYYY-MM-DD].md` — machine-readable, version-controlled.
- **Archive PDF File**: `archive/[Topic_Slug]_[YYYY-MM-DD].pdf` — human-readable, printable, shareable.

## Workflow

### Step 1: Format the Archive
Create a Markdown file with this structure:

```markdown
# [Topic Title] — LinkedIn Thought Leadership Series
**Created**: [Date]  |  **Quarter**: [Q1/Q2/Q3/Q4 Year]  |  **Status**: Approved

---

## Strategic Intent
- **Audience**: [from Skill 1]
- **Core Message**: [from Skill 1]
- **Personal Anecdote**: [from Skill 1]
- **CTA**: [from Skill 1]
- **Tone**: [from Skill 1]

## 6-Week Roadmap
[Table from Skill 2]

## Final Posts

### Week 1: [Title]
[Full post text]

### Week 2: [Title]
[Full post text]

[...repeat for all 6 weeks]

## Benchmark Results
[Scorecard table from Skill 6]

## User Feedback Log
- **HITL 5a**: [Summary of feedback and changes made]
- **HITL 6a**: [Summary of benchmark review and approval]

## Metadata
- **Skills Used**: 1-7 (+ 8 if published)
- **LLM Platform**: [e.g., Claude, Manus, GPT-4]
- **Total Iterations**: [count of revision cycles]
```

### Step 2: Save the Markdown File
Save to: `archive/[Topic_Slug]_[YYYY-MM-DD].md`

Example: `archive/SQL_Query_Performance_2026-02-17.md`

### Step 3: Generate the PDF Version
Convert the archive Markdown to PDF using `md-to-pdf` (install if needed: `npm install -g md-to-pdf`):

```bash
md-to-pdf archive/[Topic_Slug]_[YYYY-MM-DD].md
```

This produces: `archive/[Topic_Slug]_[YYYY-MM-DD].pdf`

**PDF formatting guidelines**:
- Clean, readable typography (default md-to-pdf styles are appropriate)
- Each week's post should start on a new section with clear heading
- Tables (roadmap, benchmark) should render cleanly

If `md-to-pdf` is unavailable, instruct the user to open the `.md` file in a markdown viewer (VS Code, Typora, Obsidian) and use **Print → Save as PDF**.

### Step 4: Confirm to User
Present a summary:
> "Your 6-week series has been archived.
> - Markdown: `archive/SQL_Query_Performance_2026-02-17.md`
> - PDF: `archive/SQL_Query_Performance_2026-02-17.pdf`
>
> Both files contain your full session: intent, roadmap, all 6 posts, benchmark scores, and feedback log."

## Constraints
- Do NOT modify any content — archive exactly what was approved.
- Include ALL metadata for reproducibility.
- Use consistent file naming: `[Topic_Slug]_[YYYY-MM-DD].md` / `.pdf`
- PDF is for human readability only — the `.md` is the canonical source of truth.

## Failure Modes
- **Missing inputs**: If any input is missing (e.g., no benchmark was run), note it as "[Not Available]" in the archive rather than failing silently.
- **md-to-pdf unavailable**: Fall back to manual print-to-PDF instructions.
- **PDF rendering issues**: If tables or formatting break, open the `.md` in a browser-based renderer (e.g., GitHub) and print from there.
