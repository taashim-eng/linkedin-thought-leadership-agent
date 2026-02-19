---
name: content-strategist
description: Takes the Strategic Intent Document and creates a cohesive 6-week LinkedIn content roadmap with weekly themes, titles, and narrative arc.
---

# Skill 2: Content Strategist

## Overview
Transforms the Strategic Intent Document into a structured 6-week content calendar. Each week has a specific angle that builds on the previous one, creating a narrative arc that keeps readers engaged across the full series.

## Inputs
- **Strategic Intent Document**: Output from Skill 1 (audience, message, anecdote, CTA, tone).

## Outputs
- **6-Week Content Roadmap**: A table with weekly themes, working titles, and brief descriptions.

## Workflow

### Step 1: Define the 6-Week Narrative Arc
Map the series to this proven engagement structure:

| Week | Arc Position | Purpose |
|------|-------------|---------|
| 1 | **The Hook** | Surface a pain point the audience recognizes |
| 2 | **The Framework** | Introduce a mental model or approach |
| 3 | **The Story** | Share the personal anecdote (from Q3) |
| 4 | **The Tactics** | Provide concrete, actionable advice |
| 5 | **The Vision** | Connect to the future (AI, industry trends) |
| 6 | **The Call** | Synthesize the series + drive the final CTA |

### Step 2: Generate Working Titles and Descriptions
For each week, create:
- **Working Title**: A compelling, specific headline (not generic)
- **Objective**: What the reader should think/feel/do after this post
- **Key Content**: 2-3 bullet points on what the post will cover
- **"What's Next" Teaser**: A one-sentence bridge to the next week

### Step 3: Validate Narrative Cohesion
Review the 6-week plan as a whole:
- Does each week logically follow the previous one?
- Is the personal anecdote placed in Week 3 for maximum impact?
- Does the series build toward the CTA in Week 6?

## Constraints
- Each week MUST have a distinct angle — no two weeks should feel like the same post reworded.
- The roadmap must align with the Core Message from the Strategic Intent Document.
- Keep descriptions concise (2-3 sentences per week).

## Failure Modes
- **Topic too narrow**: If the topic can't sustain 6 unique angles, suggest broadening it or combining related subtopics.
- **Topic too broad**: If the topic is too wide, suggest narrowing to a specific facet that matches the audience.

## Example Output
```markdown
# 6-Week Roadmap: Optimizing SQL Query Performance

| Week | Title | Objective |
|------|-------|-----------|
| 1 | The "Good Enough" Trap | Hook: Make readers question their SQL performance complacency |
| 2 | The Instant Satisfaction Gap | Framework: Introduce the speed-expectation mismatch |
| 3 | Near Real-Time is the New Baseline | Story: Share the personal war story |
| 4 | Technical Levers for Time-to-Market | Tactics: 5 concrete optimization techniques |
| 5 | AI-Ready Infrastructure | Vision: Connect SQL to agentic AI readiness |
| 6 | The Strategic Pivot | Call: Synthesize and drive the follow CTA |
```
