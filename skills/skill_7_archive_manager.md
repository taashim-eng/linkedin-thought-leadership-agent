---
name: archive-manager
description: Formats the complete session (intent, roadmap, posts, feedback, and benchmark scores) into a structured Markdown archive file for future reference and reproducibility.
---

# Skill 7: Archive Manager

## Overview
Acts as a digital librarian. Packages the entire session — from the initial interview through the final approved posts — into a single, well-structured Markdown file for the project's `archive/` directory.

## Inputs
- **Strategic Intent Document**: Output from Skill 1.
- **6-Week Roadmap**: Output from Skill 2.
- **Final Approved Posts**: Output from Skill 5 (after HITL 5a approval).
- **Benchmark Scorecard**: Output from Skill 6 (after HITL 6a approval).
- **Feedback Log**: All user feedback from HITL checkpoints.

## Outputs
- **Archive File**: A comprehensive Markdown file saved to `archive/[Topic]_[Date].md`.

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

### Step 2: Save the File
Save to: `archive/[Topic_Slug]_[YYYY-MM-DD].md`

Example: `archive/SQL_Query_Performance_2026-02-17.md`

### Step 3: Confirm to User
Present a summary:
> "Your 6-week series has been archived. File: `archive/SQL_Query_Performance_2026-02-17.md`
> This file contains your full session: intent, roadmap, all 6 posts, benchmark scores, and feedback log."

## Constraints
- Do NOT modify any content — archive exactly what was approved.
- Include ALL metadata for reproducibility.
- Use consistent file naming: `[Topic_Slug]_[YYYY-MM-DD].md`

## Failure Modes
- **Missing inputs**: If any input is missing (e.g., no benchmark was run), note it as "[Not Available]" in the archive rather than failing silently.
