---
name: linkedin-thought-leadership-orchestrator
description: Master orchestrator that coordinates the 9-skill pipeline for creating a 6-week LinkedIn thought leadership content series. Manages state, sequences skills, enforces human-in-the-loop checkpoints, and handles error recovery.
---

# LinkedIn Thought Leadership Master Orchestrator

## Overview
This skill is the "brain" of the LinkedIn Thought Leadership Agent. It sequences the 8 specialized skills (1-8), maintains state across phases, and enforces two mandatory Human-in-the-Loop (HITL) checkpoints before finalization.

## Pipeline Sequence

### Phase 1: Discovery
- Invoke `skill_1_intent_discovery` to conduct the 5-question strategic interview.
- **Output**: Strategic Intent Document (audience, message, anecdote, CTA, tone).
- **Gate**: All 5 questions must be answered before proceeding.

### Phase 2: Strategy
- Invoke `skill_2_content_strategist` with the Strategic Intent Document.
- **Output**: 6-Week Content Roadmap with weekly themes, titles, and objectives.

### Phase 3: Creation
- Invoke `skill_3_draft_architect` to generate 6 initial post drafts.
- Invoke `skill_4_voice_tone_refiner` to polish each draft for the leader's voice.
- Invoke `skill_5_engagement_optimizer` to add LinkedIn formatting, hooks, and hashtags.
- **Output**: 6 optimized, LinkedIn-ready post drafts.

### Phase 4: HITL Feedback (Checkpoint 5a)
- **PAUSE**: Present all 6 optimized posts to the user.
- Collect feedback on each post (approve, revise, or reject).
- If revisions requested: re-invoke Skills 4 and/or 5 with specific feedback.
- **Gate**: Proceed only when user explicitly approves all 6 posts.

### Phase 5: Quality & Benchmark (Checkpoint 6a)
- Invoke `skill_6_quality_reviewer` to run the quality benchmark.
- **PAUSE**: Present benchmark scores and analysis to the user.
- If scores below threshold or user requests changes: loop back to Phase 3.
- **Gate**: Proceed only when user approves benchmark results.

### Phase 6: Archive & Publish
- Invoke `skill_7_archive_manager` to save the complete session.
- (Optional) Invoke `skill_8_poster_reviewer` via LiGo MCP to publish to LinkedIn.

## State Management
Maintain these artifacts throughout the pipeline:
- `strategic_intent`: Output from Skill 1 (persists through all phases)
- `roadmap`: Output from Skill 2
- `drafts`: Current version of the 6 posts (updated by Skills 3-5)
- `feedback_log`: User feedback from HITL checkpoints
- `benchmark_scores`: Quality metrics from Skill 6

## Error Recovery
- If any skill fails, log the error and present options to the user: retry, skip, or abort.
- If the user provides incomplete interview answers, prompt for clarification before proceeding.
- If benchmark scores are below 3.0/5.0 on any metric, flag the series for revision.

## Example Usage
```
User: "I want to create a Q1 2026 LinkedIn series on SQL Query Performance."
Orchestrator: "Starting Phase 1: Intent Discovery. I'll ask you 5 strategic questions to shape this series..."
```
