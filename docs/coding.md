# Coding and Refactors

Agentic AI is especially strong at:

- refactoring
- adding tests
- fixing errors
- wiring up CLIs

## Your job

- define what must not change (scientific assumptions)
- define what must improve (reproducibility, readability, speed)
- require verification

## A safe refactor prompt

```text
Refactor this project for readability and reproducibility.

Constraints:
- Do not change scientific logic without asking.
- Keep outputs identical unless you explain why.

Definition of done:
- `make test` passes
- `make figures` regenerates the main figure(s)
```

## When to stop

If you cannot explain what changed, you are moving too fast.
