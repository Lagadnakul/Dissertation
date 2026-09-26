# data/

| Path | Committed | What it is |
| --- | --- | --- |
| `swebench_lite.jsonl` | ✅ yes | the frozen task set — 300 instances, one JSON object per line, sorted by `instance_id` |
| `swebench_lite.meta.json` | ✅ yes | the upstream revision sha, row count, field list, per-repo counts, export timestamp |
| `cache/` | ❌ no | fetched repo source files, keyed by `repo@commit:path` |
| `runs/` | ❌ no | `<date>_<config>/` — one directory per sweep, the cell ledger and row output |

## Why the task set is committed

`swebench_lite.jsonl` is 3.5M of text and it is **the independent variable of
the whole study**. Committing it freezes the exact 300 problems to one file
whose hash can be checked, instead of re-fetching a dataset that may have been
revised upstream between runs. `swebench_lite.meta.json` records the revision it
came from:

```
princeton-nlp/SWE-bench_Lite  default/test
revision 6ec7bb89b9342f664a54a6e0a6ea6501d3437cc2
```

Regenerate with:

```sh
bun scripts/export_dataset.ts
```

The script refuses to write unless upstream reports exactly 300 rows and all
nine required fields are present, so a silent upstream change becomes a loud
failure.

## Composition

300 instances across **12 repositories** — not 11, which is what the design docs
said before this export measured it:

| n | repo |
| --- | --- |
| 114 | django/django |
| 77 | sympy/sympy |
| 23 | matplotlib/matplotlib |
| 23 | scikit-learn/scikit-learn |
| 17 | pytest-dev/pytest |
| 16 | sphinx-doc/sphinx |
| 6 | astropy/astropy |
| 6 | psf/requests |
| 6 | pylint-dev/pylint |
| 5 | pydata/xarray |
| 4 | mwaskom/seaborn |
| 3 | pallets/flask |

This distribution is why stratified sampling (§8.3) matters: django alone is 38%
of the benchmark, and Nakul's original 20-task pilot drew only django and
astropy. A uniform random 60 would still be django-dominated. The `≥3 per repo`
floor in `configs/base.yaml` is set against the smallest repo here — flask, with
3 — so every repo is representable without oversampling.
