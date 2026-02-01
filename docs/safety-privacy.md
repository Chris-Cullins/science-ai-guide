# Safety, Privacy, and Policy

This is the "don't get fired / don't leak data / don't fool yourself" page.

## Defaults (recommended)

- Don't put unpublished results, sensitive human-subject data, credentials, or embargoed material into any tool unless your institution explicitly allows it.
- Treat AI output as *untrusted* until you verify it.
- Prefer working in a repository with version control so you can review diffs.

## Data classification (simple version)

Default to these categories:

- Public: papers, public code, public datasets
- Internal: lab notes, non-public drafts, internal docs
- Sensitive: human-subject data, patient data, credentials, export-controlled data

Rule of thumb:

- Public is usually OK.
- Internal might be OK depending on your institution.
- Sensitive is usually NOT OK without explicit approvals and the right tooling.

## Secrets

Never paste:

- API keys
- passwords
- private tokens
- SSH keys

If the agent needs to access something, use environment variables or local config files that are not committed.

## Human oversight

## Human oversight

Even if agentic AI can do a lot, you still need to:

- inspect diffs
- run checks
- validate math and statistics
- verify citations and claims

## Citations and factual claims

Default rule:

- If you did not provide sources, assume citations can be wrong or invented.

Better pattern:

- Provide the PDFs or URLs.
- Ask the agent to quote and attribute specific claims to specific sources.

## Code execution safety

Agents can run commands. That is powerful and risky.

Safe defaults:

- run in a repo, not your whole home directory
- prefer throwaway copies for early experiments
- review commands before running if you do not recognize them

## Common failure modes

## Common failure modes

- Confident wrong answers (especially on niche domain facts)
- "Looks right" plots with incorrect preprocessing
- Silent changes in assumptions (units, coordinate conventions)
- Fake citations

## A simple policy for a lab

- No sensitive data in external tools.
- All code changes reviewed via diff.
- All key results reproducible via a one-command run.
- All citations verified.
