# First Hour: A Safe, Useful Win

Goal: get one small, real task done with an agentic tool, while keeping risk low.

## Setup

- Use a non-sensitive project (or a copy).
- Make sure it's under version control.

## Pick one task (30-60 minutes)

1. "Add a `README.md` that explains setup + a one-command run."
2. "Add a minimal test that checks the main function runs on a tiny sample."
3. "Make a `Makefile` (or `justfile`) with `make format`, `make test`, `make run`."

## The prompt

```text
Act like a careful research software engineer.

Before editing anything:
- summarize what you think this project does
- propose a short plan

Rules:
- keep changes small and reviewable
- run a quick verification step
- explain how to undo changes

Task:
<paste the task you chose>
```

## What "success" looks like

- You can point to a diff and say what changed.
- You can run one command and see it work.
- You didn't paste any sensitive data.
