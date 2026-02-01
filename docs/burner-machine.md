# Burner Machine and Sandboxes

Do you need a "burner machine"?

Usually: no.
Sometimes: yes.

This page is a practical way to think about risk.

## What people mean by "burner"

- A dedicated laptop or desktop used for AI-assisted work
- A separate OS account
- A VM (virtual machine)
- A cloud dev environment

The point is to reduce blast radius:

- fewer sensitive files accessible
- fewer saved credentials in browsers
- less risk if you mis-click "yes" on something

## When you should consider it

- You routinely handle sensitive human-subject or clinical data.
- You have export-controlled or proprietary data.
- Your institution has strict compliance requirements.
- You want to try agentic tools before you trust them.

## Lightweight option (recommended for most)

1. Create a dedicated folder for AI-assisted projects.
2. Use a separate browser profile for AI tools.
3. Keep secrets out of repos.
4. Work in copies of projects until you trust the workflow.

## Stronger option: separate OS user

- Create a new user account on your machine.
- Use it only for agentic AI work.
- Do not sign into personal email or password managers there.

## Strongest option: VM or cloud environment

- Use a VM (or a cloud dev box) that contains only the project.
- Destroy and recreate when you are done.

This is higher effort, but it is clean.

## The bigger win: permissions discipline

Even with a burner machine, you still need:

- diffs
- verification
- no secrets in prompts

Burner setups reduce risk. They do not replace good habits.
