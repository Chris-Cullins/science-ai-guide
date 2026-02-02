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

## 4) Debug a crashing simulation or script

```text
My script crashes with the following error:
<paste error>

Context:
- The script is in <file path>.
- It is supposed to <brief description of what it does>.

Task:
- Identify the root cause.
- Propose a fix.
- Explain why it failed.

Rules:
- Do not change the scientific logic without asking.
- If you need to see more files, ask.
```

## 5) Review code for correctness before trusting results

```text
I need you to review this analysis code before I trust its outputs.

Task:
- Read the code carefully.
- List any potential bugs, edge cases, or silent failures.
- Check for common pitfalls: off-by-one errors, incorrect joins, unit mismatches, unintended type coercion.
- Tell me what assumptions the code makes.

Output:
- A numbered list of issues (or "none found").
- Confidence level (high / medium / low) for each issue.
```

## 6) Generate synthetic test data

```text
I need synthetic test data to validate my analysis pipeline.

Context:
- The real data has columns: <list columns and types>
- The pipeline should produce <expected output>

Task:
- Generate a small synthetic dataset (10-50 rows) that exercises:
  - Normal cases
  - Edge cases (empty values, extreme values, boundary conditions)
  - At least one case that should trigger a known behavior

Output:
- A CSV or code that generates the data.
- A brief description of what each test case is meant to check.
```

## 7) Explain inherited or unfamiliar code

```text
I inherited this codebase and need to understand it.

Task:
- Summarize what this code does at a high level.
- Identify the main entry points.
- List the key functions and their purposes.
- Flag any confusing or non-obvious parts.

Rules:
- Do not change anything.
- If something is unclear, say so rather than guessing.
```

## 8) Add tests to existing code

```text
Add tests for the following code.

Context:
- File(s): <paths>
- Testing framework: <pytest / unittest / other>

Task:
- Write tests that cover:
  - Normal operation
  - Edge cases
  - At least one failure case
- Tests should be independent and fast.

Rules:
- Do not modify the original code unless necessary to make it testable.
- If you need to refactor for testability, propose the change first.
```

## 9) Domain-specific: physics / numerical work

```text
You are helping with a physics or numerical analysis project.

Extra rules:
- Always state units explicitly.
- Check dimensional consistency.
- For numerical code, consider precision, stability, and convergence.
- When in doubt, add a limiting-case check or a back-of-the-envelope sanity test.
```

## 10) Domain-specific: biology / life sciences

```text
You are helping with a biology or life sciences project.

Extra rules:
- Be careful with sequence data (orientation, indexing conventions).
- Statistical tests must be appropriate for the data type (counts, proportions, continuous).
- Do not invent gene names, pathways, or biological claims.
- If working with patient or human-subject data, remind me to check privacy constraints.
```
