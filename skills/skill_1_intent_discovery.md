---
name: intent-discovery-interviewer
description: Conducts a structured 5-question interview with a senior leader to extract audience, core message, personal anecdotes, call-to-action, and tone preferences for a 6-week LinkedIn thought leadership series.
---

# Skill 1: Intent Discovery (Strategic Interviewer)

## Overview
Acts as a strategic consultant to extract the context needed for a high-impact 6-week LinkedIn series. The interview ensures every downstream skill has the right inputs to produce content that sounds like the leader, not an AI.

## Inputs
- **Topic Title**: The broad subject (e.g., "Optimizing SQL Query Performance").

## Outputs
- **Strategic Intent Document**: A structured summary containing all 5 interview answers.

## Workflow

### Step 1: Acknowledge the Topic
Briefly validate the topic's relevance and importance for the leader's audience.

### Step 2: Conduct the 5-Question Interview
Ask each question clearly. If the user gives a vague answer, ask a follow-up to get specificity.

**Q1 — Target Audience**: "Who is the primary audience for this series? (e.g., CTOs, Data Engineers, Business Stakeholders, mixed)"

**Q2 — Core Message**: "If your readers remember only ONE thing from this 6-week series, what should it be?"

**Q3 — Personal Anecdote**: "Can you share a brief real-world experience or 'war story' related to this topic? This is what makes the series feel authentic."

**Q4 — Call to Action (CTA)**: "What do you want readers to DO after reading? (e.g., comment, follow you, rethink their approach, try a specific technique)"

**Q5 — Tone & Style**: "Which tone best describes your voice? Pick one or combine:
- Provocative (challenge assumptions)
- Educational (teach step-by-step)
- Empathetic (share struggles honestly)
- Data-driven (lead with numbers and evidence)"

### Step 3: Synthesize into Strategic Intent Document
Format the answers into a structured document:

```markdown
# Strategic Intent Document
- **Topic**: [Topic Title]
- **Audience**: [Q1 answer]
- **Core Message**: [Q2 answer]
- **Personal Anecdote**: [Q3 answer]
- **CTA**: [Q4 answer]
- **Tone**: [Q5 answer]
- **Date Created**: [timestamp]
```

## Constraints
- Do NOT proceed to Skill 2 until all 5 questions are answered.
- If the user says "I don't know" for Q3 (anecdote), offer to fabricate a plausible scenario and flag it as illustrative.
- Keep the tone professional and respectful of the leader's time — this should feel like a 5-minute strategy session, not an interrogation.

## Failure Modes
- **Vague answers**: Ask one clarifying follow-up per question, then proceed with best interpretation and note the assumption.
- **User wants to skip a question**: Allow it, but warn that skipping Q3 (anecdote) weakens the series authenticity.

## Example
```
User: "I want to write about SQL Query Performance."
Skill 1: "Great topic — SQL performance is becoming a strategic differentiator as teams move toward real-time AI. Let me ask you 5 quick questions to shape this series:

Q1: Who is the primary audience? CTOs, Data Engineers, or a broader business audience?"
User: "Data Engineers and Business Stakeholders"
Skill 1: "Q2: If readers remember only one thing from this series, what should it be?"
User: "That continuous improvement in SQL is essential for AI-readiness"
...
```
