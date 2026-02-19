# LinkedIn Thought Leadership Agent — Project Memory

## Project Overview
- **What**: 9-skill agentic pipeline that generates 6-week LinkedIn thought leadership series
- **Assignment**: MSIS 549 B HW2 — Agentic AI for Real-World Impact (Path A: Skills Pack)
- **Repo**: https://github.com/taashim-eng/linkedin-thought-leadership-agent
- **Status**: Complete — skills polished, benchmark done, test run done, repo pushed

## Pipeline Architecture
Skills 0-8 in sequence: Orchestrator → Intent Discovery (5Q interview) → Content Strategist (6-week arc) → Draft Architect → Voice Refiner → Engagement Optimizer (HITL 5a) → Quality Reviewer (HITL 6a) → Archive Manager → Poster (MCP)

## Key Files
- `skills/skill_0-8_*.md` — The 9 skill files (the actual deliverable)
- `TUTORIAL_WRITEUP.md` — Comprehensive tutorial for submission
- `benchmark/BENCHMARK_APPENDIX.md` — 4 test cases, scoring rubrics, failure analysis
- `diagrams/architecture_infographic.html` — A4 landscape solution architecture
- `diagrams/week1-6_*.html` — Visual diagrams for each LinkedIn post (1080x1080 HTML)
- `outputs/test_run_AI_Dev_Tool_Series.md` — Full test run output (6 posts)
- `outputs/Q1_2026_SQL_Performance_Series.md` — Original SQL series output
- `archive/AI_Chatbot_to_Dev_Tool_2026-02-11.md` — Archived test run session

## Test Run Completed (2026-02-11)
- **Topic**: IT Moving from AI as a Search Chatbot to a Dev Tool
- **Audience**: IT Professionals and Leadership Teams
- **6 Posts**: "Your Team Is Using AI Wrong" → "AI Maturity Ladder" → "How AI Fixed Our Testing" → "5 Moves: Chat to IDE" → "AI-Native Team of 2027" → "Stop Asking. Start Building."
- **Benchmark**: 4.5/5.0 overall (strongest: Cohesion 4.8, Voice 4.7)
- **HITL 5a**: Approved without revisions
- **HITL 6a**: Approved
- **Visuals**: 6 HTML diagrams created, one per post

## LinkedIn MCP Setup
- **Package**: `@ldraney/mcp-linkedin` (installed globally via npm)
- **Binary**: `C:\Users\taash\AppData\Roaming\npm\mcp-linkedin.cmd`
- **Config**: Added to `C:\Users\taash\.claude\settings.json` as `"linkedin"` MCP server
- **Auth**: OAuth flow — will prompt browser login on first use after Claude Code restart
- **Status**: Configured but NOT yet authenticated. Needs Claude Code restart to load.

## Next Steps
1. **Restart Claude Code** to load LinkedIn MCP server
2. **Authenticate** via browser OAuth when prompted
3. **Post Week 1** using `linkedin_create_post` tool with the Week 1 text
4. **Attach visual**: Screenshot `diagrams/week1_ai_usage_gap.html` and attach to post
5. **Capture engagement**: Screenshot LinkedIn impressions after 24-48hrs for homework evidence
6. **Optional**: Convert TUTORIAL_WRITEUP.md to PDF for submission
7. **Optional**: Push final commit with CLAUDE.md to GitHub

## Benchmark Summary (for reference)
| Test Case | Overall Score |
|-----------|:---:|
| SQL Performance (original) | 4.5 |
| Data Cleanliness (original) | 4.2 |
| AI Chatbot to Dev Tool (test run) | 4.5 |
| WAL Protocol (edge case) | 3.4 |
| Vague Input (ambiguous) | 3.6 |
| Single-Prompt Baseline | 2.0 |

## User Preferences
- Visuals/diagrams for EVERY post (HTML format, 1080x1080 for LinkedIn)
- Provocative + Educational tone preferred
- Wants real LinkedIn posting, not just drafts
- Values practical, specific content over generic thought leadership
