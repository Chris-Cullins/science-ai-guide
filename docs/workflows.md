# Workflows (Plan -> Do -> Verify)

Agentic tools feel magical when you treat them like a junior colleague: they move fast, but you own correctness.

## The default loop

1. **Plan**: ask for a short plan and the expected artifacts.
2. **Do**: let it implement in small chunks.
3. **Verify**: run checks (tests, plots, unit sanity checks) and review diffs.
4. **Record**: write down what changed and how to reproduce it.

## What to verify in science work

- Data provenance: exactly which files/versions were used
- Determinism: fixed seeds, pinned versions, saved configs
- Sanity checks: units, limiting cases, back-of-the-envelope estimates
- Reproducibility: "fresh clone -> one command -> same figures"

## Two example task prompts

### Reproducible analysis

```text
You are helping me make this analysis reproducible.

Rules:
- Propose a plan first.
- Do not change scientific logic without asking.
- Add a single command that reproduces the main figure(s).
- Add quick sanity checks (units, basic invariants).

Goal:
- When I run `make figures` (or similar), it produces the same outputs.
```

### "Take over the annoying parts"

```text
Please refactor this project so a new lab member can run it.

Deliverables:
- README with setup + one-command run
- pinned dependencies
- scripts organized into a minimal pipeline
- a short checklist for verifying outputs are sensible
```
