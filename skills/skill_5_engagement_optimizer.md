---
name: engagement-optimizer
description: Optimizes refined drafts for LinkedIn's algorithm and readability. Adds hooks, formatting, visual recommendations, and hashtags. Includes the first Human-in-the-Loop checkpoint (HITL 5a).
---

# Skill 5: Engagement Optimizer + HITL Checkpoint 5a

## Overview
Prepares the refined drafts for maximum LinkedIn engagement. Optimizes formatting for the platform's algorithm, adds visual recommendations, and presents the complete series to the user for feedback.

## Inputs
- **Refined Drafts**: Output from Skill 4 (6 posts with leader's voice).

## Outputs
- **Optimized Posts**: 6 LinkedIn-ready posts with formatting, visuals, and hashtags.
- **User Feedback**: Collected during HITL checkpoint 5a.

## Workflow

### Step 1: Optimize the Hook (First 2 Lines)
LinkedIn truncates posts after ~210 characters with a "...see more" button. The hook MUST:
- Fit within 2 lines (< 200 characters)
- Create curiosity or tension that compels the click
- Avoid starting with "I" (LinkedIn's algorithm deprioritizes self-referential openings)

**Good hooks**: Questions, bold claims, surprising statistics, contrarian takes.
**Bad hooks**: "I'm excited to share...", "Here are 5 tips...", "Last week I..."

### Step 2: Format for Readability
Apply LinkedIn-optimized formatting:
- Short paragraphs (1-3 sentences max)
- Line breaks between paragraphs (LinkedIn collapses dense text)
- Bullet points for lists (max 5 items)
- Bold key phrases sparingly (LinkedIn supports basic markdown in some clients)

### Step 3: Add Visual Recommendations
For each post, suggest ONE visual:
- **Week 1-2**: Conceptual image or metaphor visual
- **Week 3**: Photo-style (authentic, human moment)
- **Week 4**: Infographic or technical diagram
- **Week 5**: Futuristic/vision-style visual
- **Week 6**: Professional portrait or branded graphic

Also suggest a system/architecture diagram where relevant (Mermaid or draw.io format).

### Step 4: Add Hashtags
Add 3-5 hashtags per post:
- 1-2 broad reach tags (e.g., #DataEngineering, #Leadership)
- 1-2 niche tags (e.g., #SQLPerformance, #AgenticAI)
- 1 series-specific tag (e.g., #SQLSeriesQ1)

### Step 5: HITL Checkpoint 5a
**PAUSE the pipeline.** Present all 6 optimized posts to the user with this prompt:

> "Here are your 6 optimized LinkedIn posts for the series. Please review each one and provide feedback:
> - **Approve**: This post is ready.
> - **Revise**: [Specify what to change]
> - **Reject**: [Explain why — I'll redraft from scratch]
>
> I'll update any posts with revisions before we proceed to quality benchmarking."

If the user requests changes:
- For voice/tone changes: re-invoke Skill 4, then re-run Skill 5
- For content/structure changes: re-invoke Skill 3, then Skills 4 and 5
- For formatting-only changes: apply directly in this skill

**Gate**: Do NOT proceed until user explicitly approves all 6 posts.

## Constraints
- Maximum 5 hashtags per post (more looks spammy).
- No emojis unless the user's tone is casual/playful.
- Visual recommendations are suggestions, not generated images.

## Failure Modes
- **Over-formatting**: If posts look like a marketing flyer, reduce formatting. LinkedIn favors conversational, essay-style posts.
- **Hook too clickbait-y**: If the hook promises more than the post delivers, tone it down.
