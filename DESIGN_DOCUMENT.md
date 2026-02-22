# LinkedIn Thought Leadership Agent — Design Document

**Author**: Taashi Manyanga
**Version**: 1.0 (Claude Edition)
**Date**: February 2026
**Repository**: https://github.com/taashim-eng/linkedin-thought-leadership-agent

---

## 1. System Overview

### 1.1 Purpose
The LinkedIn Thought Leadership Agent is a 9-skill sequential pipeline that transforms a user's topic and domain expertise into a polished, cohesive 6-week LinkedIn content series. It enforces narrative structure, authentic voice, quality benchmarking, and optional automated publishing.

### 1.2 Design Philosophy
- **Single responsibility per skill**: Each skill does exactly one thing. Debugging is immediate — if voice sounds wrong, look at Skill 4.
- **Sequential pipeline over parallel**: Posts must form a narrative arc; parallel generation produces disconnected content.
- **Human judgment at every gate**: Two mandatory HITL checkpoints ensure the user controls quality.
- **Reproducibility first**: Every session is archived with full metadata so any run can be reconstructed.

### 1.3 Architecture Type
Path A — Agentic Skills Pack (Markdown files)
Platform-agnostic: tested on Manus AI and Claude Code.

---

## 2. Component Inventory

| # | Skill File | Name | Phase | Type |
|---|-----------|------|-------|------|
| 0 | `skill_0_master_orchestrator.md` | Master Orchestrator | All | Controller |
| 1 | `skill_1_intent_discovery.md` | Intent Discovery | Phase 1 | Input |
| 2 | `skill_2_content_strategist.md` | Content Strategist | Phase 2 | Planner |
| 3 | `skill_3_draft_architect.md` | Draft Architect | Phase 3 | Generator |
| 4 | `skill_4_voice_tone_refiner.md` | Voice & Tone Refiner | Phase 3 | Transformer |
| 5 | `skill_5_engagement_optimizer.md` | Engagement Optimizer | Phase 3 + HITL | Formatter |
| 6 | `skill_6_quality_reviewer.md` | Quality Reviewer | Phase 5 + HITL | Evaluator |
| 7 | `skill_7_archive_manager.md` | Archive Manager | Phase 6 | Persister |
| 8 | `skill_8_poster_reviewer.md` | Poster & Reviewer | Phase 6 | Publisher |

---

## 3. Skill Interface Specifications

### Skill 0: Master Orchestrator

| | |
|---|---|
| **Trigger** | User states topic intent |
| **Inputs** | Topic string from user |
| **Outputs** | Orchestrates all phases; final confirmation |
| **State Managed** | `strategic_intent`, `roadmap`, `drafts[]`, `feedback_log`, `benchmark_scores` |
| **Gates** | Phase 1→2: all 5 interview answers complete; Phase 3→4: HITL 5a approved; Phase 5→6: HITL 6a approved |
| **Error Recovery** | Retry / skip / abort options on any skill failure |

### Skill 1: Intent Discovery

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 1 |
| **Inputs** | Topic title (string) |
| **Outputs** | Strategic Intent Document (structured markdown) |
| **Fields Produced** | Topic, Audience, Core Message, Personal Anecdote, CTA, Tone |
| **Constraint** | Must not proceed until all 5 questions answered |
| **Failure Mode** | Vague answer → one follow-up then best-interpretation with flagged assumption |

### Skill 2: Content Strategist

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 2 |
| **Inputs** | Strategic Intent Document |
| **Outputs** | 6-Week Content Roadmap (table: week, arc position, title, objective, key content, teaser) |
| **Arc Structure** | Week 1: Hook → Week 2: Framework → Week 3: Story → Week 4: Tactics → Week 5: Vision → Week 6: Call |
| **Constraint** | Each week must have a distinct angle; no two weeks can be the same post reworded |
| **Failure Mode** | Topic too narrow → suggest broadening; topic too broad → suggest narrowing |

### Skill 3: Draft Architect

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 3 |
| **Inputs** | Strategic Intent Document + 6-Week Roadmap |
| **Outputs** | 6 initial post drafts (150-300 words each) |
| **Post Structure** | Hook / Body (2-3 paragraphs) / Insight / CTA / Hashtags (3-5) / Teaser |
| **Constraint** | Anti-AI-ism rules enforced (banned patterns list); personal anecdote in Week 3 only |
| **Failure Mode** | Draft too generic → add specificity; draft too long → tighten |

**Banned Patterns (Skill 3)**:
- "In today's fast-paced world..." / "In the era of..."
- "Let's dive in..." / "Let's explore..."
- "It's important to note that..."
- "In conclusion..." / "To sum up..."
- Excessive hedging ("might," "could potentially")
- Lists that start with "Here are X things..."

### Skill 4: Voice & Tone Refiner

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 3 (after Skill 3) |
| **Inputs** | 6 initial drafts + Tone specification from Strategic Intent |
| **Outputs** | 6 refined drafts with leader's voice applied |
| **Detection Table** | AI patterns identified and replaced (see table below) |
| **Constraint** | Do not change core message or structure; do not make posts longer |
| **Failure Mode** | Over-refinement → dial back; tone mismatch → re-apply tone table |

**Detection & Replacement Table (Skill 4)**:

| AI Pattern | Replacement Rule |
|-----------|-----------------|
| "In today's fast-paced world" | Delete — start with specific claim |
| "Let's dive in" / "Let's explore" | Delete — start content directly |
| "It's important to note" | Delete — if important, reader sees it |
| "This is a game-changer" | Replace with specific impact metric |
| "Leverage" / "Synergy" | Replace with plain language |
| "In conclusion" | Delete — CTA serves this purpose |
| "In the era of AI" | Delete — start with specific claim |

**Tone Application Table (Skill 4)**:

| Tone | Technique |
|------|-----------|
| Provocative | Bold claims, rhetorical questions, challenges to assumptions |
| Educational | Numbered steps, "here's how" framing, concrete examples |
| Empathetic | First-person struggles, "I've been there" language |
| Data-driven | Lead with statistics, percentages, benchmark comparisons |

### Skill 5: Engagement Optimizer

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 3 (after Skill 4) |
| **Inputs** | 6 refined drafts |
| **Outputs** | 6 LinkedIn-optimized posts + visual recommendations + HITL 5a user feedback |
| **Hook Rule** | Must fit within 200 chars; must not start with "I"; must create curiosity or tension |
| **Formatting Rules** | Short paragraphs (1-3 sentences), line breaks between paragraphs, max 5 hashtags |
| **Visuals** | One visual recommendation per post; HTML diagram if relevant (1080x1080 preferred) |
| **HITL 5a** | PAUSE — user reviews all 6 posts; each gets Approve / Revise / Reject response |
| **Routing on Revision** | Voice/tone → re-invoke Skill 4; content/structure → re-invoke Skill 3; formatting → apply in Skill 5 |

**Visual Recommendation Guidelines**:

| Week | Visual Type |
|------|------------|
| 1 | Conceptual split-screen / comparison |
| 2 | Framework ladder / staircase |
| 3 | Before/after process flow |
| 4 | Numbered action list infographic |
| 5 | Timeline comparison (present vs future) |
| 6 | Series journey map |

### Skill 6: Quality Reviewer

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 5 (after HITL 5a approval) |
| **Inputs** | 6 approved posts + Strategic Intent Document |
| **Outputs** | Quality Scorecard (per-post + aggregate) + HITL 6a user feedback |
| **Scoring Scale** | 1-5 per metric, per post; aggregate per metric and overall |
| **Threshold** | Any post scoring below 3.0 on any metric → flagged for mandatory revision |
| **HITL 6a** | PAUSE — user reviews scorecard; approve or request changes |

**Scoring Rubric (Skill 6)**:

| Metric | 5 (Excellent) | 3 (Acceptable) | 1 (Poor) |
|--------|:---:|:---:|:---:|
| Actionability | Specific, immediately actionable, measurable outcome | General advice requiring interpretation | Vague inspiration, no next step |
| Voice Consistency | Indistinguishable from real leader; consistent all 6 posts | Professional but generic; minor drift | Obviously AI-generated; voice varies |
| Strategic Depth | Insider knowledge, specific examples, contrarian insight | Standard industry points, competent | Surface observations anyone could write |
| Narrative Cohesion | Clear thread all 6 weeks; teasers create anticipation | Loosely related; could be reordered | 6 unrelated articles on same broad topic |
| LinkedIn Optimization | Strong hook, clean formatting, hashtags, visual | Acceptable but hook weak or hashtags generic | Wall of text, no hook, no CTA |

### Skill 7: Archive Manager

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 6 (after HITL 6a approval) |
| **Inputs** | All prior outputs: strategic intent, roadmap, 6 posts, benchmark scores, feedback log |
| **Outputs** | `archive/[Topic_Slug]_[YYYY-MM-DD].md` + `.pdf` |
| **Naming Convention** | `archive/SQL_Query_Performance_2026-02-17.md` |
| **PDF Generation** | `md-to-pdf [file].md` (install: `npm install -g md-to-pdf`) |
| **Constraint** | Do NOT modify content — archive exactly what was approved |

### Skill 8: Poster & Reviewer

| | |
|---|---|
| **Trigger** | Invoked by Skill 0 at Phase 6 (optional) |
| **Inputs** | Final approved post(s); optional schedule |
| **Outputs** | Live LinkedIn post URL/URN; publication log entry |
| **Always Presents** | Option A (manual, recommended) + Option B1 (MCP) + Option B2 (direct API) |
| **Constraint** | ALWAYS confirm before publishing; never auto-post |
| **Token Lifespan** | 60 days; use `linkedin_refresh_token` or re-run OAuth on expiry |

---

## 4. State Management

The Master Orchestrator (Skill 0) maintains these artifacts throughout the session:

```
SESSION STATE
├── strategic_intent        ← Output of Skill 1; used by Skills 2, 3, 6
├── roadmap                 ← Output of Skill 2; used by Skill 3
├── drafts[]                ← Living array; updated by Skills 3, 4, 5
│   ├── draft_v1[]          ← Skill 3 output
│   ├── draft_v2[]          ← Skill 4 output
│   └── draft_v3[]          ← Skill 5 output (LinkedIn-optimized)
├── feedback_log            ← User feedback from HITL 5a and 6a
└── benchmark_scores        ← Output of Skill 6; stored in archive
```

---

## 5. Data Flow Diagram

```
User Input (Topic)
        │
        ▼
   [Skill 0: Orchestrator] ─── maintains session state ───────────────────┐
        │                                                                   │
   Phase 1: Discovery                                                       │
        │                                                                   │
   [Skill 1: Intent] ──► Strategic Intent Document                         │
        │                          │                                        │
   Phase 2: Strategy               │                                        │
        │                          ▼                                        │
   [Skill 2: Strategist] ──► 6-Week Roadmap                                │
        │                          │                                        │
   Phase 3: Creation               │                                        │
        │                          ▼                                        │
   [Skill 3: Drafter] ──► 6 Initial Drafts (v1)                           │
        │                          │                                        │
   [Skill 4: Refiner] ──► 6 Refined Drafts (v2)                           │
        │                          │                                        │
   [Skill 5: Optimizer] ──► 6 Optimized Posts (v3) + Visuals               │
        │                                                                   │
   Phase 4: HITL 5a                                                         │
        │                                                                   │
   ✋ USER REVIEW ──► Approve / Revise (loop) / Reject (loop)               │
        │                                                                   │
   Phase 5: Benchmark                                                       │
        │                                                                   │
   [Skill 6: Reviewer] ──► Quality Scorecard (5 metrics x 6 posts)         │
        │                                                                   │
   ✋ USER REVIEW ──► Approve / Request Changes (loop)                      │
        │                                                                   │
   Phase 6: Finalization                                                    │
        │                          │                                        │
   [Skill 7: Archive] ──► .md + .pdf saved to archive/         ◄───────────┘
        │
   [Skill 8: Poster] ──► LinkedIn post live (optional)
```

---

## 6. HITL Checkpoint Design

### Checkpoint 5a (Content Review)
- **Trigger**: After Skill 5 completes
- **User Decision**: Per post: Approve / Revise / Reject
- **Revision Routing**:
  - Voice/tone issue → re-invoke Skill 4 → re-run Skill 5
  - Content/structure issue → re-invoke Skill 3 → re-run Skills 4 and 5
  - Formatting only → apply directly in Skill 5
- **Gate**: ALL 6 posts must be approved before Phase 5 begins
- **Rationale**: Prevents benchmark effort on content the user would reject

### Checkpoint 6a (Benchmark Gate)
- **Trigger**: After Skill 6 completes
- **User Decision**: Approve scorecard / Request changes
- **If changes requested**: Loop back to Phase 3 with specific revision instructions
- **Gate**: User must explicitly approve before Phase 6 begins
- **Rationale**: Gives user confidence in quality metrics before archiving and publishing

---

## 7. Error Handling

| Error Scenario | Recovery Action |
|---------------|----------------|
| Skill fails to invoke | Log error; present Retry / Skip / Abort to user |
| Incomplete interview answers (Skill 1) | Prompt for clarification; proceed with flagged assumption if user declines |
| Draft too generic (Skill 3) | Add specific examples, numbers, or tool names before passing to Skill 4 |
| AI pattern detected post-refinement (Skill 4) | Rerun detection table; flag remaining instances |
| Benchmark score below 3.0 (Skill 6) | Mandatory flag; recommend re-invoking Skills 3-5 for the failing post |
| MCP tools not loading (Skill 8) | Fall back to Option B2 (direct API) or Option A (manual) |
| LinkedIn API 401 (Skill 8) | Access token expired; re-run OAuth flow |
| LinkedIn API 403 (Skill 8) | Missing `w_member_social` scope; re-authorize |

---

## 8. Security Design

| Concern | Mitigation |
|---------|-----------|
| LinkedIn API credentials | Stored in `~/.claude/settings.json` env vars only — never in skill files, archive files, or git repo |
| OAuth access tokens | 60-day expiry; stored locally on user's machine |
| Personal anecdotes in archives | Archive files should not be committed to public repos without review |
| `.gitignore` | Configured to block `.env`, credential files |

---

## 9. Known Limitations & Design Trade-offs

| Limitation | Root Cause | Mitigation / Future Fix |
|-----------|-----------|------------------------|
| Voice Refiner optimized for Manager/Director only | One-size-fits-all detection table | Add audience-specific voice profiles as a parameter |
| Week 5 (Vision) consistently underperforms | No access to real-time industry data | Add a "trends research" sub-step before Skill 3 for Week 5 |
| Single HITL rater bias | Only one human evaluator | Add peer review step for inter-rater reliability |
| No A/B testing on actual LinkedIn engagement | No LinkedIn Analytics API access | Manual engagement capture after 24-48 hours |
| MCP tools unreliable in Claude Code | MCP server initialization issues | Direct API fallback (Option B2) always available |
| Sequential pipeline is slower than parallel | Design choice for narrative coherence | Acceptable trade-off; pipeline runs in <10 mins for full series |

---

## 10. File & Directory Structure

```
linkedin-thought-leadership-agent/
├── README.md                          # Project overview
├── README.pdf                         # Human-readable PDF
├── TUTORIAL_WRITEUP.md                # Assignment submission
├── TUTORIAL_WRITEUP.pdf               # PDF version
├── DESIGN_DOCUMENT.md                 # This file
├── DESIGN_DOCUMENT.pdf                # PDF version
├── USER_GUIDE.md                      # How-to guide
├── USER_GUIDE.pdf                     # PDF version
├── CLAUDE.md                          # Session memory (not for submission)
├── .gitignore                         # Blocks credentials
├── skills/
│   ├── skill_0_master_orchestrator.md
│   ├── skill_1_intent_discovery.md
│   ├── skill_2_content_strategist.md
│   ├── skill_3_draft_architect.md
│   ├── skill_4_voice_tone_refiner.md
│   ├── skill_5_engagement_optimizer.md
│   ├── skill_6_quality_reviewer.md
│   ├── skill_7_archive_manager.md
│   └── skill_8_poster_reviewer.md
├── benchmark/
│   └── BENCHMARK_APPENDIX.md          # Full benchmark with 4 test cases
├── outputs/
│   ├── Q1_2026_SQL_Performance_Series.md
│   ├── 2026_Roadmap_Plan.md
│   └── test_run_AI_Dev_Tool_Series.md  # Live test run (Feb 2026)
├── diagrams/
│   ├── architecture_infographic.html  # A4 landscape solution overview
│   ├── week1_ai_usage_gap.html
│   ├── week2_ai_maturity_ladder.html
│   ├── week3_testing_before_after.html
│   ├── week4_five_moves.html
│   ├── week5_2024_vs_2027.html
│   └── week6_series_journey.html
└── archive/
    └── AI_Chatbot_to_Dev_Tool_2026-02-11.md  # Full archived session
```
