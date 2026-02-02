# MCP and Connectors

MCP (Model Context Protocol) is a way for agentic tools to connect to external services and data sources. Instead of copy-pasting information into the agent, you can give it direct access to your databases, documents, and tools.

This is powerful—and risky. This page covers what MCP can do, when to use it, and how to stay safe.

## What MCP enables

With MCP connectors, an agent can:

### Access your documents
- Read files from Google Drive
- Search your Notion workspace
- Pull pages from Confluence
- Access shared lab documentation

### Work with project management
- Read and create GitHub issues
- Update Jira tickets
- Check Linear tasks
- Post to Slack channels

### Query data sources
- Run SQL queries against databases
- Search internal knowledge bases
- Access APIs you've set up
- Pull from data warehouses

### Control tools
- Run commands on remote servers
- Interact with lab equipment (if APIs exist)
- Trigger CI/CD pipelines
- Manage cloud resources

## Why scientists should care

The biggest productivity gains come from connecting AI to your actual working context.

### Your documentation becomes accessible

Instead of:
- "Let me explain our data format..."
- [paste 500 lines of documentation]

You can say:
- "Read our data format docs and process this file accordingly"

The agent pulls the docs itself.

### Your protocols are always available

Lab protocols, standard operating procedures, analysis guidelines—all accessible without copy-pasting.

### Your project context is persistent

The agent can see your GitHub issues, your shared notes, your experiment logs. It understands the context of what you're working on.

## The risk: bigger blast radius

More access means more potential for damage.

### What can go wrong

- Agent reads confidential documents it shouldn't
- Agent modifies data in a database (if write access is enabled)
- Agent posts to public channels accidentally
- Credentials are exposed through the connection
- Agent takes actions you didn't intend

### The principle: least privilege

Give the agent the minimum access it needs, not everything it could possibly use.

**Bad:** "Connect to our entire Google Drive"

**Good:** "Connect to the lab-protocols folder, read-only"

## Getting started safely

### Start with read-only access

Most MCP connections can be configured as read-only. Start there.

- ✅ Read GitHub issues
- ❌ Create or close GitHub issues (not yet)

Once you trust the setup, you can expand permissions incrementally.

### Start with non-sensitive data

Connect to:
- Public documentation
- Open-source code
- General reference materials

Don't connect to:
- Patient data systems
- Financial databases
- Anything covered by compliance requirements

### Log what the agent does

Enable logging for MCP connections so you can audit:
- What did it read?
- What did it modify?
- When did access happen?

## Common MCP setups for scientists

### GitHub integration

Connect the agent to your lab's GitHub organization:

**Use cases:**
- "What issues are assigned to me?"
- "Create an issue for this bug I found"
- "What's the status of PR #123?"

**Permissions to consider:**
- Read issues: low risk
- Create issues: medium risk (might spam)
- Merge PRs: high risk (don't enable without review)

### Documentation access

Connect to your docs system (Notion, Confluence, Google Drive):

**Use cases:**
- "Follow our style guide for this code"
- "What does our protocol say about data normalization?"
- "Find the onboarding doc for new lab members"

**Permissions to consider:**
- Read docs: low risk
- Edit docs: medium risk (agent might make changes)
- Delete: high risk (don't enable)

### Database access

Connect to your lab's database:

**Use cases:**
- "How many samples from experiment X are in the database?"
- "Query the results table for entries matching Y"
- "Generate a summary of data collected last month"

**Permissions to consider:**
- Read/SELECT: low-medium risk
- Write/INSERT: medium risk
- Modify/UPDATE/DELETE: high risk (be very careful)

## Setting up MCP connections

The exact setup depends on your tool. Here's the general pattern:

### For Claude Code

MCP servers are configured in your settings:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```

See [Claude Code MCP docs](https://code.claude.com/docs/en/mcp) for details.

### For other tools

- **Cursor:** Check Settings → MCP
- **Codex CLI:** See Codex documentation for connector setup
- **Copilot:** Uses its own extension system

## Security best practices

### Use separate credentials

Don't use your personal credentials for MCP connections. Create service accounts with limited permissions.

### Review permissions regularly

Audit what's connected and what access it has:

```bash
# In Claude Code
/mcp  # Shows connected servers and their status
```

Remove connections you're not actively using.

### Don't connect sensitive systems

Some things should never be connected to external AI tools:

- Systems with patient/clinical data
- Financial systems
- HR databases
- Anything with credentials or secrets
- Compliance-regulated data stores

### Test in a sandbox first

Before connecting to production systems:

1. Set up a test/staging version
2. Connect the agent to the test version
3. Verify it behaves as expected
4. Then (carefully) connect to production

## When MCP is worth the complexity

MCP adds setup complexity. It's worth it when:

- You repeatedly need the same external context
- Copy-pasting documentation is eating your time
- You want the agent to stay up-to-date with changes
- The data source is frequently updated

It's not worth it for:

- One-time tasks
- Small projects where copy-paste is fine
- Situations where security concerns outweigh convenience

## A cautious rollout

1. **Week 1:** Read-only access to non-sensitive docs
2. **Week 2:** Add GitHub issue reading
3. **Week 3:** Evaluate. Is it useful? Any problems?
4. **Week 4+:** Incrementally add more connections

Go slow. It's easy to add access, harder to undo damage.

## See also

- [Advanced Usage](advanced-usage.md)
- [Safety, Privacy, and Policy](safety-privacy.md)
- [Lab Rollout](lab-rollout.md)
