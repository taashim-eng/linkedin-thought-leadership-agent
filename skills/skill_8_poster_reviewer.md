---
name: poster-reviewer-ligo-mcp
description: Handles LinkedIn publishing via the LiGo MCP (LinkedIn MCP Runner). Supports writing, editing, scheduling, and post-publication verification. Requires MCP server configuration.
---

# Skill 8: Poster & Reviewer (LiGo MCP Integration)

## Overview
Automates the final step: publishing approved content to LinkedIn. Uses the **LiGo MCP** (LinkedIn MCP Runner) server to post, edit, and verify content directly on the platform.

**This skill is optional** — users can always copy/paste the approved posts manually. The MCP integration adds convenience and scheduling capabilities.

## Prerequisites
- **LiGo MCP Server**: Must be configured and running. See [MCP Setup](#mcp-setup) below.
- **LinkedIn Authentication**: Handled securely through LiGo's OAuth flow.

## Inputs
- **Final Approved Post(s)**: Output from Skill 6/7 (one or more posts to publish).
- **Schedule** (optional): Preferred posting date/time for each post.

## Outputs
- **Live Post URL**: Direct link to the published LinkedIn post.
- **Publication Confirmation**: Status of each post (published, scheduled, or failed).

## Workflow

### Step 1: Initialize MCP Connection
- Connect to the LiGo MCP server.
- Verify authentication status.
- If not authenticated, guide the user through LiGo's OAuth flow.

### Step 2: Prepare Post
- Use LiGo's `edit_post` tool to format the content for LinkedIn's API.
- Attach visual/image if provided.
- Preview the formatted post for user confirmation.

### Step 3: Publish or Schedule
- **Immediate**: Use `write_post` to publish now.
- **Scheduled**: Use `schedule_post` to queue for a future date/time.
- Always confirm with the user before executing: "Ready to publish Week [X] to LinkedIn. Proceed?"

### Step 4: Post-Publication Verification
- Use LiGo's feedback loop to verify the post is live.
- Check for formatting issues (broken links, truncated text, missing images).
- Return the live URL to the user.

## MCP Setup

Add to your Claude Code `settings.json` or Claude Desktop `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ligo-linkedin": {
      "command": "npx",
      "args": ["-y", "@anthropic/ligo-mcp-server"],
      "env": {
        "LINKEDIN_CLIENT_ID": "<your-client-id>",
        "LINKEDIN_CLIENT_SECRET": "<your-client-secret>"
      }
    }
  }
}
```

*Note: Exact package name and configuration may vary. Consult the LiGo MCP documentation for the latest setup instructions.*

## Constraints
- **Security**: Never store credentials in skill files, archive files, or git repos.
- **User Confirmation**: ALWAYS confirm before publishing — no automatic posting.
- **Rate Limits**: LinkedIn has API rate limits. Space posts appropriately (recommended: 1 per week).

## Failure Modes
- **MCP server not running**: Inform user and offer manual copy/paste as fallback.
- **Authentication expired**: Guide user through re-authentication.
- **API error**: Log the error, inform the user, and suggest retrying or posting manually.
- **LinkedIn formatting issues**: If the post looks wrong after publishing, use `edit_post` to fix.

## Example
```
User: "Publish Week 1 to LinkedIn."
Skill 8: "Connecting to LiGo MCP... Authenticated as [user].
Here's a preview of the post. Ready to publish? (yes/no)"
User: "yes"
Skill 8: "Published! Live at: https://linkedin.com/posts/...
Verified: formatting OK, no truncation. Post is live."
```
