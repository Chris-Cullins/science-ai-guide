# FAQ

## Is this going to replace scientists?

No one knows. But it is already changing the day-to-day work.

The most robust stance is: learn to use it, keep your verification habits strong, and keep your scientific judgment sharp.

## Will I lose my skills?

Skill atrophy is real if you stop thinking.

Mitigations:

- keep doing some work "by hand" (derivations, small scripts)
- require the agent to explain reasoning
- use it to teach you, not just to produce output

## Can I trust citations?

Not by default.

If you did not provide sources, assume citations may be invented.

## Can I use this with R / Matlab / Julia / other languages?

Yes. Agentic tools work with any language that can be edited as text files and run from a terminal. Python examples dominate this guide because it is the most common in scientific computing, but the workflows apply equally to R scripts, Matlab `.m` files, Julia code, or shell scripts.

The key is the same: define the goal, let the agent edit and run, verify the output.

## What if my institution blocks these tools?

Options:

- Check if your institution has an approved alternative (some have enterprise agreements with specific vendors).
- Use a personal device on a personal network for non-sensitive, public-data work.
- Ask IT about the specific policy—sometimes "blocked" means "not yet evaluated."
- See [Burner Machine and Sandboxes](burner-machine.md) for isolation strategies.

If you genuinely cannot use external tools, some of the prompting and verification habits in this guide still apply to local models or approved internal systems.

## How do I explain this to skeptical colleagues or advisors?

Focus on:

- **Verification**: "I review every change and run tests before trusting results."
- **Reproducibility**: "The workflow produces one-command reproducible outputs."
- **Transparency**: "I disclose AI assistance and can show exactly what it did (diffs, logs)."

Skepticism is healthy. The goal is not to convince anyone that AI is magic, but to show that your specific workflow maintains scientific rigor.

## What about code I wrote with AI—do I own it?

Generally, yes—you own code you produce using AI tools, just as you own code you write with autocomplete or Stack Overflow snippets. However:

- Check your institution's IP policies.
- Check the terms of service of the specific tool.
- If you are working on proprietary or patentable code, consult your tech transfer office.

This is not legal advice.

## Which model is best for X?

It changes constantly. As of early 2026:

- **Claude (Sonnet/Opus)**: strong at multi-file refactors, long context, and reasoning
- **GPT-4 / GPT-4o**: good general-purpose, wide tool ecosystem
- **Gemini**: strong at very long documents and multimodal tasks

For most scientist workflows, any of the top-tier models will work. Pick based on what your institution supports and what you can afford.

See: [Multi-Model Strategy](multi-model.md)

## The agent made a mess of my code. How do I recover?

If you are using git (you should be):

- `git diff` to see what changed
- `git stash` to set aside changes temporarily
- `git checkout .` to discard all uncommitted changes
- `git reset --hard HEAD~1` to undo the last commit (use with caution)

If you are not using git, your options are limited. This is why version control is non-negotiable for agentic workflows.

See: [Troubleshooting](troubleshooting.md)

## How do I know when a session is "too long"?

Signs:

- The agent starts forgetting earlier instructions
- Responses become repetitive or less coherent
- It makes mistakes it would not have made earlier

Rule of thumb: if a session has been running for more than 30-60 minutes of active work, or if you have pasted a lot of context, consider starting fresh. Summarize what you accomplished and begin a new session with a clean slate.

## See also

- [Troubleshooting](troubleshooting.md)
- [Safety, Privacy, and Policy](safety-privacy.md)
- [Disclosure](disclosure.md)

