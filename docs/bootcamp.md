# Bootcamp: Agentic AI for Scientists (2 Days)

This is a practical bootcamp plan you can run solo or as a lab.

The goal is not to "learn AI". The goal is to build habits that produce correct, reproducible work faster.

## Day 0 (30 minutes): Safety first

1. Decide what data you will NOT share.
   - Default: no unpublished results, no human-subject data, no credentials.
2. Decide whether you want a sandbox setup.
   - See: [Burner Machine and Sandboxes](burner-machine.md)
3. Pick one primary tool.
   - Recommended: Claude Code ([Claude Code](claude-code.md))

## Day 1: Get a real win with guardrails

### Module 1: Install and run your first session (30 minutes)

- Follow: [Claude Code](claude-code.md)
- If you get stuck, use: [Troubleshooting](troubleshooting.md)

### Module 2: First win (60 minutes)

Use: [First Hour](first-hour.md)

Target outcome:

- a README
- a one-command run
- a tiny sanity check

### Module 3: Learn the workflow loop (60 minutes)

Read: [Workflows](workflows.md)
Practice:

- Ask for a plan.
- Make one small edit.
- Run one verification command.
- Review diffs.

### Module 4: Verification mindset (60 minutes)

Read: [Verification and Rigor](verification.md)
Practice:

- Add one limiting-case check or synthetic-data test.
- Write down assumptions and units.

## Day 2: Use it on real science

### Module 5: A literature workflow (60 minutes)

Read: [Literature and Notes](literature.md)
Practice:

- Pick 2-3 papers.
- Create structured notes.
- Build a comparison table (assumptions, failure modes).

### Module 6: A reproducible analysis workflow (90 minutes)

Read: [Data Analysis](data-analysis.md)
Practice:

- Convert one notebook or script into a pipeline.
- Add a config file.
- Make "fresh clone -> one command" work.

### Module 7: Figures you can trust (60 minutes)

Read: [Figures and Tables](figures.md)
Practice:

- Add labels, units, and provenance.
- Add a lightweight sanity summary (counts, means, ranges).

### Module 8: Cost and multi-model usage (30 minutes)

Read:
- [Cost Control](cost-control.md)
- [Multi-Model Strategy](multi-model.md)

Goal:

- know when a second tool is worth paying for
- know how to avoid runaway usage

## Graduation criteria

You are "agentic AI fluent" when:

- you can define "done" as a command that passes
- you can read diffs and explain changes
- you can identify at least 3 ways an output could be wrong
- you have a reproducible workflow for one real project
