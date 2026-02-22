# LinkedIn Thought Leadership Agent — User Guide

**Author**: Taashi Manyanga
**Version**: 1.0 (Claude Edition)
**Date**: February 2026
**Repository**: https://github.com/taashim-eng/linkedin-thought-leadership-agent

---

## Quick Summary

This system takes your topic + domain expertise and produces a polished 6-week LinkedIn series — with narrative arc, authentic voice, quality scoring, and optional automated publishing. It takes about 30-60 minutes end-to-end for a first run.

---

## Part 1: First-Time Setup

### What You Need
- Claude Code (CLI) or Manus AI — any LLM assistant that supports Markdown skill files
- A LinkedIn account (for publishing)
- 30-60 minutes for your first run

### Step 1: Clone the Repository
```bash
git clone https://github.com/taashim-eng/linkedin-thought-leadership-agent.git
cd linkedin-thought-leadership-agent
```

### Step 2: Install the Skills

**For Claude Code**:
```bash
mkdir -p ~/.claude/skills/linkedin-agent
cp skills/*.md ~/.claude/skills/linkedin-agent/
```

**For Manus AI**: Upload each file in `skills/` via the platform's skill upload interface.

**For any other LLM**: Copy the skill files into the appropriate directory for your platform's skill support.

### Step 3: Verify Installation
Open a new Claude Code session and type:
```
What LinkedIn thought leadership skills do you have available?
```
You should see the 9 skills listed (Master Orchestrator through Poster & Reviewer).

---

## Part 2: Running the Pipeline (Step-by-Step)

### Starting a New Series

Type this to begin:
```
I want to create a 6-week LinkedIn thought leadership series on [YOUR TOPIC].
```

The orchestrator will guide you through the rest. Here's what to expect at each stage:

---

### Stage 1: The Interview (5 minutes)
*Skill 1 — Intent Discovery*

You'll be asked 5 questions. Answer them honestly and specifically — the quality of your answers directly determines the quality of your posts.

**Q1 — Target Audience**
> "Who is the primary audience for this series?"

*Good answer*: "Data Engineers and Business Stakeholders at mid-size tech companies"
*Weak answer*: "Tech people"

**Q2 — Core Message**
> "If your readers remember only ONE thing, what should it be?"

*Good answer*: "Continuous improvement in SQL is essential for AI-readiness"
*Weak answer*: "SQL is important"

**Q3 — Personal Anecdote**
> "Can you share a real-world experience related to this topic?"

*Good answer*: "Our business team was frustrated when their dashboards were 24 hours behind reality — the root cause was slow SQL queries that couldn't keep up with our data volume"
*Weak answer*: "I've worked with SQL a lot"

**Tip**: If you skip Q3 (the anecdote), Week 3 will be weaker. The personal story is what separates your series from generic AI content.

**Q4 — Call to Action**
> "What do you want readers to DO after reading?"

Make this specific: "Run an EXPLAIN ANALYZE on their top 3 slowest queries" beats "think about performance".

**Q5 — Tone**
> Choose: Provocative / Educational / Empathetic / Data-driven (or combine)

---

### Stage 2: Approve the Roadmap (2 minutes)
*Skill 2 — Content Strategist*

You'll see a 6-week roadmap with titles and objectives. The arc follows:
- **Week 1**: Hook (the pain point)
- **Week 2**: Framework (a mental model)
- **Week 3**: Story (your anecdote)
- **Week 4**: Tactics (concrete advice)
- **Week 5**: Vision (future implications)
- **Week 6**: Call (synthesize + CTA)

**What to check**:
- Do the titles feel like YOUR voice?
- Is Week 3 using your actual anecdote?
- Does Week 6 connect back to your CTA?

Say "looks good, proceed" or request changes before moving on.

---

### Stage 3: Wait for Drafts (5-10 minutes)
*Skills 3, 4, 5 — Draft → Refine → Optimize*

The system runs three sub-stages automatically:
1. **Skill 3** writes initial 150-300 word drafts with anti-AI-ism rules applied
2. **Skill 4** refines voice to match your tone specification
3. **Skill 5** optimizes hooks, formatting, hashtags, and suggests visuals

You don't need to do anything during this stage.

---

### Stage 4: HITL Checkpoint 5a — Review All 6 Posts (10-15 minutes)
*Your most important input*

You'll see all 6 posts. For each one, respond with:

**APPROVE**: "Week 1 — Approve"

**REVISE**: "Week 2 — Revise: The hook is too generic, make it more provocative. Try starting with a question that challenges assumptions."

**REJECT**: "Week 4 — Reject: This misses the technical audience entirely. Restart with more specific database examples."

**Common revision patterns**:
- "Sounds too corporate" → ask to re-invoke Skill 4 with more casual voice
- "Too long" → ask to cut to 200 words
- "Missing my anecdote" → paste your anecdote and ask to weave it in
- "Wrong hashtags" → specify which hashtags to use

**Tip**: Read each post out loud. If it doesn't sound like you, it needs revision.

---

### Stage 5: Benchmark Review (3 minutes)
*Skill 6 — Quality Reviewer + HITL 6a*

You'll see a scorecard like this:

| Post | Action | Voice | Depth | Cohesion | LinkedIn | Avg |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Week 1 | 4 | 5 | 4 | 5 | 5 | **4.6** |
| Week 2 | 4 | 5 | 5 | 5 | 5 | **4.8** |
...

**What to look for**:
- Any score below 3.0 → that post needs revision (mandatory flag)
- Low Voice Consistency → re-invoke Skill 4
- Low Actionability → Week 4 or 6 are usually the fix
- Low Narrative Cohesion → check Week 5 or 6 (they're often where arc breaks down)

Say "approved" to proceed or request specific revisions.

---

### Stage 6: Archive + Publish
*Skills 7 and 8*

**Archiving (automatic)**:
Your full session is saved to `archive/[Topic]_[Date].md` and `.pdf`. This includes the intent document, roadmap, all 6 posts, and benchmark scores.

**Publishing**:

You'll be asked: *Option A (manual) or Option B (automated)?*

**Option A — Manual (Recommended for first-timers)**:
1. Copy each post's text from the archive file
2. Go to linkedin.com → Start a post → Paste
3. Open the corresponding `diagrams/weekX_*.html` in your browser
4. Screenshot it (Windows: Win+Shift+S) and attach to the post
5. Post

**Option B — Automated (if MCP is configured)**:
The system will call `linkedin_create_post` directly. See Setup section for MCP configuration.

---

## Part 3: Using the Visual Diagrams

Each post has a corresponding HTML visual in `diagrams/`. Open in any browser and screenshot for LinkedIn.

| Week | File | What It Shows |
|------|------|--------------|
| 1 | `week1_ai_usage_gap.html` | Split-screen Level 1 vs Level 3 |
| 2 | `week2_ai_maturity_ladder.html` | 3-step maturity ladder with stats |
| 3 | `week3_testing_before_after.html` | Before/after process flow |
| 4 | `week4_five_moves.html` | 5-step action list |
| 5 | `week5_2024_vs_2027.html` | 4-dimension comparison table |
| 6 | `week6_series_journey.html` | Full 6-week journey map |

**To screenshot on Windows**: Win+Shift+S → select the browser window → save as PNG.

**LinkedIn image tip**: These are 1080x1080 optimized. Post as a single image attachment for best results.

---

## Part 4: Customising for a New Topic

You can reuse this system for any 6-week series. What changes each time:
- Your answers to the 5 interview questions
- The topic-specific roadmap (generated fresh each time)
- The posts and visuals (generated from scratch)

What stays the same:
- All 9 skill files (no editing needed)
- The narrative arc structure (Hook → Framework → Story → Tactics → Vision → Call)
- The benchmark rubric (frozen for consistency)

**Best topics for this system**:
- Topics where you have genuine personal experience (the anecdote is the strongest element)
- Audiences who are Manager/Director level (voice refiner is optimized for this level)
- Topics with concrete, actionable advice for Week 4

**Topics that need extra attention**:
- Highly technical niche topics (voice refiner may over-simplify — request more technical language in HITL 5a)
- Visionary/trend topics (Week 5 is the consistently weak spot — add specific examples)

---

## Part 5: LinkedIn MCP Setup (Optional)

For automated posting, configure the LinkedIn MCP server.

### One-Time Setup

**Step 1: Install the package**
```bash
npm install -g @ldraney/mcp-linkedin
```

**Step 2: Create a LinkedIn Developer App**
1. Go to https://www.linkedin.com/developers/apps/new
2. Create an app, request "Share on LinkedIn" product
3. Add redirect URI: `http://localhost:3000/callback`
4. Copy Client ID and Client Secret

**Step 3: Run OAuth to get your access token**

Start a local server to capture the OAuth callback:
```javascript
// Save as oauth_server.js and run: node oauth_server.js
const http = require('http');
const url = require('url');
const fs = require('fs');
http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);
  if (parsed.query.code) {
    fs.writeFileSync('auth_code.txt', parsed.query.code);
    res.end('<h1>Success! Close this tab.</h1>');
  } else { res.end('Waiting...'); }
}).listen(3000);
```

Visit this URL in your browser (replace YOUR_CLIENT_ID):
```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid+profile+w_member_social
```

Exchange the code for a token:
```javascript
const https = require('https');
const qs = require('querystring');
const body = qs.stringify({
  grant_type: 'authorization_code',
  code: 'YOUR_AUTH_CODE',
  redirect_uri: 'http://localhost:3000/callback',
  client_id: 'YOUR_CLIENT_ID',
  client_secret: 'YOUR_CLIENT_SECRET'
});
// POST to https://www.linkedin.com/oauth/v2/accessToken
// Response includes access_token and id_token (contains person ID in 'sub' field)
```

**Step 4: Add to Claude Code settings**

Edit `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "linkedin": {
      "command": "C:\\Users\\USERNAME\\AppData\\Roaming\\npm\\mcp-linkedin.cmd",
      "args": [],
      "env": {
        "LINKEDIN_CLIENT_ID": "your_client_id",
        "LINKEDIN_CLIENT_SECRET": "your_client_secret",
        "LINKEDIN_REDIRECT_URI": "http://localhost:3000/callback",
        "LINKEDIN_API_VERSION": "202510",
        "LINKEDIN_ACCESS_TOKEN": "your_access_token",
        "LINKEDIN_PERSON_ID": "your_person_id"
      }
    }
  }
}
```

**Step 5: Restart Claude Code** — MCP server loads on startup.

**Token renewal**: Tokens expire after 60 days. Re-run OAuth when expired.

---

## Part 6: Troubleshooting

### "The post sounds like AI"
Re-invoke Skill 4 with explicit feedback:
> "Re-run Skill 4 on Week 2. The phrase 'navigating the complex landscape' is an AI pattern. Replace it with a specific example. The tone should be more direct — less corporate."

### "Week 5 is weak"
Week 5 (Vision) is the consistently weak spot. At HITL 5a, revise it with:
> "Week 5 — Revise: Add 2 specific predictions with evidence. Include one counter-intuitive insight. Start with 'By 2027...' and ground it in current trends the audience already sees."

### "The roadmap doesn't fit my topic"
After Skill 2, request adjustments:
> "Week 3 should focus on [specific subtopic]. Week 5 should emphasize [specific future trend] rather than general AI adoption."

### "The MCP server isn't loading"
Use the direct API instead (Option B2). This works without MCP:
```javascript
// Post directly via LinkedIn API — see Skill 8 for full Node.js snippet
// Status 201 = success. Response includes post URN for your publishing log.
```

### "I want to change the tone mid-series"
Consistent tone across all 6 posts is important for Voice Consistency scores. If you must change tone, change it before Stage 3 (before drafts are generated). After drafts exist, changing tone requires re-running Skills 3-5 for affected posts.

### "The archive isn't generating a PDF"
Install `md-to-pdf` globally:
```bash
npm install -g md-to-pdf
md-to-pdf archive/your_file.md
```
If npm is unavailable, open the `.md` file in VS Code and use "Markdown: Open Preview" → right-click → Print → Save as PDF.

---

## Part 7: Publishing Schedule

Recommended cadence for the 6-week series:

| Week | Timing | Best Days | Best Time |
|------|--------|-----------|-----------|
| 1 | Week 0 | Tuesday | 8-10am local |
| 2 | +7 days | Thursday | 8-10am local |
| 3 | +14 days | Tuesday | 8-10am local |
| 4 | +21 days | Thursday | 8-10am local |
| 5 | +28 days | Tuesday | 8-10am local |
| 6 | +35 days | Thursday | 8-10am local |

After each post, track impressions, reactions, and comments at 24 and 48 hours. This engagement data will tell you which weeks of the arc resonate most with your audience.

---

## Part 8: What to Do After the Series

1. **Review engagement metrics** — Compare Week 1-6 performance. Which arc position (Hook, Tactics, Story) performed best?
2. **Update your archive** — Add actual engagement metrics to the archive file for future reference
3. **Plan the next series** — Use `outputs/2026_Roadmap_Plan.md` as a quarterly planning template
4. **Improve the system** — If Week 5 consistently underperformed, update Skill 3's Week 5 drafting instructions before the next run

---

*Questions? See the README or open an issue at: https://github.com/taashim-eng/linkedin-thought-leadership-agent/issues*
