# Literature and Notes

This is an area where AI can help a lot, but it is also where it hallucinates the most.

## Safe approach

- Use AI to summarize papers you provide.
- Use AI to generate questions, hypotheses, and comparisons.
- Do not trust it to "know" the literature without sources.

## Good tasks

- "Summarize this paper in 10 bullets, then list 10 weaknesses."
- "Compare these two methods and tell me when each fails."
- "Extract all datasets, hyperparameters, and evaluation metrics."

## Bad tasks (unless you verify)

- "Give me citations for X"
- "What is the state of the art in Y" (without forcing sources)

## A workflow that works

1. Put PDFs in a folder.
2. Ask the agent to create structured notes per paper.
3. Ask for a synthesis across papers, explicitly citing which paper supports which claim.

## Output format suggestion

- One note per paper
- One synthesis note per topic
- A table of methods vs assumptions vs failure modes

## See also

- [Writing and Grants](writing.md)
- [Prompt Templates](prompts.md)
- [Verification and Rigor](verification.md)
