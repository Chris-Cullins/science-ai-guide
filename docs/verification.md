# Verification and Rigor (How Not to Fool Yourself)

Agentic AI can be fast. It is not inherently careful.

Your job is to make correctness cheap.

## What to verify

### Code

- Does it run?
- Do tests pass?
- Are edge cases handled?

### Math and statistics

- Units and dimensional analysis
- Limiting cases
- Known benchmarks
- Synthetic data tests

### Plots and figures

- Are axes labeled correctly?
- Are you plotting what you think you are plotting?
- Are preprocessing steps recorded?

### Writing

- No invented citations
- Claims match the data
- Clear separation between results and speculation

## A verification mindset

Ask:

- What would prove this wrong?
- What is the simplest test that would catch the most likely mistake?

## Cross-checking

Useful pattern:

- Use one model to propose.
- Use another model (or your own reasoning) to critique.

But do not confuse "two models agree" with truth. They can share the same blind spots.

## Reproducibility is part of verification

If you cannot rerun it reliably, you cannot really verify it.

## Staying sharp (avoiding skill atrophy)

Heavy AI use can erode your own abilities if you are not deliberate.

Habits that help:

- **Do some work by hand**: One derivation per week, one script without AI assistance.
- **Explain it back**: After the AI solves something, explain the solution to yourself (or a colleague). If you cannot, you did not learn.
- **Require explanations**: Ask the AI to explain its reasoning, then evaluate whether the reasoning is sound.
- **Periodically calibrate**: Try a task without AI, then with AI. Notice what you would have missed.

The goal is not to avoid AI, but to ensure you remain capable of catching its mistakes.

## See also

- [Workflows (Plan-Do-Verify)](workflows.md)
- [Troubleshooting](troubleshooting.md)
- [Reproducibility](reproducibility.md)
