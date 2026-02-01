# Troubleshooting

Agentic tools fail in predictable ways. Most fixes are workflow fixes.

## When the agent "thrashes"

Symptoms:

- repeated edits without progress
- long responses that do not change the outcome

Fix:

- stop and restate the goal
- ask for a smaller plan
- reduce scope to a minimal reproducible example

## When results are wrong but plausible

Fix:

- add explicit sanity checks
- test on synthetic data
- require units and assumptions

## When the environment breaks

Fix:

- pin dependencies
- use a virtual environment
- add a one-command setup

## If you get lost

- use `git diff` to see what changed
- make a commit before big changes
- revert or back out changes rather than trying to patch blindly
