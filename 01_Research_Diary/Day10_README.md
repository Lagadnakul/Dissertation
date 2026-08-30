# Day 10 — README (Implementation Log)

**Goal for today:** Build and run the Reflection-only condition — show the model its own previous failed attempt and ask it to critique and revise it, without any external information about what the real test actually showed.
**Status:** ✅ Complete. All 5 tasks accounted for. Recovery rate: 0/5.

---

## How to explain this to your professor in 2 minutes

> "Today we tested whether letting the model reflect on its own previous mistake — without telling it what the real test actually said — could fix the bugs that survived blind retry. It couldn't. Zero of the 5 remaining failures were fixed. Combined with yesterday's blind retry result, we now have a clean pattern across two different naive recovery strategies: neither pure repetition nor self-critique-without-evidence can fix a genuine logic error. This strongly motivates our actual contribution — giving the model the real test failure output, not just letting it guess at its own mistake."

---

## What was done today

### 1. Built the Reflection-only generator
`day10_step1_reflection_only.py` showed the model, in a single combined prompt: the bug report, the real file content, and its own **original Day 6/7 attempt** (not the blind retry one) — explicitly told this attempt failed — then asked for a self-critique (`REFLECTION:`) followed by a revised patch. No external test output or error message was given; the model could only guess at its own mistake.

### 2. Ran evaluation on the 5 still-unresolved tasks
```
python3 -m swebench.harness.run_evaluation --dataset_name SWE-bench/SWE-bench_Lite --predictions_path predictions_reflectiononly.json --max_workers 2 --run_id day10_test
```
Result: 0 resolved, 3 genuine FAIL, 2 malformed-patch ERROR. All 5 accounted for cleanly, no data gaps this time.

---

## Full comparison table (all 3 conditions so far)

| Task | Day 8 (baseline) | Day 9 (Blind Retry) | Day 10 (Reflection-only) |
|---|---|---|---|
| astropy-7746 | FAIL | FAIL | FAIL |
| django-11019 | FAIL | ERROR (malformed) | ERROR (malformed) |
| django-11283 | FAIL | FAIL | FAIL |
| django-11564 | FAIL | ERROR (malformed) | FAIL (flipped back) |
| django-11620 | ERROR | ERROR | ERROR |

**Reflection-only recovery rate: 0/5.**

---

## The key finding (important — write this down)

**Across two different naive recovery strategies (Blind Retry and Reflection-only), zero genuine logic failures have been fixed.** This is a clean, repeated, unambiguous pattern, not noise:

- Blind Retry: 0/4 genuine logic failures fixed (only accidentally fixed formatting errors)
- Reflection-only: 0/5 fixed (same tasks, still zero)

**In plain words:** letting the model reflect on its own mistake, without telling it what actually went wrong according to the real test, is functionally no better than not reflecting at all. The model is guessing at its own error in the dark — it has no way to verify whether its self-critique is even correct, since it never sees the ground truth of what the test actually reported.

**This directly motivates Day 11.** The one variable neither Blind Retry nor Reflection-only has tested yet is: *what happens when the model is shown the actual, real test failure output instead of guessing?* That's exactly what Diagnose+Revise (your core contribution) tests.

## Secondary pattern worth noting

`django-11564` flipped from ERROR (Day 9) back to FAIL (Day 10), while `django-11019` stayed ERROR across both. This reinforces the Day 9 observation: **patch formatting reliability shows real run-to-run variance in this model**, somewhat independent of which recovery strategy is applied — worth a sentence in your paper's discussion of threats to validity.

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day10_step1_reflection_only.py` | Generates reflection + revised attempt (single combined call) | `06_Methodology/code/` |
| `day10_step2_make_predictions_reflection.py` | Builds predictions.json for the reflection batch | `06_Methodology/code/` |
| `predictions_reflectiononly.json` | 5 evaluated predictions | `06_Methodology/code/` |
| `gemini-3.6-flash-reflectiononly-attempt3.day10_test.json` | Evaluation report | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

None — this was the first fully clean run in the project, with no data gaps, no missing tasks, and no infrastructure hiccups. All prior fixes (WSL, Docker integration, tolerant extraction) held steady.

---

## Next step (Day 11)

Build and run **Diagnose + Revise** — your actual research contribution. Instead of self-guessed reflection, feed the model the REAL test failure evidence (actual pytest output for genuine failures, actual patch-apply error text for malformed-patch failures) pulled directly from the evaluation logs, and ask it to diagnose the specific root cause before revising. This is the first condition that gives the model real, verifiable ground truth about its own mistake.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
