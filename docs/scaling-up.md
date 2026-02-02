# Scaling Up Your Usage (Advanced)

Once you have the basics down, the biggest productivity jump comes from running multiple agent sessions in parallel.

Example: many terminals open, each running Claude Code on a different task.

This page explains how to scale up without losing correctness, burning money, or making a reproducibility mess.

## The core idea

You are not using "one assistant".
You are running a small team.

That means you need:

- clear task boundaries
- a shared definition of done
- a verification step per task
- a way to merge results safely

## What parallelism is good for

- "Do in parallel" work:
  - writing tests while another session refactors
  - generating a figure script while another session cleans a dataset
  - drafting paper text while another session builds a reproducible pipeline
  - literature summaries in parallel (paper A, paper B, paper C)

- "Do not parallelize" work:
  - editing the same file in multiple sessions
  - changing the same experiment config from multiple places
  - anything where you cannot easily compare outputs

## A practical setup

### 1) One terminal per task

Name the job in your first message:

- "Session A: refactor + tests"
- "Session B: figures"
- "Session C: README + reproducibility"

### 2) One branch (or worktree) per task

If you use git, the clean approach is one branch per task.

If you are comfortable with git worktrees, they are ideal for parallel agents.
Each agent gets its own folder and can edit freely.

Rule: never run two agents against the same working directory.

### 3) One verification command per task

Examples:

- `pytest`
- `make figures`
- `python scripts/make_fig_2.py --config configs/fig2.yaml`

If the agent cannot tell you what command proves success, the task is not ready.

## Coordination patterns

### Pattern: manager + workers

One "manager" session:

- maintains the plan
- defines interfaces (file names, function signatures)
- reviews results from worker sessions

Worker sessions:

- implement a specific piece
- provide diffs and the verification output

This reduces chaos dramatically.

### Pattern: critique session

Keep one session whose only job is:

- review diffs
- look for footguns
- propose tests

Even if you do not run multiple agents, this pattern is worth it.

## Preventing the common disasters

### Disaster 1: two agents edit the same file

Fix:

- assign ownership per file
- split tasks by module
- use worktrees/branches

### Disaster 2: the repo "works" but results changed silently

Fix:

- pin dependencies
- capture configs
- add regression checks (hashes, summary stats)
- require the agent to explain any output changes

### Disaster 3: cost explodes

Fix:

- set a budget per day/week
- keep tasks small
- stop runaway sessions
- do not paste huge context repeatedly

See: [Cost Control](cost-control.md)

## A concrete "multi-terminal" workflow

1. Create a task list for the next 2 hours.
2. Split into 3-5 independent tasks.
3. Create a new branch/worktree per task.
4. Start a session per branch.
5. Require each session to:
   - propose a plan
   - keep changes small
   - run verification
   - summarize what changed
6. Merge one task at a time back into main.

## Useful prompts

### Session kickoff prompt

```text
You are working in parallel with other agent sessions.

Your task:
- <one specific task>

Rules:
- Only edit files in <folder/module>.
- Do not edit files owned by other sessions.
- Propose a plan first.
- Provide a verification command and run it.
- End by summarizing the diff in plain English.
```

### Manager prompt

```text
You are the "manager" agent.

Your job:
- break work into independent tasks
- assign file ownership
- define interfaces between tasks
- define verification commands

Output:
- a numbered task list with owners (Session A/B/C)
- the expected artifacts per task
```

## If you are doing science (not software)

The same idea applies:

- parallelize what is independent
- centralize decisions about assumptions, units, and definitions
- treat every output as untrusted until it passes checks
