# LaTeX and Math with Agentic AI

Agentic AI tools can help a lot with LaTeX: drafting sections, formatting equations, cleaning up tables, and converting sketches into typeset math.

The key idea: models can read and write raw `.tex` files directly, and many "harnesses" can also accept images (screenshots, PDFs, whiteboard photos).

## What AI is good at

- Converting plain English into LaTeX prose
- Converting equations in text form into LaTeX math
- Cleaning up LaTeX formatting (environments, alignment, tables)
- Refactoring a messy preamble and macros (carefully)
- Turning rough notes into a clean derivation outline

## What AI is risky at

- Inventing steps in a derivation
- "Fixing" equations incorrectly while making them look nicer
- Producing plausible but wrong notation
- Adding citations or claims without sources

Your defense is the usual loop: diff + compile + sanity checks.

## Working with raw LaTeX

You can paste LaTeX directly into the agent or point it at a `.tex` file.

Good tasks:

- "Rewrite this paragraph for clarity but keep the math and meaning unchanged."
- "Turn this inline equation into a properly aligned display equation."
- "Make this table readable and consistent with the paper style."

## Image -> LaTeX (whiteboard, screenshots, PDFs)

Many AI interfaces can accept images.

Practical workflow:

1. Write an equation on a whiteboard (or notebook).
2. Take a photo.
3. Give the image to the tool (or save it into your project folder).
4. Ask the agent to convert it into LaTeX.

Notes:

- If the tool cannot accept images directly, you can often still do this by saving the image and giving the agent the file path.
- Always verify the result. OCR + math parsing is good, but not perfect.

## A minimal compile loop

If you have a local TeX install:

```bash
latexmk -pdf main.tex
```

If you do not, consider Overleaf as the simplest path.

## Prompt templates

### 1) Convert a whiteboard equation to LaTeX (with verification)

```text
I am going to provide an image of a handwritten equation.

Task:
- Convert the equation into LaTeX.
- If any symbols are ambiguous, list the ambiguity and provide 2-3 possible interpretations.
- Output both:
  1) a standalone LaTeX equation
  2) the same equation inside an `align` environment

Rules:
- Do not "fix" the math.
- Preserve the structure as written.
```

### 2) Clean up a derivation without changing meaning

```text
I will provide a LaTeX snippet.

Goal:
- Improve readability and formatting.

Constraints:
- Do not change the meaning.
- Do not change variable names unless you ask.

Definition of done:
- It compiles.
- The math is structurally identical.
```

### 3) Turn rough notes into a paper-ready subsection

```text
Turn these rough notes into a LaTeX subsection.

Constraints:
- Do not add citations.
- Do not invent results.
- If a claim is not supported by what I provided, mark it as "needs source".

Deliverable:
- LaTeX text using standard environments (equation/align, itemize).
```

## Recommended habits

- Keep equations close to the code that generated results (where applicable).
- Use consistent notation; ask the agent to build a notation table.
- Compile frequently.
- When the math is important, cross-check with a second method (manual check, symbolic tool, or a second model).
