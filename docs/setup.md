# Setup Checklist

This page is intentionally practical.

## Accounts and billing

- Pick one primary tool (recommendation: Claude Code).
- Decide who pays: you personally vs lab vs institution.
- Turn on billing alerts where possible.

## Local machine basics

Minimum you want:

- a terminal you are comfortable using
- Python (or your language) installed
- a way to create isolated environments (venv/conda)
- git installed

## Project hygiene (do this once)

- Put the project in a repo (git).
- Add a `README.md` with setup and the "one command" run.
- Add a `Makefile` or similar task runner.
- Add a tiny test / sanity check.

## Your first guardrails

In your first sessions, make these rules explicit:

- propose a plan before editing
- keep changes small and reviewable
- run verification commands
- do not add citations or claims you cannot verify

## If you are in a regulated environment

Stop and get clarity on:

- human-subject data rules
- patient/clinical data policies
- export controls / ITAR
- data retention and sharing policies

Default safe policy: do not paste sensitive data into any external tool.
