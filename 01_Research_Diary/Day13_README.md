# Day 13 — README (Implementation Log)

**Goal for today:** Consolidate all results from Days 8-12 into one final master table with core metrics - no new experiments, pure data consolidation.
**Status:** Complete. Verified accurate via manual sanity check.

---

## How to explain this to your professor in 2 minutes

> "Today we didn't run any new experiments - we pulled together everything we'd already measured across the baseline and all three recovery conditions into one master table, and calculated the headline numbers: 60% of tasks passed on the first attempt, 20% were genuine logic failures, and 20% were originally formatting failures. Of the genuine logic failures, none of our three recovery strategies fixed any of them. We then manually verified this table against the raw evaluation reports to make sure there were no transcription errors before treating these as our final numbers."

---

## What was done today

### 1. Built the master results table
`day13_master_results.py` consolidated results from six separate evaluation runs (Day 8 baseline, Day 9/12 Blind Retry, Day 10/12 Reflection-only, Day 11b Diagnose+Revise) into one clean table covering all 20 pilot tasks.

### 2. Computed core metrics
- Baseline: 12/20 PASS (60%), 4/20 genuine logic FAIL (20%), 4/20 malformed-patch ERROR (20%)
- Genuine logic failures recovered: 0/4 (0%) across all three conditions
- Malformed-patch cases: 1 permanently excluded, 2 resolved only under old tooling, 1 resolved and confirmed under reliable tooling across all three conditions

### 3. Documented scope honestly
Not every task was tested under every condition - some were skipped once already resolved (to save API quota), and one remains permanently excluded. This is recorded explicitly in the table rather than hidden.

### 4. Manually verified accuracy (sanity check)
Compared the master table against two raw evaluation report files:
- `gemini-3.6-flash-diagnoserevise-v2-searchreplace.day11b_tes.json` - resolved_ids: ["django__django-11620"] - matches exactly
- `gemini-3.6-flash-blindretry-attempt1.day8_test.json` - 12 resolved / 4 unresolved / 4 error task IDs - matches exactly

**Result: master table confirmed accurate, no transcription errors.**

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day13_master_results.py` | Builds the master table and computes metrics | `06_Methodology/code/` |
| `master_results.json` | Machine-readable final results | `06_Methodology/code/` |
| `master_results_table.md` | Paper-ready markdown table | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

None - this was a clean consolidation day using only data already collected and verified in prior days.

---

## Next step (Day 14)

Generate publication-ready charts from the master results, to visually summarize the findings for the paper's Results section.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*












Good research question → controlled methodology → reproducible implementation → trustworthy data → honest interpretation.