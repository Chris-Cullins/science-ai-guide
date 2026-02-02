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

## Recovery strategies for bigger messes

### The agent made many wrong changes

If you caught it early:
```bash
git checkout .          # discard all uncommitted changes
git clean -fd           # remove untracked files (careful!)
```

If you already committed:
```bash
git log --oneline       # find the last good commit
git reset --hard <hash> # go back to it (loses later commits)
```

If you want to keep some changes:
```bash
git stash               # set aside current changes
git diff HEAD~3         # review last 3 commits
# cherry-pick what you want to keep
```

### The agent introduced a subtle bug in math/statistics

This is the hardest case because the code "works" but produces wrong results.

Prevention is better than cure:
- Always add sanity checks (known values, limiting cases)
- Compare against a reference implementation or hand calculation
- Use synthetic data where you know the correct answer

If you suspect a bug:
1. Isolate the suspicious section
2. Add print statements or logging for intermediate values
3. Test on a minimal example
4. Ask a different model (or a colleague) to review

### The agent "fixed" something that wasn't broken

Classic symptoms:
- A working feature stops working
- Tests that passed now fail
- Behavior changed in ways you didn't ask for

Fix:
1. `git diff` to see exactly what changed
2. Revert the specific changes that broke things
3. Be more specific in your next prompt: "Only change X, do not modify Y"

### The session is too long and quality has dropped

Signs:
- Agent forgets earlier context
- Repeated mistakes
- Circular conversations

Fix:
1. Summarize what you accomplished so far
2. Start a fresh session
3. Paste only the essential context into the new session

## Preventing problems before they start

- **Commit frequently**: Small commits are easy to revert.
- **Review diffs immediately**: Don't let changes pile up.
- **Keep tasks small**: One clear goal per session.
- **Define "done" upfront**: A test, a command, a specific output.

## See also

- [Workflows (Plan-Do-Verify)](workflows.md)
- [Verification and Rigor](verification.md)
- [Git Basics](git-basics.md)
