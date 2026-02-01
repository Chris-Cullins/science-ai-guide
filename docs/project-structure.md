# Project Structure That Works With Agents

Most pain comes from messy structure. Fixing structure pays off.

## A simple layout

This works for many labs:

```text
project/
  README.md
  pyproject.toml (or requirements.txt)
  data/            # raw or external data references
  src/             # code
  notebooks/       # exploratory work
  scripts/         # entry points
  results/         # generated outputs (often gitignored)
  configs/         # parameter sets for runs
  tests/           # sanity checks
```

## One-command runs

Pick a canonical command, for example:

- `make figures`
- `make test`
- `python -m yourpackage.run --config configs/paper.yaml`

Agents are much more reliable when "done" is defined as "this command passes".
