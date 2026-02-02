# Data Analysis (AI-Assisted)

AI can help you write analysis code quickly. The risk is silent wrongness.

## What to insist on

- a minimal reproducible script
- a config file for parameters
- sanity checks on shapes, units, and ranges
- deterministic outputs (seeded randomness)

## Typical wins

- cleaning up messy scripts
- turning notebooks into pipelines
- adding tests and validations
- speeding up plotting and reporting

## Typical traps

- incorrect joins / merges
- wrong filtering
- subtle unit conversions
- plotting post-processed data without recording steps

## Common pitfalls in pandas / numpy code

AI-generated data analysis code often introduces subtle bugs. Watch for:

**Indexing and alignment:**
- Mixing `.loc` and `.iloc` incorrectly
- Losing index alignment after operations
- Off-by-one errors in slicing

**Data types:**
- Silent type coercion (strings to numbers, floats to ints)
- Datetime parsing assumptions (timezone, format)
- Categorical vs string confusion

**Missing data:**
- `NaN` propagation in calculations
- `dropna()` applied too broadly or too narrowly
- Filling missing values with inappropriate defaults

**Aggregation:**
- `groupby` dropping groups unexpectedly
- Wrong aggregation function (mean vs sum vs count)
- Multi-index confusion after groupby

**Joins and merges:**
- Wrong join type (inner vs outer vs left)
- Duplicate rows from many-to-many joins
- Key column mismatches (whitespace, case, type)

## Validation patterns for statistical code

Before trusting any statistical result:

1. **Check shapes**: Print `.shape` before and after every transformation.
2. **Check ranges**: Are values in expected bounds? Any negative values where there should not be?
3. **Check distributions**: Quick histograms or `.describe()` to catch anomalies.
4. **Synthetic data test**: Run on data where you know the answer.
5. **Limiting cases**: What happens with N=1, N=0, all identical values?

## When to use SQL vs DataFrames

**Prefer SQL when:**
- Data is already in a database
- Joins are complex and well-defined
- You want the database to optimize the query plan
- Reproducibility is easier (query is a string you can save)

**Prefer DataFrames when:**
- Data is in files (CSV, Parquet, etc.)
- You need iterative, exploratory analysis
- Custom transformations are easier in Python/R
- Integration with plotting and modeling libraries

## A practical definition of done

- "Fresh clone -> install deps -> run one command -> produces figure/table"

## Example: notebook to pipeline prompt

```text
Convert this Jupyter notebook into a reproducible pipeline.

Requirements:
1. Extract all parameters into a config file (YAML or JSON).
2. Create a single entry-point script that:
   - Loads the config
   - Runs the analysis
   - Saves outputs to a predictable location
3. Add shape/sanity checks after each major step.
4. Pin dependencies in requirements.txt.
5. Ensure outputs are identical to the notebook (or explain differences).

Do not change the scientific logic without asking.
```

## See also

- [Figures and Tables](figures.md)
- [Reproducibility](reproducibility.md)
- [Verification and Rigor](verification.md)
