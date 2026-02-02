# Oh I Get It (Guided Tour)

This is a deliberately "aha"-style experience.

You will use an agentic tool to download this guide onto your computer, then have the agent walk you through it interactively.

This guide uses Claude Code as the default tool, but you do not have to use Claude Code. Use whatever tool you already have and like.

See: [Pick Your Tools](tooling.md)

Note: if there is something in this guide you do not understand, ask your tool of choice to explain it. That is one of the best ways to learn fast.

## What you will do

1. Install your agent tool
2. Start it in a fresh folder
3. Paste a single prompt
4. Let the agent:
   - download the guide (from GitHub)
   - open the docs locally
   - propose a fast learning path
   - answer questions as you go

## Safety note

The prompt below asks the agent to run shell commands (`curl`, `tar`, etc.).

If you do not recognize a command, ask it to explain before you approve it.

## Step 1: Install an agent tool

Default path in this guide:

- [Claude Code](claude-code.md)

If you already pay for ChatGPT, you can do a very similar experience with [OpenAI Codex CLI](https://github.com/openai/codex) (a terminal-based coding agent).

## Step 2: Start your agent tool

Open a terminal: [Open a Terminal](open-terminal.md)

Then run:

```bash
mkdir -p ~/agentic-ai-guide-tour
cd ~/agentic-ai-guide-tour
claude
```

If you are using Codex CLI instead:

```bash
mkdir -p ~/agentic-ai-guide-tour
cd ~/agentic-ai-guide-tour
codex
```

## Step 3: Paste this prompt into your tool

Replace nothing; just paste.

```text
I want an interactive walkthrough of the "Science + Agentic AI Guide".

Please do the following carefully:

0) First, propose a short plan and list the exact commands you intend to run.
1) Create a new subfolder called `science-ai-guide` inside the current directory.
2) Download the latest guide content from GitHub into that folder (no git required).
   - Use the repository tarball: https://github.com/Chris-Cullins/science-ai-guide/archive/refs/heads/main.tar.gz
   - Use curl and tar.
   - Extract it so that `science-ai-guide/docs/` exists and contains the Markdown files.
3) After download, open and read:
   - `science-ai-guide/docs/index.md`
   - `science-ai-guide/docs/notes-from-the-human.md`
4) Give me a 10-minute "orientation" of how this guide is structured and what to read first.
5) Ask me 3 questions to personalize a learning path (my OS, how technical I am, what I want to use this for).
6) Based on my answers, give me a short plan for the next 60 minutes.

Rules:
- Keep it beginner-friendly.
- Do not ask me to do complex setup unless it is necessary.
- When you recommend running a command, explain what it does in one sentence.
```

## If you are on Windows

If the `tar` command is not available, ask the agent to use a zip download + PowerShell `Expand-Archive` instead.

## What success looks like

- You have a local copy of the guide in `~/agentic-ai-guide-tour/science-ai-guide/`
- You understand the "plan -> do -> verify" loop
- You have one small task you can delegate safely today
