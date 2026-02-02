# Advanced Usage (Your Tool of Choice)

This page is about taking your agent tool to the next level: reusable prompts, persistent instructions, automation hooks, and "background" execution.

If you are not comfortable yet with the basics (plan -> do -> verify, diffs, sanity checks), do that first:

- [Workflows](workflows.md)
- [Verification and Rigor](verification.md)

## The big unlocks

Across most agent tools, these are the high-leverage features:

1. Reusable prompts (slash commands, skills, prompt files)
2. Persistent instructions (project rules, memory)
3. Hooks (automate checks, formatting, guardrails)
4. Background mode (async tasks, non-interactive runs, PR-based agents)
5. Tool integrations (MCP, GitHub/Slack/Linear)

## Reusable prompts: stop retyping yourself

Good reusable prompts encode your lab's defaults:

- "Propose a plan first"
- "Do not change scientific assumptions without asking"
- "Run verification"
- "Summarize the diff"

## Hooks: make correctness automatic

Hooks are the "seatbelts" for autonomy.

Common good hooks:

- auto-format code on file edits
- block secrets from being committed
- require tests to run before marking a task done
- warn when the agent tries risky commands

## Background mode: delegate and come back

Different tools implement this differently:

- cloud tasks you can start and review later
- non-interactive CLI runs in CI
- agents that open PRs for review

The rule is the same: do not trust results until you review diffs and run checks.

## Official docs to go deeper

### Claude Code

Claude Code is the default tool in this guide. These links cover the advanced features you asked about (skills, hooks, subagents, background execution, etc.).

- Extend overview (CLAUDE.md, Skills, subagents, hooks, MCP, plugins):
  https://code.claude.com/docs/en/features-overview.md
- Skills (custom slash commands / reusable prompts):
  https://code.claude.com/docs/en/skills.md
- Hooks guide (how to automate workflows with hooks):
  https://code.claude.com/docs/en/hooks-guide.md
- Hooks reference (events and schemas):
  https://code.claude.com/docs/en/hooks.md
- Subagents (specialized agents for task-specific workflows):
  https://code.claude.com/docs/en/sub-agents.md
- Memory (project and user memory, persistence across sessions):
  https://code.claude.com/docs/en/memory.md
- Run Claude Code programmatically / headless mode:
  https://code.claude.com/docs/en/headless.md
- Claude Code on the web (async tasks):
  https://code.claude.com/docs/en/claude-code-on-the-web.md
- CLI reference:
  https://code.claude.com/docs/en/cli-reference.md
- Settings:
  https://code.claude.com/docs/en/settings.md
- Cost management:
  https://code.claude.com/docs/en/costs.md
- Sandboxing:
  https://code.claude.com/docs/en/sandboxing.md

### OpenAI Codex

If you already pay for a ChatGPT plan, Codex can be a great way to get an agentic workflow without adding another subscription.

- Codex overview:
  https://developers.openai.com/codex/
- Codex CLI overview:
  https://developers.openai.com/codex/cli
- Codex CLI reference (flags/options):
  https://developers.openai.com/codex/cli/reference
- Codex CLI slash commands (reusable prompts):
  https://developers.openai.com/codex/cli/slash-commands
- Rules (persistent project instructions):
  https://developers.openai.com/codex/rules
- AGENTS.md (agent coordination patterns):
  https://developers.openai.com/codex/guides/agents-md
- Skills (create reusable skills):
  https://developers.openai.com/codex/skills

Codex CLI repo (install instructions and releases):

- https://github.com/openai/codex

### GitHub Copilot

Copilot has a large docs set. These are the most relevant advanced topics:

- Main docs index:
  https://docs.github.com/en/copilot
- Custom instructions (personal/repo/org):
  https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- Prompt files (reusable prompts/templates):
  https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
- Agent skills:
  https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- Hooks (for Copilot coding agent):
  https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks
- MCP:
  https://docs.github.com/en/copilot/concepts/context/mcp

### Cursor

Cursor moves quickly and its docs are the best source of truth:

- Docs:
  https://cursor.com/docs
- Pricing (to understand "background agents" and plan limits):
  https://cursor.com/pricing

## A scientist-friendly way to use advanced features

If you want to adopt one advanced feature at a time, do it in this order:

1. Persistent instructions (project rules)
2. Reusable prompts for your top 3 workflows
3. Hooks for tests / formatting / safety
4. Background tasks
5. Tool integrations (MCP)

Each step should make your work more reproducible and less error-prone.
