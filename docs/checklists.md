# Checklists

These are the habits that make agentic AI safe and useful.

## Pre-flight (before you delegate)

- Is the data allowed to be shared with this tool?
- Is the task small enough to review?
- Do you have a definition of done?
- Do you have a verification command or sanity check?
- Is the project under version control?

## During flight (while the agent works)

- Ask for a plan before large edits.
- Keep changes in small steps.
- Require it to explain assumptions and units.
- Stop if you do not understand what changed.

## Post-flight (before you trust results)

- Review diffs.
- Run tests / scripts.
- Check units, limiting cases, and basic invariants.
- Verify citations manually.
- Record how to reproduce the result.

## Red flags

- "It should work" without running anything
- new citations you did not provide
- big refactors without tests
- plots with missing units or unclear preprocessing

## See also

- [Verification and Rigor](verification.md)
- [Workflows (Plan-Do-Verify)](workflows.md)
- [Troubleshooting](troubleshooting.md)
