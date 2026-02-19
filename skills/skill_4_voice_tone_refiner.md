---
name: voice-tone-refiner
description: Ghostwriter skill that transforms initial drafts to match a senior leader's authentic voice. Removes AI-isms, adds professional weight, and aligns tone with the Strategic Intent Document.
---

# Skill 4: Voice & Tone Refiner

## Overview
Acts as a senior ghostwriter. Takes initial drafts and refines the language to sound like a real Manager/Director wrote them — authoritative, experienced, and human.

## Inputs
- **Initial Drafts**: Output from Skill 3 (6 posts).
- **Tone & Style**: From the Strategic Intent Document (e.g., "Provocative," "Educational").

## Outputs
- **Refined Drafts**: 6 posts with the leader's authentic voice applied.

## Workflow

### Step 1: Remove AI-isms
Scan each draft and eliminate:

| AI Pattern | Replace With |
|-----------|-------------|
| "In today's fast-paced world" | [Delete — start with a specific claim] |
| "Let's dive in" / "Let's explore" | [Delete — just start the content] |
| "It's important to note" | [Delete — if it's important, the reader will see it] |
| "In conclusion" | [Delete — the CTA serves this purpose] |
| "This is a game-changer" | [Replace with specific impact: "This cut our query time by 60%"] |
| "Leverage" / "Synergy" | [Replace with plain language: "use," "combined effort"] |

### Step 2: Add Professional Weight
Apply industry-standard strategic phrasing appropriate to the leader's level:
- "Strategic alignment" instead of "matching goals"
- "Operational efficiency" instead of "doing things faster"
- "Competitive advantage" instead of "being better than others"
- "Time-to-market" instead of "getting things done quickly"

### Step 3: Match the Requested Tone
Apply tone-specific adjustments:

| Tone | Technique |
|------|-----------|
| **Provocative** | Use direct challenges, rhetorical questions, bold claims |
| **Educational** | Use clear explanations, numbered steps, "here's how" framing |
| **Empathetic** | Use first-person struggles, "I've been there" language |
| **Data-driven** | Lead with statistics, percentages, benchmark comparisons |

### Step 4: Ensure Authority
- Replace passive voice with active voice
- Use "I" and "we" (first person) — leaders speak from experience
- Add specificity: replace "many companies" with "3 out of 4 data teams I've worked with"

## Constraints
- Do NOT change the core message, structure, or 6-week roadmap.
- Do NOT make posts longer — refinement should tighten, not expand.
- Preserve the personal anecdote exactly as the user provided it.

## Failure Modes
- **Over-refinement**: If the posts start sounding like a corporate press release, dial back. They should sound like a human expert, not a PR team.
- **Tone mismatch**: If the user requested "Provocative" but the output is "Educational," re-apply Step 3.

## Example
**Before** (AI-sounding):
> "In today's fast-paced world, it's important to note that SQL performance is a critical factor for businesses."

**After** (Leader's voice):
> "Your SQL queries are the foundation of every dashboard, every AI model, every real-time decision your team makes. If they're slow, everything downstream suffers."
