---
name: poster-reviewer
description: Handles LinkedIn publishing via two options: (A) manual copy/paste (recommended for reliability) or (B) automated posting via the LinkedIn MCP server or direct API call. Always presents both options to the user.
---

# Skill 8: Poster & Reviewer

## Overview
Handles the final step: publishing approved posts to LinkedIn. **Always presents two options** to the user — manual posting (simpler, always works) or automated posting via MCP/API (faster at scale, requires setup). The user chooses based on their setup.

## Inputs
- **Final Approved Post(s)**: Output from Skill 6/7 (one or more posts to publish).
- **Schedule** (optional): Preferred posting date/time for each post.

## Outputs
- **Published Post**: Live on LinkedIn with confirmed URL/URN.
- **Publication Log**: Status of each post (published, scheduled, or failed).

---

## Workflow

### Step 1: Always Present Both Options

Before doing anything, present the user with this choice:

```
Ready to publish Week [X]: "[Post Title]"

How would you like to post?

OPTION A — Manual (Recommended)
  Simple. Always works. No setup required.
  1. Copy the post text below
  2. Go to linkedin.com → Start a post → Paste → Post
  3. Optionally attach the visual (open diagrams/weekX_*.html in browser → screenshot)
  ✓ Best for: one-off posts, first-time users, troubleshooting

OPTION B — Automated (MCP or API)
  Faster. Good for bulk posting. Requires prior setup.
  - Option B1: LinkedIn MCP server (if configured in settings.json)
  - Option B2: Direct LinkedIn API call via Node.js
  ✓ Best for: posting multiple weeks, scheduled publishing

Which do you prefer? (A / B1 / B2)
```

---

### Option A: Manual Posting (Recommended)

1. **Copy the post text** — present it in a clean, copy-ready block.
2. **Attach the visual**:
   - Open `diagrams/weekX_*.html` in a browser
   - Screenshot the full page (Windows: Win+Shift+S)
   - Save as PNG and attach when composing the post
3. **Post on LinkedIn**:
   - Go to linkedin.com → click "Start a post"
   - Paste text → attach screenshot → click "Post"
4. **Confirm**: Ask user to paste the post URL or confirm it's live.

---

### Option B1: LinkedIn MCP Server

**Prerequisites**: MCP server must be configured in `~/.claude/settings.json` and Claude Code restarted.

**Setup** (one-time):
```json
{
  "mcpServers": {
    "linkedin": {
      "command": "C:\\Users\\<username>\\AppData\\Roaming\\npm\\mcp-linkedin.cmd",
      "args": [],
      "env": {
        "LINKEDIN_CLIENT_ID": "<your-client-id>",
        "LINKEDIN_CLIENT_SECRET": "<your-client-secret>",
        "LINKEDIN_REDIRECT_URI": "http://localhost:3000/callback",
        "LINKEDIN_API_VERSION": "202510",
        "LINKEDIN_ACCESS_TOKEN": "<your-access-token>",
        "LINKEDIN_PERSON_ID": "<your-person-id>"
      }
    }
  }
}
```

**Install**: `npm install -g @ldraney/mcp-linkedin`

**OAuth flow** (one-time to get access token + person ID):
1. Start local callback server: `node -e "require('http').createServer((req,res)=>{console.log(req.url);res.end('OK')}).listen(3000)"`
2. Generate auth URL and visit in browser
3. Copy code from redirect URL
4. Exchange code for token via Node.js or `linkedin_exchange_code` MCP tool

**Usage** (after setup + restart):
```
Call linkedin_create_post({
  commentary: "[post text]",
  visibility: "PUBLIC"
})
```

**Troubleshooting**: If MCP tools don't appear after restart, fall back to Option B2.

---

### Option B2: Direct LinkedIn API (No MCP Required)

**Prerequisites**: Valid access token and person ID (from OAuth flow above).

**Post via Node.js**:
```javascript
const https = require('https');
const body = JSON.stringify({
  author: 'urn:li:person:<PERSON_ID>',
  lifecycleState: 'PUBLISHED',
  specificContent: {
    'com.linkedin.ugc.ShareContent': {
      shareCommentary: { text: '<POST_TEXT>' },
      shareMediaCategory: 'NONE'
    }
  },
  visibility: {
    'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
  }
});

const options = {
  hostname: 'api.linkedin.com',
  path: '/v2/ugcPosts',
  method: 'POST',
  headers: {
    'Authorization': 'Bearer <ACCESS_TOKEN>',
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body),
    'X-Restli-Protocol-Version': '2.0.0',
    'LinkedIn-Version': '202510'
  }
};
// Status 201 = success. Response includes post URN.
```

Save the returned URN (e.g., `urn:li:share:7430329696413843458`) to the publishing log.

---

### Step 2: Post-Publication Verification

After posting (any method):
- Confirm the post is visible on LinkedIn
- Check for formatting issues (line breaks, hashtags rendering correctly)
- Log the post URN/URL in `CLAUDE.md` publishing log
- Ask user to add the visual if not already attached

---

## OAuth Setup Reference (Getting Access Token)

1. Create a LinkedIn Developer App at https://www.linkedin.com/developers/apps
2. Request the **"Share on LinkedIn"** product (for `w_member_social` scope)
3. Add redirect URI: `http://localhost:3000/callback`
4. Run the OAuth flow to get `LINKEDIN_ACCESS_TOKEN` and `LINKEDIN_PERSON_ID`
5. Store in `settings.json` env vars — **never commit to git**

Token lifespan: **60 days**. Use `linkedin_refresh_token` or re-run OAuth when expired.

---

## Constraints
- **Security**: Never store credentials in skill files, archive files, or git repos. Use env vars only.
- **User Confirmation**: ALWAYS confirm before publishing — no automatic posting.
- **Rate Limits**: LinkedIn limits posting frequency. Space posts at least 1 per day; recommended 1 per week for thought leadership.
- **Option A is always valid**: If automated posting fails for any reason, fall back to manual immediately.

## Failure Modes
- **MCP tools not loading**: Fall back to Option B2 (direct API) or Option A (manual).
- **API 401 error**: Access token expired — re-run OAuth flow.
- **API 403 error**: Missing `w_member_social` scope — re-authorize with correct scope.
- **Formatting issues on LinkedIn**: Line breaks may collapse — preview before posting. Use blank lines between paragraphs.
