# Advanced Usage (Your Tool of Choice)

This page is about taking your agent tool to the next level: reusable prompts, persistent instructions, and "background" execution.

If you are not comfortable yet with the basics (plan -> do -> verify, diffs, sanity checks), do that first:

- [Workflows](workflows.md)
- [Verification and Rigor](verification.md)

## The big unlocks

Across most agent tools, these are the high-leverage features for scientists:

1. **Persistent instructions** (project rules, memory) - tell the agent your conventions once
2. **Reusable prompts** (slash commands, skills, prompt files) - encode your lab's workflows
3. **Background mode** (async tasks, non-interactive runs) - start a task and come back later

## Persistent instructions: tell it once

Instead of repeating "do not change scientific assumptions" every session, you can store instructions that load automatically.

Most tools support a project-level file (like `CLAUDE.md` or `AGENTS.md`) where you write:

- coding conventions
- verification requirements
- "always do X before Y" rules
- project-specific context

This is the single highest-leverage feature. Start here.

## Reusable prompts: stop retyping yourself

Good reusable prompts encode your lab's defaults:

- "Propose a plan first"
- "Do not change scientific assumptions without asking"
- "Run verification"
- "Summarize the diff"

Most tools let you save these as slash commands (like `/review` or `/deploy`) that you can invoke instead of typing the full prompt each time.

## Background mode: delegate and come back

Different tools implement this differently:

- cloud tasks you can start and review later
- non-interactive CLI runs in CI
- agents that open PRs for review

The rule is the same: do not trust results until you review diffs and run checks.

## Official docs to go deeper

### Claude Code

Claude Code is the default tool in this guide.

**Start here:**

- [Memory](https://code.claude.com/docs/en/memory.md) (CLAUDE.md - persistent project instructions)
- [Skills](https://code.claude.com/docs/en/skills.md) (custom slash commands / reusable prompts)
- [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web.md) (background/async tasks)
- [Cost management](https://code.claude.com/docs/en/costs.md)

**Reference:**

- [Extend overview](https://code.claude.com/docs/en/features-overview.md) (full feature summary)
- [CLI reference](https://code.claude.com/docs/en/cli-reference.md)
- [Settings](https://code.claude.com/docs/en/settings.md)
- [Sandboxing](https://code.claude.com/docs/en/sandboxing.md)

**For developers:**

- [Hooks guide](https://code.claude.com/docs/en/hooks-guide.md) (automate workflows with scripts)
- [Subagents](https://code.claude.com/docs/en/sub-agents.md) (spawn specialized workers)
- [Headless mode](https://code.claude.com/docs/en/headless.md) (run programmatically)

### OpenAI Codex

If you already pay for a ChatGPT plan, Codex can be a great way to get an agentic workflow without adding another subscription.

- [Codex overview](https://developers.openai.com/codex/)
- [Codex CLI overview](https://developers.openai.com/codex/cli)
- [Codex CLI reference](https://developers.openai.com/codex/cli/reference) (flags/options)
- [Codex CLI slash commands](https://developers.openai.com/codex/cli/slash-commands) (reusable prompts)
- [Rules](https://developers.openai.com/codex/rules) (persistent project instructions)
- [AGENTS.md](https://developers.openai.com/codex/guides/agents-md) (agent coordination patterns)
- [Skills](https://developers.openai.com/codex/skills) (create reusable skills)
- [Codex CLI repo](https://github.com/openai/codex) (install instructions and releases)

### GitHub Copilot

Copilot has a large docs set. These are the most relevant advanced topics:

- [Main docs index](https://docs.github.com/en/copilot)
- [Custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) (personal/repo/org)
- [Prompt files](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file) (reusable prompts/templates)
- [Agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks) (for Copilot coding agent)
- [MCP](https://docs.github.com/en/copilot/concepts/context/mcp)

### Cursor

Cursor moves quickly and its docs are the best source of truth:

- [Docs](https://cursor.com/docs)
- [Pricing](https://cursor.com/pricing) (to understand "background agents" and plan limits)

## A scientist-friendly way to use advanced features

If you want to adopt one advanced feature at a time, do it in this order:

1. **Persistent instructions** - set up a project rules file with your conventions
2. **Reusable prompts** - save your top 3 workflows as slash commands
3. **Background tasks** - learn to start longer tasks and review them later
4. **Tool integrations (MCP)** - connect to databases, Slack, or other services if needed

Each step should make your work more reproducible and less error-prone.

## For developers: hooks

If you have software engineering experience, hooks let you run scripts automatically when specific events happen (file edits, before commits, etc.). They're powerful for enforcing guardrails like:

- auto-format code on file edits
- block secrets from being committed
- require tests to pass before marking done

Most scientists can skip this feature initially. The verification habits in this guide give you the same safety without writing code.

## See also

- [MCP & Connectors](mcp.md)
- [Scaling Up Your Usage](scaling-up.md)
- [Cost Control](cost-control.md)
