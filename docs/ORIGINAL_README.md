# Contract Clause Search Engine

A retrieval tool for locating potentially relevant clauses in long agreements. It returns source passages and relevance scores without making legal conclusions.

## Usage
```bash
pip install -r requirements.txt
python src/clause_search.py index sample_contracts --index-dir outputs/index
python src/clause_search.py search outputs/index "termination for material breach" --top-k 5
```

This project supports document review only. Contract interpretation should remain with qualified reviewers.
