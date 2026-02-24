---
name: poster-reviewer
description: Handles LinkedIn publishing via manual or automated options.
---

# Skill 8: Poster & Reviewer

## Overview

Handles the final step: publishing approved posts to LinkedIn.

Always present two options:

- **Option A**: Manual posting (simpler, always works).
- **Option B**: Automated posting via MCP or API (faster at scale).

The user chooses based on setup.

## Inputs

- **Final approved post(s)**: Output from Skill 6/7.
- **Schedule** (optional): Preferred posting date/time per post.

## Outputs

- **Published post**: Live on LinkedIn with confirmed URL/URN.
- **Publication log**: Status of each post (published, scheduled, failed).

## Workflow

### Step 1: Present both options

Before posting, present this choice:

```text
Ready to publish Week [X]: "[Post Title]"

How would you like to post?

OPTION A — Manual (Recommended)
  Simple. Always works. No setup required.
  1. Copy the post text below
  2. Go to linkedin.com → Start a post → Paste → Post
  3. Optionally attach the visual:
     open diagrams/weekX_*.html in browser → screenshot
  ✓ Best for: one-off posts, first-time users, troubleshooting

OPTION B — Automated (MCP or API)
  Faster. Good for bulk posting. Requires prior setup.
  - Option B1: LinkedIn MCP server (if configured in settings.json)
  - Option B2: Direct LinkedIn API call via Node.js
  ✓ Best for: posting multiple weeks, scheduled publishing

Which do you prefer? (A / B1 / B2)
```

### Option A: Manual posting

1. **Copy post text** and present it in a clean block.
2. **Attach visual**:

   - Open `diagrams/weekX_*.html` in a browser.
   - Screenshot the full page.
   - Save as PNG and attach to the post.

3. **Post on LinkedIn**:

   - Go to `linkedin.com`.
   - Click **Start a post**.
   - Paste text, attach screenshot, click **Post**.

4. **Confirm**: Ask user to share post URL or confirm it is live.

### Option B1: LinkedIn MCP server

Prerequisites:

- MCP server configured in `~/.claude/settings.json`.
- Claude Code restarted.

Setup (one-time):

```json
{
  "mcpServers": {
    "linkedin": {
      "command": "mcp-linkedin",
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

Install:

```bash
npm install -g @ldraney/mcp-linkedin
```

OAuth flow (one-time):

1. Start local callback server:

```javascript
const http = require('http');
http
  .createServer((req, res) => {
    console.log(req.url);
    res.end('OK');
  })
  .listen(3000);
```

2. Generate auth URL and visit in browser.
3. Copy code from redirect URL.
4. Exchange code for token via Node.js or `linkedin_exchange_code` MCP tool.

Usage after setup/restart:

```text
Call linkedin_create_post({
  commentary: "[post text]",
  visibility: "PUBLIC"
})
```

Troubleshooting:

If MCP tools do not appear after restart, fall back to Option B2.

### Option B2: Direct LinkedIn API

Prerequisites:

- Valid access token.
- Valid person ID.

Post via Node.js:

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
    Authorization: 'Bearer <ACCESS_TOKEN>',
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body),
    'X-Restli-Protocol-Version': '2.0.0',
    'LinkedIn-Version': '202510'
  }
};

// Status 201 = success. Response includes post URN.
```

Save returned URN (for example
`urn:li:share:7430329696413843458`) in the publishing log.

### Step 2: Post-publication verification

After posting (any method):

- Confirm post visibility on LinkedIn.
- Check formatting (line breaks and hashtags).
- Log post URN/URL in `CLAUDE.md` publishing log.
- Ask user to attach the visual if missing.

## OAuth setup reference

1. Create a LinkedIn Developer App:
   <https://www.linkedin.com/developers/apps>
2. Request **Share on LinkedIn** product (`w_member_social`).
3. Add redirect URI: `<http://localhost:3000/callback>`.
4. Run OAuth flow to get `LINKEDIN_ACCESS_TOKEN` and `LINKEDIN_PERSON_ID`.
5. Store values in local `settings.json` env vars.

Token lifespan is usually 60 days.
Use `linkedin_refresh_token` or re-run OAuth when expired.

## Constraints

- **Security**:
  Never store credentials in skill files, archive files, or git repos.
  Use environment variables only.
- **User confirmation**:
  Always confirm before publishing.
  Do not auto-publish.
- **Rate limits**:
  LinkedIn limits posting frequency.
  Space posts at least one per day.
  Weekly cadence is recommended for thought leadership.
- **Option A is always valid**:
  If automation fails, fall back to manual immediately.

## Failure Modes

- **MCP tools not loading**:
  Fall back to Option B2 or Option A.
- **API 401**:
  Access token expired; re-run OAuth.
- **API 403**:
  Missing `w_member_social` scope; re-authorize.
- **Formatting issues on LinkedIn**:
  Line breaks may collapse.
  Preview before posting and keep blank lines between paragraphs.
