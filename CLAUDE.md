# LinkedIn Thought Leadership Agent — Project Memory

## Project Overview
- **What**: 9-skill agentic pipeline that generates 6-week LinkedIn thought leadership series
- **Assignment**: MSIS 549 B HW2 — Agentic AI for Real-World Impact (Path A: Skills Pack)
- **Repo**: https://github.com/taashim-eng/linkedin-thought-leadership-agent
- **Status**: Complete — skills polished, benchmark done, test run done, MCP authenticated, ready to post

## Pipeline Architecture
Skills 0-8 in sequence: Orchestrator → Intent Discovery (5Q interview) → Content Strategist (6-week arc) → Draft Architect → Voice Refiner → Engagement Optimizer (HITL 5a) → Quality Reviewer (HITL 6a) → Archive Manager → Poster (MCP)

## Key Files
- `skills/skill_0-8_*.md` — The 9 skill files (the actual deliverable)
- `TUTORIAL_WRITEUP.md` — Comprehensive tutorial for submission
- `benchmark/BENCHMARK_APPENDIX.md` — 4 test cases, scoring rubrics, failure analysis
- `diagrams/architecture_infographic.html` — A4 landscape solution architecture
- `diagrams/week1-6_*.html` — Visual diagrams for each LinkedIn post (1080x1080 HTML)
- `outputs/test_run_AI_Dev_Tool_Series.md` — Full test run output (6 posts, all approved)
- `archive/AI_Chatbot_to_Dev_Tool_2026-02-11.md` — Full archived session with benchmark

## Test Run: "IT Moving from AI Chatbot to Dev Tool" (2026-02-11)
- **Topic**: IT Moving from AI as a Search Chatbot to a Dev Tool
- **Audience**: IT Professionals and Leadership Teams
- **Tone**: Provocative + Educational
- **Anecdote**: AI-embedded testing — from 2 weeks to 2 minutes, developers review instead of write tests
- **CTA**: Create a safe, incentivized space for teams to use AI in IDEs

### 6 Posts (all approved, benchmark 4.5/5.0)
| Week | Title | Visual |
|------|-------|--------|
| 1 | "Your Team Is Using AI Wrong" | `diagrams/week1_ai_usage_gap.html` |
| 2 | "The AI Maturity Ladder: Chat → Copilot → Partner" | `diagrams/week2_ai_maturity_ladder.html` |
| 3 | "How AI Fixed Our Testing Problem" | `diagrams/week3_testing_before_after.html` |
| 4 | "5 Ways to Move from Chat to IDE" | `diagrams/week4_five_moves.html` |
| 5 | "The AI-Native Dev Team of 2027" | `diagrams/week5_2024_vs_2027.html` |
| 6 | "Stop Asking. Start Building." | `diagrams/week6_series_journey.html` |

### Benchmark Scores
| Metric | Score |
|--------|:---:|
| Actionability | 4.2 |
| Voice Consistency | 4.7 |
| Strategic Depth | 4.3 |
| Narrative Cohesion | 4.8 |
| LinkedIn Optimization | 4.7 |
| **Overall** | **4.5** |

## LinkedIn MCP Setup — FULLY CONFIGURED
- **Package**: `@ldraney/mcp-linkedin` (installed globally via npm)
- **Binary**: `C:\Users\taash\AppData\Roaming\npm\mcp-linkedin.cmd`
- **Config**: In `C:\Users\taash\.claude\settings.json` as `"linkedin"` MCP server
- **Auth**: COMPLETE — OAuth done for Merc Wahuri (test account)
- **Person ID**: hYPf1hbAJR (Merc Wahuri)
- **Token expiry**: ~60 days from 2026-02-11 (renew mid-April 2026)
- **Status**: READY TO POST — just needed Claude Code restart to load MCP

## Publishing Log
| Week | Title | Status | Post URN | Posted |
|------|-------|--------|----------|--------|
| 1 | "Your Team Is Using AI Wrong" | LIVE | `urn:li:share:7430329696413843458` | 2026-02-11 |
| 2 | "The AI Maturity Ladder" | Pending | — | — |
| 3 | "How AI Fixed Our Testing Problem" | Pending | — | — |
| 4 | "5 Ways to Move from Chat to IDE" | Pending | — | — |
| 5 | "The AI-Native Dev Team of 2027" | Pending | — | — |
| 6 | "Stop Asking. Start Building." | Pending | — | — |

**Note**: MCP tools did not load into Claude Code session. Posts can be made directly via LinkedIn API using the access token + person ID in settings.json. Use the Node.js API call pattern (see previous session).

## NEXT STEPS
1. Add visual to Week 1 post — open `diagrams/week1_ai_usage_gap.html`, screenshot, attach on LinkedIn
2. Screenshot impressions at 24-48hrs for homework evidence
3. Post Weeks 2-6 on weekly cadence (Tue-Thu, 8-10am recommended)
4. Convert `TUTORIAL_WRITEUP.md` to PDF for assignment submission

### Week 1 Post Text (ready to copy/post)
```
Most IT teams spent 2024 rolling out AI. The result? Expensive autocomplete.

Your developers are using ChatGPT to Google things faster. Your managers are using Copilot to summarize emails. Nobody is actually building with it.

Here's the uncomfortable truth: if your team's primary use of AI is "ask it a question and read the answer," you haven't adopted AI. You've adopted a search engine with better grammar.

The gap between teams that use AI to ask questions and teams that use AI to write, test, and ship code is widening every quarter. One group is getting incrementally faster at finding answers. The other is fundamentally changing how software gets built.

I've watched this play out across multiple teams. The ones still treating AI as a chatbot aren't falling behind slowly — they're standing still while the ground moves under them.

The question isn't whether your team uses AI. It's whether they use it for anything that actually ships.

AI adoption isn't a binary. Most teams are stuck at Level 1 — and they don't even know there are levels.

Ask your developers one question this week: "What did AI help you build last sprint?" If the answer is "nothing" — that's your signal.

#AIinIT #SoftwareDevelopment #DevProductivity #AIAdoption #AIDevPartner

Coming Next Week: The 3 levels of AI maturity — and why most teams can't get past Level 1.
```

## Subsequent Steps (after Week 1 posts)
5. **Capture engagement**: Screenshot LinkedIn impressions at 24-48hrs — add to benchmark as real-world evidence
6. **Post remaining weeks**: Weeks 2-6 on weekly cadence (Tue-Thu, 8-10am recommended)
7. **PDF conversion**: Convert `TUTORIAL_WRITEUP.md` to PDF for assignment submission
8. **GitHub**: Already pushed (3 commits). May want final commit after posting evidence added.

## Benchmark Summary (all test cases)
| Test Case | Overall Score |
|-----------|:---:|
| AI Chatbot to Dev Tool (live test run) | 4.5 |
| SQL Performance (original Manus run) | 4.5 |
| Data Cleanliness (original Manus run) | 4.2 |
| WAL Protocol (edge case) | 3.4 |
| Vague Input (ambiguous) | 3.6 |
| Single-Prompt Baseline | 2.0 |

## User Preferences
- Visuals/diagrams for EVERY post (HTML format, 1080x1080 for LinkedIn)
- Provocative + Educational tone preferred
- Test runs use Merc Wahuri LinkedIn account
- Values practical, specific content over generic thought leadership
- Save CLAUDE.md before every restart for continuity
