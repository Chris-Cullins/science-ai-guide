# Claude Code (Recommended)

Claude Code is an agentic coding tool that runs in your terminal and can edit files, run commands, and iterate.

## What you need

- A Claude subscription (Pro/Max/Team/Enterprise) or a Claude Console account

Notes:

- If you are just getting started, Pro is often enough.
- If you use it heavily (long sessions, large repos), you may need a higher tier.
- Pricing changes; verify here: https://www.anthropic.com/pricing

Official docs:
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)

## Install

From the official instructions:

macOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

Windows CMD

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Windows (WinGet)

```powershell
winget install Anthropic.ClaudeCode
```

macOS (Homebrew)

```bash
brew install --cask claude-code
```

Then:

```bash
cd your-project
claude
```

If you're prompted to log in on first use, follow the browser flow.

## How scientists should use it (default guardrails)

- Start with a throwaway repo or a copy of your project.
- Tell it to propose a plan before editing.
- Require it to run tests / a minimal validation script.
- Review diffs for every change.

## The 30-minute starter task

Pick one:

- "Add a `Makefile` (or `justfile`) that runs `pytest`, `ruff`, and a quick smoke test."
- "Turn my one-off analysis script into a reproducible pipeline with a config file and pinned dependencies."
- "Write a small CLI that loads my CSV and produces the exact plot I need for Figure 2."
