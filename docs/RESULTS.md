# Execution record — Contract Clause Search Engine

**Status:** Local execution completed using bundled fixtures.  
**Python:** 3.13.5  
**Execution time:** 6.67 seconds in the packaging environment (not a standardized benchmark).  
**Method:** `python src/clause_search.py index sample_contracts --index-dir outputs/index`, `python src/clause_search.py search outputs/index "termination for material breach" --top-k 5`

## Observed output

![Observed output](../assets/result.svg)



**Raw output:** [execution.txt](../results/execution.txt)  
**Command records and SHA-256 digests:** [execution.json](../results/execution.json)

## Interpretation

Results were computed on the included test fixtures. They demonstrate one successful invocation, not measured generalization, comparative performance, system availability or operational readiness. If the fixtures or application are synthetic, values remain synthetic or simulated.
