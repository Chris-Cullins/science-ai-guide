# First Hour: A Safe, Useful Win

Goal: get one small, real task done with an agentic tool, while keeping risk low.

This exercise takes 30-60 minutes. By the end, you'll have hands-on experience with the core loop: ask → review → verify → commit.

## Before you start

### Pick a safe project

Use something where mistakes don't matter:

- A personal side project
- A copy of a real project (not the original)
- An old analysis you're not actively using
- A fresh test repository

**Do not** use:
- Code with sensitive data
- Production systems
- Anything where breaking it would be a problem

### Verify it's under version control

```bash
cd your-project
git status
```

If you see "not a git repository," initialize one:

```bash
git init
git add .
git commit -m "Initial state before AI assistance"
```

This lets you see exactly what changes and undo anything you don't like.

### Open your agentic tool

Start Claude Code, Cursor, or whichever tool you chose:

```bash
# Claude Code
claude

# Codex CLI
codex
```

Navigate to your project folder.

## Pick one task

Choose **one** of these. Don't try to do everything at once.

### Option 1: Add a README (easiest)

Good for: any project without documentation

```text
Create a README.md that explains:
- What this project does (based on reading the code)
- How to install dependencies
- How to run the main script
- What outputs to expect

Read the existing code first to understand the project.
Keep the README concise (under 100 lines).
```

**What success looks like:** A clear README that accurately describes your project.

### Option 2: Add a minimal test

Good for: projects with no tests

```text
Add a minimal test for the main functionality.

Requirements:
- Use pytest
- Test that the main function runs without error on a tiny sample
- Keep the test simple and fast

Read the code first to understand what to test.
Create a tests/ directory if it doesn't exist.
Run the test to verify it passes.
```

**What success looks like:** `pytest tests/` runs and passes.

### Option 3: Create a Makefile

Good for: projects with multiple manual steps

```text
Create a Makefile with these targets:
- make install: install dependencies
- make test: run tests (or a simple verification)
- make run: run the main analysis/script

Look at the existing code to understand what commands are needed.
Test each target to make sure it works.
```

**What success looks like:** Each `make` command runs the right thing.

### Option 4: Clean up one messy script

Good for: scripts that have gotten out of hand

```text
Refactor this script for clarity:
[paste or point to the script]

Rules:
- Do not change what the script does
- Extract functions where it improves readability
- Add brief docstrings to functions
- Keep the same inputs and outputs

Propose a plan before making changes.
Run the script before and after to verify outputs match.
```

**What success looks like:** Same output, cleaner code.

## The prompt template

Whichever task you choose, wrap it in this template:

```text
Act like a careful research software engineer.

Before editing anything:
1. Summarize what you think this project does
2. Propose a short plan for the task
3. Wait for my approval before making changes

Rules:
- Keep changes small and reviewable
- Run verification after changes
- Explain how to undo if something goes wrong

Task:
[paste your chosen task here]
```

This template enforces the plan-do-verify workflow from the start.

## What to expect

### The agent reads your project

It will explore your files to understand the codebase. You'll see it reading various files. This is normal.

### The agent proposes a plan

Before making changes, it should tell you what it intends to do. Review this. If it misunderstands something, correct it.

### The agent makes changes

You'll see edits being made to files. In Claude Code, you'll be asked to approve changes. In other tools, you might see them happen directly.

### The agent runs verification

It should run something to confirm the changes work—tests, the script itself, a linter.

## After the agent finishes

### Review the diff

See exactly what changed:

```bash
git diff
```

or in your IDE's diff view.

Read through the changes. Do they make sense? Did the agent change anything unexpected?

### Run verification yourself

Don't just trust that the agent's verification worked. Run it yourself:

```bash
# For a test
pytest tests/

# For a Makefile
make test
make run

# For a script
python your_script.py
```

### Commit if it looks good

```bash
git add .
git commit -m "Add README via Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Or revert if it doesn't

```bash
git checkout .
```

This undoes all changes. That's why version control matters.

## What "success" looks like

After your first hour, you should be able to say:

- ✅ I can point to a diff and explain what changed
- ✅ I can run one command and see it work
- ✅ I didn't paste any sensitive data
- ✅ I understand the plan → do → verify loop
- ✅ I know how to undo changes if needed

## Common first-hour problems

### "The agent is confused about my project"

It might misunderstand what your code does. This is fine—correct it:

```text
That's not quite right. This script processes [X], not [Y].
The main entry point is [file]. Try again with that understanding.
```

### "The changes don't work"

Revert and try a more specific prompt:

```text
The test you wrote fails because [reason].
Fix the test to handle [specific issue].
```

### "It changed things I didn't ask for"

Be more explicit about scope:

```text
Only modify [specific file].
Do not touch any other files.
```

### "I don't understand the changes"

Ask for explanation:

```text
Explain what this change does and why you made it.
```

Never accept changes you don't understand.

## What's next

Once you've completed this first hour:

1. Try another task on the same project
2. Move to a slightly more complex task
3. Work through the [AI Fluency week](ai-fluency.md)
4. Set up a [CLAUDE.md](claude-code.md#claudemd) with your preferences

The goal is building fluency through practice. The first hour is just the beginning.

## See also

- [Why Agentic AI](why-agentic.md)
- [Workflows (Plan-Do-Verify)](workflows.md)
- [AI Fluency (1-Week Ramp)](ai-fluency.md)
- [Troubleshooting](troubleshooting.md)
