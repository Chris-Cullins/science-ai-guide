# Coding and Refactors

Agentic AI excels at the mechanical parts of coding—the parts that take time but don't require deep scientific judgment. This page covers how to use it effectively while keeping your science correct.

## What AI is genuinely good at

### Refactoring
Turning messy code into clean code without changing behavior. This is where AI shines brightest:
- Extracting functions from long scripts
- Renaming variables for clarity
- Reorganizing file structure
- Converting notebooks to modules

### Adding tests
Writing test cases for existing code:
- Unit tests for individual functions
- Integration tests for pipelines
- Edge case coverage
- Regression tests that catch future bugs

### Fixing errors
When you have a stack trace or error message:
- Diagnosing the root cause
- Proposing fixes
- Explaining why the error occurred

### Wiring up CLIs and configs
The boring but necessary plumbing:
- Adding command-line argument parsing
- Reading config files
- Setting up logging
- Handling input/output paths

### Documentation
Writing docstrings, README files, and usage examples from existing code.

## What AI is risky at

### Scientific logic
The agent does not understand your domain. It will happily:
- Change units without telling you
- Swap coordinate conventions
- Simplify equations incorrectly
- Remove "unnecessary" constants that matter

### Statistical choices
Choosing the right test, handling multiple comparisons, interpreting p-values—these require judgment the agent doesn't have.

### Novel algorithms
If you're implementing something new, the agent may confidently produce plausible-looking code that's subtly wrong.

## Your job as the human

For every coding task, define:

1. **What must not change** - scientific assumptions, core logic, validated results
2. **What should improve** - readability, reproducibility, performance, test coverage
3. **How you'll verify** - a test, a command, a comparison to known output

If you can't define these, the task isn't ready to delegate.

## Common coding tasks with prompts

### Clean up a messy script

```text
Refactor this script for readability and maintainability.

Rules:
- Do not change the scientific logic or numerical outputs
- Extract repeated code into functions
- Add type hints to function signatures
- Keep the same input/output behavior

Verification:
- Running the script with the same inputs produces identical outputs
- Show me the diff so I can review what changed
```

### Add tests to existing code

```text
Add tests for the functions in src/analysis.py.

Requirements:
- Use pytest
- Cover normal cases, edge cases, and at least one failure case
- Tests should run in under 5 seconds total
- Do not modify the original code unless necessary for testability

If you need to refactor for testability, propose the change first and explain why.
```

### Convert a notebook to a script

```text
Convert this Jupyter notebook into a reproducible Python script.

Requirements:
- Move all parameters to a config file or CLI arguments
- Remove interactive/exploratory code that isn't needed for the final result
- Add a main() function as the entry point
- Ensure outputs are identical to the notebook

Do not change any scientific logic. If you're unsure whether something is "exploratory" or "essential," ask.
```

### Fix a bug from a stack trace

```text
I'm getting this error:
[paste stack trace]

Context:
- The code is in [file path]
- It's supposed to [describe expected behavior]
- It fails when [describe when it fails]

Please:
1. Identify the root cause
2. Propose a fix
3. Explain why this error occurred
4. Suggest how to prevent similar bugs
```

### Speed up slow code

```text
This script takes too long to run. Profile it and suggest optimizations.

Constraints:
- Do not change outputs (results must be numerically identical)
- Prefer simple optimizations over clever ones
- If you suggest using a different library, explain the tradeoff

Show me the before/after timing for any changes you make.
```

### Add a CLI interface

```text
Add a command-line interface to this script.

Requirements:
- Use argparse (or click if you prefer)
- Required arguments: input_file, output_dir
- Optional arguments: --config, --verbose, --seed
- Include --help with clear descriptions
- Add a main() entry point that parses args and runs the analysis
```

## The refactor workflow

1. **Commit first** - make sure you can undo everything
2. **Define "same behavior"** - a test, a checksum, a comparison
3. **Ask for small changes** - one refactor at a time
4. **Verify after each change** - run the test before continuing
5. **Review the diff** - understand what changed

If a refactor breaks something, it's much easier to find the problem when changes are small.

## When to stop

Signs you're moving too fast:

- You can't explain what the agent changed
- You're approving diffs without reading them
- Tests are passing but you don't know why
- The code "looks cleaner" but you're not sure it's correct

Slow down. The goal is correct, maintainable code—not fast code.

## A safe refactor prompt

```text
Refactor this project for readability and reproducibility.

Constraints:
- Do not change scientific logic without asking
- Keep outputs identical unless you explain why they differ
- Make changes incrementally so I can review each step

Definition of done:
- `make test` passes
- `make figures` regenerates the main figures identically
- I can read the diff and understand every change
```

## See also

- [Verification and Rigor](verification.md)
- [Workflows (Plan-Do-Verify)](workflows.md)
- [Troubleshooting](troubleshooting.md)
