---
name: quality-reviewer-benchmark
description: Performs a structured quality review of the 6-post series against defined metrics. Runs the mini-benchmark and presents results for user approval (HITL checkpoint 6a).
---

# Skill 6: Quality Reviewer + Benchmark (HITL Checkpoint 6a)

## Overview
Acts as the final editor and quality gate. Reviews the approved series for consistency, alignment with intent, and overall quality. Runs a structured mini-benchmark and presents results to the user.

## Inputs
- **Optimized Posts**: Output from Skill 5 (user-approved after HITL 5a).
- **Strategic Intent Document**: Output from Skill 1 (for alignment check).

## Outputs
- **Quality Scorecard**: Per-post and aggregate scores across 5 metrics.
- **Failure Analysis**: Description of any post that scored below 3.0.
- **User Approval**: Collected during HITL checkpoint 6a.

## Workflow

### Step 1: Quality Review Checklist
Review each post against these criteria:

| Check | Question | Action if Failed |
|-------|----------|-----------------|
| Clarity | Can a non-expert understand the key point? | Simplify jargon |
| Consistency | Does this post fit the series narrative arc? | Revise transitions |
| Alignment | Does it serve the Core Message from Skill 1? | Refocus the content |
| Authenticity | Does it sound like the leader, not AI? | Re-invoke Skill 4 |
| Engagement | Is the hook strong? Is the CTA clear? | Re-invoke Skill 5 |

### Step 2: Run Mini-Benchmark
Score each post on a 1-5 scale across these metrics:

**Metric 1 — Actionability**: Does the post give the reader something concrete to do?
- 5: Specific, immediately actionable advice with measurable outcome
- 3: General advice that requires interpretation
- 1: Vague inspiration with no clear next step

**Metric 2 — Voice Consistency**: Does this post sound like the same leader as the others?
- 5: Indistinguishable from real leader's writing; consistent across all 6 posts
- 3: Professional but could be anyone; minor voice drift between posts
- 1: Obviously AI-generated; voice varies wildly between posts

**Metric 3 — Strategic Depth**: Does the post demonstrate genuine expertise?
- 5: Reveals insider knowledge, specific examples, or contrarian insights
- 3: Covers standard industry talking points competently
- 1: Surface-level observations that any reader could have written

**Metric 4 — Narrative Cohesion**: Does this post build on previous weeks and tease the next?
- 5: Clear thread connecting all 6 weeks; "What's Next" teasers create anticipation
- 3: Posts are loosely related but could be reordered without loss
- 1: Posts feel like 6 unrelated articles on the same broad topic

**Metric 5 — LinkedIn Optimization**: Is the post formatted for maximum engagement?
- 5: Strong hook, clean formatting, appropriate hashtags, visual recommendation
- 3: Acceptable formatting but hook is weak or hashtags are generic
- 1: Wall of text, no hook, no CTA, no hashtags

### Step 3: Calculate Aggregate Scores
- Per-post average (across 5 metrics)
- Per-metric average (across 6 posts)
- Overall series average
- Identify the weakest post and the weakest metric

### Step 4: HITL Checkpoint 6a
**PAUSE the pipeline.** Present the scorecard:

> "Quality Benchmark Results:
>
> | Post | Actionability | Voice | Depth | Cohesion | LinkedIn | Avg |
> |------|:---:|:---:|:---:|:---:|:---:|:---:|
> | Week 1 | X | X | X | X | X | X.X |
> | ... | ... | ... | ... | ... | ... | ... |
> | **Average** | X.X | X.X | X.X | X.X | X.X | **X.X** |
>
> **Weakest Post**: Week X (score: X.X) — [reason]
> **Weakest Metric**: [metric] (score: X.X) — [recommendation]
>
> Do you approve these results, or would you like me to revise specific posts?"

**Gate**: Do NOT proceed until user approves.

## Constraints
- Benchmark must be run with frozen prompts — no ad-hoc scoring.
- All scores must be justified with a brief rationale (not just numbers).
- If any post scores below 3.0 on any metric, it MUST be flagged.

## Failure Modes
- **Score inflation**: If all posts score 5.0, the rubric is too lenient. Review the anchors critically.
- **Inconsistent scoring**: Ensure the same standard is applied to all 6 posts.
