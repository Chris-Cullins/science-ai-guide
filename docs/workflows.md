# Workflows (Plan → Do → Verify)

Agentic tools feel magical when you treat them like a junior colleague: they move fast, but you own correctness.

The core workflow is simple: **Plan → Do → Verify → Record**. This page explains each step and how to apply it in scientific work.

## The default loop

### 1. Plan

Before the agent changes anything, ask for a plan:

```text
Before making any changes, propose a plan:
- What files will you modify?
- What's your approach?
- What could go wrong?
- How will we verify it worked?
```

Review the plan. Does it make sense? Is the scope right? Will it touch things you don't want touched?

**Why this matters:** Agents can move fast in the wrong direction. A 30-second plan review saves 30 minutes of cleanup.

### 2. Do

Let the agent implement in small, reviewable chunks. Not everything at once.

```text
Implement step 1 of the plan.
Stop after that step so I can review before continuing.
```

For larger tasks:
```text
Implement this in stages. After each stage:
- Show me what changed
- Run a quick verification
- Wait for my approval before continuing
```

**Why this matters:** Small changes are reviewable. Large changes are overwhelming. You want to catch mistakes before they compound.

### 3. Verify

Run checks to confirm the changes work:

- **Tests**: `pytest tests/`
- **Scripts**: Run them and check outputs
- **Diffs**: Review what actually changed
- **Sanity checks**: Do the numbers make sense?

```bash
# See what changed
git diff

# Run tests
pytest tests/ -v

# Run the analysis and check outputs
python scripts/analyze.py
```

**Why this matters:** "It should work" is not verification. Running it is verification.

### 4. Record

Document what happened:

- Commit with a clear message
- Note any assumptions made
- Record how to reproduce

```bash
git add .
git commit -m "Add data normalization step

- Normalizes columns A-D by internal standard
- Verified: outputs match expected values within 0.1%
- Config: configs/normalization.yaml

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Why this matters:** Future you (and collaborators) need to know what was done and why.

## What to verify in science work

Scientific verification is more demanding than typical software verification.

### Data provenance

- Which exact files/versions were used?
- Were any transformations applied?
- Can you trace back to the raw data?

```text
Before running this analysis, confirm:
- Which data files you'll use
- What preprocessing has been applied
- Where outputs will be saved
```

### Determinism

- Are random seeds fixed?
- Are dependencies pinned?
- Are configs saved?

```text
Add determinism to this analysis:
- Set random seed to 42 at the start
- Save the config used to results/run_config.yaml
- Log the dependency versions
```

### Sanity checks

- Do units make sense?
- Do limiting cases behave correctly?
- Do back-of-the-envelope estimates match?

```text
Add sanity checks to this analysis:
- Print min/max/mean of key variables
- Verify units are consistent (all in SI)
- Check that output is in expected range [0, 1]
```

### Reproducibility

The gold standard: "fresh clone → one command → same figures."

```text
Verify reproducibility:
- Clone to /tmp/test-repo
- Run: pip install -r requirements.txt && make figures
- Compare outputs to the original
```

## Example workflows

### Workflow 1: Reproducible analysis

```text
You are helping me make this analysis reproducible.

Plan first:
- Identify all hardcoded parameters
- Find all data dependencies
- Check for random seeds

Rules:
- Do not change scientific logic without asking
- Move parameters to a config file
- Add a single command that reproduces the main figure(s)
- Add quick sanity checks (units, basic invariants)

Goal:
- When I run `make figures`, it produces the same outputs
```

### Workflow 2: Refactoring for a new lab member

```text
Please refactor this project so a new lab member can run it.

Plan first:
- What's unclear about the current structure?
- What's the minimum viable documentation?

Deliverables:
- README with setup + one-command run
- Pinned dependencies (requirements.txt)
- Scripts organized into a minimal pipeline
- A short checklist for verifying outputs

Do not change:
- Scientific logic
- Numerical outputs (verify they match before/after)
```

### Workflow 3: Debugging a failing analysis

```text
This analysis is producing wrong results.

Expected: [describe expected output]
Actual: [describe actual output]
Error (if any): [paste error]

Approach:
1. First, understand the code and identify likely causes
2. Propose a debugging plan
3. Make minimal changes to fix the issue
4. Verify the output is now correct

Do not:
- Refactor unrelated code
- Change things that aren't broken
```

### Workflow 4: Adding tests to existing code

```text
Add tests for the core functions in src/analysis.py.

Plan first:
- Which functions are most critical to test?
- What edge cases should be covered?

Requirements:
- Use pytest
- Each test should run in under 1 second
- Test both normal cases and edge cases
- Include at least one test that verifies numerical accuracy

Run the tests after writing them.
```

## When to break the loop

Sometimes you need to diverge from plan-do-verify:

### Exploration mode

When you're exploring possibilities, not building:

```text
I'm exploring different approaches. Don't implement anything yet.
Just describe options for [X] and their tradeoffs.
```

### Quick fixes

For tiny, obvious fixes:

```text
This is a one-line fix: [describe].
Just make the change and verify it works.
```

### Emergency rollback

When things are broken and you need to recover:

```text
Stop. Don't make more changes.
Show me git status and the last 5 commits.
Help me understand what went wrong.
```

## Common workflow mistakes

### Skipping the plan

"Just do it" leads to surprises. Even for small tasks, a one-sentence plan helps.

### Too much at once

"Refactor everything" is not reviewable. "Refactor the data loading function" is.

### Trusting without verifying

"The agent said it works" is not verification. Run it yourself.

### Not recording

If you don't commit and document, you'll forget what was done and why.

## See also

- [First Hour](first-hour.md)
- [Verification and Rigor](verification.md)
- [Checklists](checklists.md)
- [Troubleshooting](troubleshooting.md)
