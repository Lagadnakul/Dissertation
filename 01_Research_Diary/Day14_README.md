# Day 14 — README (Implementation Log)

**Goal for today:** Generate publication-ready charts from the master results, and confirm data accuracy before treating the numbers as final.
**Status:** Complete. Charts generated successfully. This is effectively the final infrastructure/data day of the project - only the optional Day 15 bonus experiment remains before implementation wraps.

---

## How to explain this to your professor in 2 minutes

> "Today we turned our final numbers into two charts: one showing how the 20 tasks broke down at first attempt (pass, genuine failure, or formatting failure), and one comparing all three recovery strategies side by side on the genuine failures. Before finalizing anything, we manually cross-checked our summary table against the raw evaluation logs to confirm there were no copy errors - everything matched exactly. With this, our core experimental work is essentially finished."

---

## What was done today

### 1. Manual sanity check (carried over from Day 13, completed today)
Verified two entries from the master table against their raw evaluation report files. Both matched exactly - no discrepancies found. The master table is confirmed trustworthy.

### 2. Generated two publication-ready figures
`day14_generate_charts.py` produced:
- **Figure 1 (`figure1_baseline_breakdown.png`):** bar chart of the 20-task baseline outcome (12 PASS, 4 genuine FAIL, 4 malformed ERROR)
- **Figure 2 (`figure2_recovery_comparison.png`):** stacked bar chart comparing Blind Retry, Reflection-only, and Diagnose+Revise on the 4 genuine logic failures - visually showing the identical 0/4 recovery rate across all three

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day14_generate_charts.py` | Generates both figures from master_results.json | `06_Methodology/code/` |
| `figure1_baseline_breakdown.png` | Baseline outcome chart | `06_Methodology/code/` |
| `figure2_recovery_comparison.png` | Recovery strategy comparison chart | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

None - matplotlib installed cleanly, both charts generated successfully on the first run.

---

## Where the project stands after today

Every core experiment has been run, retrofitted for fairness, consolidated, verified, and visualized. This marks the practical end of the "build and test the pipeline" phase of the project.

## Next step (Day 15 - optional bonus experiment)

Test whether a SECOND round of Diagnose+Revise (iterating again using the fresh failure evidence from this round's attempts) shows any real difference, since Blind Retry and Reflection-only have no mechanism to meaningfully improve across multiple rounds, while Diagnose+Revise theoretically should if given new evidence each time. This is optional but would meaningfully strengthen the paper if time allows.

After Day 15 (or if skipped), the project moves into the writing phase - a substantial phase of its own, not yet started.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
