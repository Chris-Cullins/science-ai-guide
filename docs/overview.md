# What This Guide Is

This is a practical guide for scientists adopting agentic AI tools.

It assumes:

- You write some code (often Python/R/Matlab) but you are not a professional software engineer.
- You care about correctness, reproducibility, and not embarrassing yourself in a paper.
- You want a workflow that is faster, not just "cool".

## The promise

Agentic AI can:

- turn vague goals into concrete code changes
- automate the boring parts (setup, refactors, glue code)
- accelerate debugging
- help you explore literature and write more clearly

## The catch

Agentic AI also:

- makes mistakes confidently
- can create plausible but wrong plots, stats, or citations
- can leak data if you paste sensitive content
- can change many files quickly (reproducibility risk)

The goal of this guide is to help you get the upside without eating the downside.

## A simple rule

If the agent can take actions, you must:

1. review diffs
2. run verification
3. keep a reproducible record

## Glossary (quick)

- Agentic AI: an AI system that can take actions (edit files, run commands, call tools).
- Diff: a view of what changed in files.
- Repo: a project folder tracked by git (version control).
- Context window: how much information the model can consider at once.
- Tokens: the model's "units" of text; cost is often per token.
