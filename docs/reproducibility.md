# Reproducibility Habits (AI-Assisted Work)

Agentic AI can change many files quickly. Reproducibility is how you keep that power from becoming chaos.

## The minimum bar

- "Fresh clone -> one command -> same key outputs."

## What to capture

- Inputs: where data came from, which version, any preprocessing
- Parameters: config files, command-line flags
- Environment: pinned dependencies, OS assumptions
- Randomness: seeds and deterministic settings
- Outputs: figures/tables written to a predictable location

## Two practical patterns

1. A `Makefile` (or `justfile`) that encodes the canonical commands.
2. A `configs/` folder with "paper-ready" configs checked into the repo.

## See also

- [Data Analysis](data-analysis.md)
- [Figures and Tables](figures.md)
- [Verification and Rigor](verification.md)
- [Lab Rollout](lab-rollout.md)
