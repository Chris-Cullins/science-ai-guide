# Prompt Templates for Scientists

These are designed to be copy/pasted into an agentic tool like Claude Code.

## 1) Paper-to-code replication

```text
I want to replicate a figure from a paper.

Context:
- I will provide the paper PDF (or key equations) and my dataset.

Rules:
- Start by listing all assumptions you are making.
- Implement a minimal, reproducible script first.
- Add unit tests or numeric spot-checks against limiting cases.

Deliverables:
- `src/` code
- `data/README.md` describing inputs
- `results/` with generated figure
- `README.md` with exact run steps
```

## 2) "Convert my messy notebook into a pipeline"

```text
Turn this notebook into a reproducible pipeline.

Constraints:
- Keep outputs identical unless you explain why they change.
- Add a config file for parameters.
- Pin dependencies.
- Add a `make run` (or equivalent).

Deliverables:
- `pipeline/` or `src/`
- `configs/`
- `README.md`
```

## 3) Grant/paper writing assistant (safe mode)

```text
Help me improve clarity without inventing facts.

Rules:
- Do not add citations.
- Do not change scientific claims.
- Only propose edits that improve structure, clarity, and readability.

Output:
- Provide a revised version and a short list of what changed.
```
