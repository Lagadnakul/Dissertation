# Day 6 — README (Implementation Log)

**Goal for today:** Stop testing one bug by hand — build a repeatable pipeline and run it across a small pilot batch of 5 real tasks, producing a real results table.
**Status:** ✅ Complete — all 5 tasks accounted for. 4/5 evaluated (all PASS), 1/5 blocked by the model's own safety system before it could even produce a fix.

---

## How to explain this to your professor in 2 minutes

> "Today we scaled our single-task pipeline to run automatically across 5 real bugs instead of one. We introduced a standard simplification from the SWE-bench paper itself, called 'oracle file localization' — instead of building a full repository-search system, we extract which file needs editing from the task's own metadata and let the model generate its own fix for that file from scratch. Out of 5 tasks, 4 fixes passed the real test suite. The 5th task never even produced a fix — Google's AI safety system blocked the response because it detected the output too closely matched existing, known code (the real fix is public on GitHub, so the model's training data likely already contains it verbatim). This is a genuinely useful finding for our research: it's a third type of failure — not a wrong fix, not a broken patch format, but the model refusing to answer at all — and it's worth reporting honestly rather than hiding."

---

## What was done today

### 1. Built a repeatable batch pipeline
Instead of manually running one task through 5+ separate script calls, built:
- `day6_step1_generate_batch.py` — automatically fetches the real file and generates a fix for 5 pilot tasks in one run
- `day6_step2_make_predictions_batch_v2.py` — combines all attempts into one `predictions_batch1.json`, with automatic diff-formatting fixes carried over from Day 5
- `day6_step3_show_results.py` — reads the harness's report and prints a clean PASS/FAIL table instead of raw JSON

### 2. Adopted "oracle file localization" (a documented, legitimate simplification)
To know which file to fetch for each new task (without a full repository-search system), we extract the file path(s) from the task's own gold-patch metadata — just the filename, never the actual fix content. This is the same simplification used in the original SWE-bench paper's "Oracle" evaluation setting, so it's a citable, standard choice, not something invented ad hoc. **Limitation to note in the paper:** this means our current pipeline isn't yet tested on the harder problem of finding the right file in a large repository — that remains future work or a stated scope boundary.

### 3. Ran the batch — found 2 tasks missing from the first result
First run only produced results for 3 of 5 tasks. Investigated rather than assuming it was fine:
- **`astropy-6938`**: the model wrote a valid patch but didn't wrap it in the expected ` ```diff ` code fence, so the extraction script silently missed it. **This was our bug, not the model's fault.** Fixed by making the extraction logic tolerate patches with or without a fence.
- **`astropy-14182`**: the saved file was completely empty (0 characters).

### 4. Diagnosed the empty file — a real, citable finding
Regenerated this task with debug logging added, which revealed:
```
finish_reason: FinishReason.RECITATION
Response length: 0 characters
```
**In plain words:** the model didn't fail to solve the bug — it never tried, because Google's safety system detected its intended output was too similar to existing, known text (very plausibly the real, public fix for this exact bug, which likely exists in the model's training data) and blocked the response entirely to avoid reproducing it.

---

## Final results table (all 5 tasks, honestly reported)

| Task ID | Result |
|---|---|
| astropy__astropy-12907 | PASS |
| astropy__astropy-14182 | **BLOCKED** — model refused to respond (RECITATION safety filter) |
| astropy__astropy-14365 | PASS |
| astropy__astropy-14995 | PASS |
| astropy__astropy-6938 | PASS |

**4 of 5 evaluated tasks passed. 1 of 5 never produced a testable output at all.**

---

## Why this matters for the paper (write this down)

This gives us a third distinct outcome category, alongside the two from Day 4-5:

| # | Category | Example |
|---|---|---|
| 1 | Malformed patch (broken diff syntax) | Day 3/4, blind attempt |
| 2 | Valid patch, wrong context/logic | Day 4/5 investigation |
| 3 | **Model refuses to respond (safety block)** | Day 6, astropy-14182 |

A complete failure taxonomy for AI coding agents needs to account for all three — not just "did the fix work," but "did the model even produce a testable fix in the first place."

**Honest caveat about the high pass rate (4/4 = 100%):** this is very likely inflated by the "oracle file localization" simplification — we handed the model the exact correct file, removing the hardest real-world part of the task (finding the right file in a large repository). A future version of this pipeline that removes this simplification would likely show a lower, more realistic pass rate. Note this explicitly as a scope limitation.

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day6_step1_generate_batch.py` | Generates fixes for 5 pilot tasks automatically | `06_Methodology/code/` |
| `day6_step1b_regenerate_missing.py` | Regenerates a specific failed/empty task, with debug info | `06_Methodology/code/` |
| `day6_step2_make_predictions_batch_v2.py` | Builds predictions.json, tolerant of missing code fences | `06_Methodology/code/` |
| `day6_step3_show_results.py` | Prints a clean PASS/FAIL table from the harness report | `06_Methodology/code/` |
| `predictions_batch1.json` | Final batch of 4 evaluated predictions | `06_Methodology/code/` |
| `gemini-3.6-flash-blindretry-attempt1.day6_test2.json` | Final evaluation report | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

1. **Silent extraction failure (astropy-6938)** — patch wasn't wrapped in a code fence, so the regex missed it entirely without any error message. Fixed by adding a fallback extraction path that works with or without fences.
2. **Empty attempt file (astropy-14182)** — traced to a `FinishReason.RECITATION` safety block, not a bug in our code. Documented as a genuine finding rather than force-fixed.

---

## Next step (Day 7)

Now that a clean single-attempt pipeline works across multiple tasks, Day 7 adds the actual comparison logic:
1. **Blind Retry baseline**: on failure, retry the exact same prompt again (no new information) — measure if blind repetition ever helps.
2. **Reflection-only baseline**: on failure, ask the model to reflect on what might be wrong (generic self-critique, no structured diagnosis) before retrying.
3. **Diagnose + Revise (our method)**: on failure, feed back the actual test error/output, ask for a structured diagnosis of the specific cause, then revise.

This is where the real 3-way comparison — the core of the research contribution — starts taking shape.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*