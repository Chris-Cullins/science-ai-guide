# Why Agentic AI (Instead of Chat)

You've probably used ChatGPT or Claude's web interface. You ask a question, get an answer, copy some code, paste it, run it, hit an error, go back, ask again... it works, but there's friction at every step.

Agentic AI is different. Instead of chatting back and forth, you give the agent access to your actual project. It reads your files, writes code, runs commands, sees the errors, and fixes them—all while you supervise.

This page explains why that matters for scientists.

## Chat-only AI vs agentic AI

### Chat-only workflow

1. Describe your problem in words
2. Get code in a chat response
3. Copy the code
4. Paste into a file
5. Run it
6. Hit an error
7. Copy the error back to chat
8. Get a fix
9. Repeat steps 3-8 until it works
10. Hope you didn't introduce bugs while copy-pasting

This works for small things, but it's exhausting for real projects.

### Agentic workflow

1. Point the agent at your project folder
2. Describe what you want
3. The agent reads your files, understands the context
4. It writes code directly into your files
5. It runs the code, sees errors, fixes them
6. You review the changes (via diff)
7. You run verification (tests, scripts)
8. Done

The agent handles the mechanical parts. You handle the judgment.

## What agentic tools can actually do

### Read and understand your project

The agent can:
- See your file structure
- Read your existing code
- Understand your dependencies
- Know what functions exist and what they do

This means you don't have to explain everything from scratch every time.

### Edit files directly

Instead of giving you code to copy-paste, the agent edits your actual files. You see a diff of exactly what changed, just like a code review.

### Run commands and see results

The agent can:
- Run your scripts
- Execute tests
- See error messages
- Check if things work

This creates a feedback loop: try something, see if it works, fix it if not.

### Iterate until it works

When something fails, the agent can:
- Read the error message
- Understand what went wrong
- Propose a fix
- Try again

This loop—try, fail, fix, retry—is where most coding time goes. The agent can do it faster.

## Concrete examples

### Example: "Fix my broken script"

**Chat approach:**
You paste your script into chat. You paste the error. You get a suggestion. You paste it back into your file. You run it. New error. Paste that. Get another suggestion. Repeat.

**Agentic approach:**
You say "This script is failing with [error]. Fix it."
The agent reads the script, runs it, sees the error, identifies the problem, fixes it, runs it again, confirms it works. You review the diff and approve.

### Example: "Make this reproducible"

**Chat approach:**
You ask for advice on making your analysis reproducible. You get a list of suggestions. You implement them yourself, one by one, asking follow-up questions when you get stuck.

**Agentic approach:**
You say "Make this project reproducible: add a Makefile, pin dependencies, create a config file for parameters."
The agent does it. Creates the Makefile. Generates requirements.txt. Extracts hardcoded values into a config. You review, test, done.

### Example: "Add tests"

**Chat approach:**
You paste a function. Ask for tests. Get tests back. Create a test file. Paste them in. Run pytest. Some fail because of import issues. Ask for fixes. Repeat.

**Agentic approach:**
You say "Add tests for the functions in src/analysis.py."
The agent reads your code, writes tests, runs them, fixes import issues, runs again until they pass. You review the tests, verify they make sense, done.

## The real shift

When you use agentic AI well, your job changes. You spend less time on:

- Typing code
- Debugging syntax errors
- Setting up project structure
- Writing boilerplate

You spend more time on:

- **Defining the goal** - What exactly should this do?
- **Setting constraints** - What must not change? What matters most?
- **Verifying results** - Is this actually correct? Does it match expectations?
- **Making decisions** - Which approach should we take?

This is a managerial skill, not a coding skill. You're directing and reviewing, not typing.

## When agentic AI helps most

### Setup and infrastructure

The "yak shaving" that eats your time:
- Setting up a new project
- Configuring environments
- Writing Makefiles
- Creating CLI interfaces
- Organizing messy code

### Refactoring

Making code better without changing behavior:
- Extracting functions
- Renaming for clarity
- Adding type hints
- Splitting large files

### Debugging

When you have an error and need to fix it:
- Reading stack traces
- Identifying root causes
- Proposing and testing fixes

### Documentation

Generating docs from existing code:
- README files
- Docstrings
- Usage examples

## When NOT to use agentic AI

### Sensitive data you cannot share

If your data contains:
- Patient information
- Classified material
- Proprietary industry data
- Anything your institution prohibits sharing

Then don't put it in an external tool. See [Safety & Privacy](safety-privacy.md).

### High-stakes decisions without verification

Don't blindly trust AI output for:
- Clinical decisions
- Safety-critical systems
- Published results (without verification)
- Anything where being wrong has serious consequences

### Tasks where you cannot define a test

If you can't articulate what "correct" looks like, you can't verify the output. And if you can't verify, you shouldn't delegate.

**The rule: If you cannot verify it, do not delegate it.**

## Getting started

If this sounds useful, the next step is to try it:

1. [Pick a tool](tooling.md)
2. [Set it up](claude-code.md)
3. [Do the first-hour exercise](first-hour.md)

You'll learn more from 30 minutes of hands-on use than from reading about it.

## See also

- [What This Guide Is](overview.md)
- [Workflows (Plan-Do-Verify)](workflows.md)
- [Pick Your Tools](tooling.md)
