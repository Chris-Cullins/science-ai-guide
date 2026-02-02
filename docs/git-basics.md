# Git Basics (So You Can Review and Undo)

Git is the safety harness for agentic AI. When an agent can change dozens of files in seconds, you need a way to see exactly what changed and undo mistakes instantly. That's git.

You don't need to master git. You need to know enough to stay safe.

## The mental model

- **Repository (repo)**: A folder where git tracks changes
- **Commit**: A snapshot of your project at a point in time
- **Diff**: A view of what changed between two points
- **Branch**: A parallel version of your project (for experiments)
- **Staging area**: Where you prepare changes before committing

Think of commits like save points in a video game. You can always go back.

## The essential commands

### See what's happening

```bash
git status              # What files changed? What's staged?
git diff                # Show unstaged changes (what you haven't added yet)
git diff --staged       # Show staged changes (what you're about to commit)
git log --oneline -10   # Show last 10 commits
```

Run `git status` constantly. It's your best friend.

### Save your work

```bash
git add filename.py     # Stage a specific file
git add -A              # Stage all changes (use carefully)
git commit -m "message" # Create a commit with a message
```

Write commit messages that explain *why*, not just *what*:
- Bad: "Update analysis.py"
- Good: "Fix off-by-one error in bootstrap resampling"

### Undo mistakes

```bash
git diff                 # See what changed before deciding
git checkout -- file.py  # Discard changes to one file
git checkout .           # Discard ALL uncommitted changes (careful!)
git reset HEAD~1         # Undo the last commit (keep changes as unstaged)
git reset --hard HEAD~1  # Undo the last commit AND discard changes (very careful!)
```

### Work with branches

```bash
git branch                    # List branches
git checkout -b experiment    # Create and switch to new branch
git checkout main             # Switch back to main
git merge experiment          # Merge experiment into current branch
```

## Why scientists should care

### You can always see what changed

When an agent makes 50 edits across 12 files, `git diff` shows you exactly what happened. You can review every line before committing.

### You can undo anything

Made a mistake? Approved something you shouldn't have?

```bash
git checkout .   # Undo all uncommitted changes, instantly
```

This is why you should commit frequently. Each commit is a safe point you can return to.

### You can reproduce exactly what produced a result

Every commit has a unique hash (like `d6958af`). When you record this hash alongside your figures and results, you can always recreate the exact state of the code that produced them.

```bash
git rev-parse HEAD   # Get current commit hash
```

### You can experiment safely

Create a branch, try something risky, and if it fails, just delete the branch. Your main code is untouched.

```bash
git checkout -b risky-refactor
# ... try things ...
# If it works:
git checkout main && git merge risky-refactor
# If it fails:
git checkout main && git branch -D risky-refactor
```

## The recommended workflow for agentic AI

### Before starting a session

```bash
git status                    # Make sure you're starting clean
git checkout -b ai-session-1  # Create a branch for this session
```

### During the session

After each significant change the agent makes:

```bash
git diff                      # Review what changed
git add -A && git commit -m "Description of change"
```

Small, frequent commits mean easy rollbacks.

### After the session

```bash
git checkout main
git merge ai-session-1        # If everything looks good
# or
git branch -D ai-session-1    # If you want to discard everything
```

## Common scenarios

### "The agent made changes I don't want"

```bash
git diff                      # See what changed
git checkout -- file.py       # Undo changes to specific file
# or
git checkout .                # Undo ALL changes
```

### "I committed something I shouldn't have"

```bash
git reset HEAD~1              # Undo commit, keep changes as unstaged
git checkout -- bad-file.py   # Discard the bad changes
git add -A && git commit -m "Fixed version"
```

### "I want to see what a file looked like before"

```bash
git log --oneline file.py     # See commits that touched this file
git show abc123:file.py       # Show file at commit abc123
```

### "I want to go back to a previous state"

```bash
git log --oneline             # Find the commit hash you want
git checkout abc123           # Go to that commit (detached HEAD)
# Look around, copy what you need
git checkout main             # Go back to current state
```

## What to keep out of git

Create a `.gitignore` file:

```text
# Data files (usually too large)
data/raw/
*.csv
*.h5

# Results (regenerate from code)
results/
*.png
*.pdf

# Environment
.venv/
__pycache__/
*.pyc

# Secrets (NEVER commit these)
.env
*credentials*
*secret*
```

Keep your repo focused on **code and config**. Data and results should be regenerable.

## Learning more

You don't need to learn all of git. But if you want to go deeper:

- [Git basics from GitHub](https://docs.github.com/en/get-started/using-git/about-git)
- Run `git help <command>` for any command

The most important thing: commit frequently, review diffs, and remember that you can always undo.

## See also

- [Project Structure](project-structure.md)
- [Troubleshooting](troubleshooting.md)
- [Reproducibility](reproducibility.md)
