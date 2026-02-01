# Git Basics (So You Can Review and Undo)

Git is the safety harness for agentic AI.

## The mental model

- A repo is a folder where git tracks changes.
- A commit is a snapshot.
- A diff shows what changed.

## Minimal commands

```bash
git status
git diff
git add -A
git commit -m "message"
```

## Why scientists should care

- You can always see what changed.
- You can undo mistakes.
- You can reproduce exactly what produced a figure.

## Recommended workflow

- Make small commits.
- Keep analysis outputs out of the repo unless needed.
- Use branches for experiments.
