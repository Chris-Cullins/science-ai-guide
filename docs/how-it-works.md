# How Agentic AI Works (Mental Model)

You do not need deep ML knowledge. But you do need a usable mental model.

## Chat model vs agent

- Chat model: generates text.
- Agent: uses a chat model plus tools (file edits, commands, web, etc.) to do multi-step work.

## The agent loop

Most agentic systems follow a loop like:

1. Read context (files, your instructions)
2. Plan
3. Take an action (edit file, run command)
4. Observe the result (diffs, errors, output)
5. Iterate until "done"

## Why errors happen

Common causes:

- Missing context (the agent did not see the relevant file)
- Ambiguous goal (no definition of done)
- Overconfident guesses (hallucinations)
- Hidden assumptions (units, conventions)

## Context window and tokens

- Models do not see your whole computer.
- They only see what is placed in their context.
- Longer context generally costs more and can be noisier.

**Important:** As conversations grow longer, model performance often degrades. A common rule of thumb: once you hit roughly 40-50% of the context window, the model may start getting confused, forgetting earlier instructions, or producing lower-quality output. The fix is to break large tasks into smaller sessions, or start fresh when you notice quality dropping.

## What makes agentic AI powerful

- It can try something, see it fail, and fix it.
- It can make consistent changes across many files.
- It can automate repetitive steps.

## What makes it dangerous

- It can change many files quickly.
- It can produce outputs that look right.
- It can run commands you did not understand.

Your control points are: scope, diffs, and verification.

## See also

- [Workflows (Plan-Do-Verify)](workflows.md)
- [Verification and Rigor](verification.md)
- [Troubleshooting](troubleshooting.md)
