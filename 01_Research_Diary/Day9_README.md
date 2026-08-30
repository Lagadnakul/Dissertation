# Day 9 — README (Implementation Log)

**Goal for today:** Build and run the Blind Retry condition — retry the exact same prompt on all 8 failing tasks with zero new information — and measure whether pure repetition alone ever fixes anything.
**Status:** ✅ Complete. All 8 tasks in the failure pool have a definitive outcome.

---

## How to explain this to your professor in 2 minutes

> "We took the 8 tasks our model failed on Day 8 and simply asked it to try again — same prompt, same information, nothing new. This is the 'Blind Retry' baseline: the simplest possible recovery strategy, and roughly what many naive coding-agent systems do today when something fails. The result: 2 of the 8 tasks passed on retry — but both were tasks that had originally failed due to a broken patch format, not a wrong understanding of the bug. Not a single genuine logic failure was fixed by blind retry. This is meaningful evidence for our core argument: merely retrying can accidentally fix formatting noise through the model's natural randomness, but it has no power to fix an actual incorrect diagnosis of the bug. That's exactly the gap our Diagnose+Revise method is designed to close."

---

## What was done today

### 1. Built the Blind Retry generator
`day9_step1_blind_retry.py` re-ran the exact same prompt (same bug report, same real file content) for each of the 8 failing tasks — no diagnosis, no reflection, no information about what went wrong last time. This isolates the effect of pure resampling/randomness alone.

### 2. Hit and resolved two data gaps
- **`astropy-14182`**: returned an empty response again (`FinishReason.RECITATION`). Retried a second time to confirm this wasn't a one-off — **it blocked again, identically.** This is now a confirmed, stable finding: this specific task's fix is consistently blocked by the model's safety system, not a flaky result. Excluded from testing (no patch was ever produced), documented as its own outcome category.
- **`django-11019`**: hit a transient `503 UNAVAILABLE` (server overload) on the first pass — not a real result. Retried successfully afterward.

### 3. Ran evaluation across all 7 testable tasks
Used the same `run_id` (`day9_test`) across two evaluation calls so the harness skipped already-completed tasks and only tested what was newly added — an efficient, low-friction way to incrementally complete a batch.

---

## Final results table

| Task | Day 8 (original) | Day 9 (Blind Retry) | Changed? |
|---|---|---|---|
| astropy-7746 | Genuine logic FAIL | Still FAIL | No |
| django-11019 | Genuine logic FAIL | ERROR (malformed patch) | Changed failure type, still unresolved |
| django-11283 | Genuine logic FAIL | Still FAIL | No |
| django-11564 | Genuine logic FAIL | ERROR (malformed patch) | Changed failure type, still unresolved |
| astropy-14182 | Malformed patch ERROR | **Blocked (confirmed twice)** | Stable — permanent safety block, excluded |
| django-11039 | Malformed patch ERROR | **PASS** | ✅ Recovered |
| django-11583 | Malformed patch ERROR | **PASS** | ✅ Recovered |
| django-11620 | Malformed patch ERROR | Still ERROR | No |

**Recovery rate: 2 of 8 (25%).**

---

## The key finding (important — this is real evidence for your thesis)

**Blind Retry only ever recovered tasks that originally failed due to patch formatting, never a genuine logic failure.**

- 0 of 4 genuine logic failures were fixed by blind retry.
- 2 of 4 malformed-patch failures were fixed — purely by the natural randomness of the model producing a differently-formatted (and this time valid) output on a second try.
- 2 genuine logic failures actually *changed category* — flipping from "wrong logic" to "malformed patch" on retry, without ever becoming correct. This shows the model's output format itself has meaningful run-to-run variance, independent of whether its underlying reasoning is right.

**In plain words for your discussion section:** blind repetition can accidentally repair a formatting accident through chance alone, but demonstrates zero capacity to correct an actual wrong diagnosis of the bug. This is concrete, measured evidence that supports your central research gap — recovery requires *diagnosis*, not just *repetition*.

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day9_step1_blind_retry.py` | Generates blind retry attempts (no new info) | `06_Methodology/code/` |
| `day9_step1b_retry_missing.py` | Closes data gaps (503 error, safety-block re-confirmation) | `06_Methodology/code/` |
| `day9_step2_make_predictions_blindretry.py` | Builds predictions.json for the blind retry batch | `06_Methodology/code/` |
| `predictions_blindretry.json` | Final 7 evaluated predictions | `06_Methodology/code/` |
| `gemini-3.6-flash-blindretry-attempt2.day9_test.json` | Final evaluation report | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

1. **Empty response persisted on retry (`astropy-14182`)** — confirmed as a stable, repeatable safety-filter block rather than a one-off glitch. Documented as its own outcome category rather than force-retried further.
2. **Transient `503` server error (`django-11019`)** — not a real result; resolved with a simple retry.
3. **Reused the same `run_id` for incremental runs** — let the harness skip already-completed tasks automatically, avoiding redundant re-evaluation and saving time.

---

## Next step (Day 10)

Build and run the **Reflection-only** condition: on the still-unresolved tasks (`astropy-7746`, `django-11019`, `django-11283`, `django-11564`, `django-11620` — 5 tasks; `astropy-14182` remains excluded, `django-11039`/`django-11583` are already resolved and don't need further testing), ask the model to write a self-critique/reflection on its previous attempt before retrying — still no structured diagnosis of the actual test failure, just generic self-reflection. This is the second of your three recovery conditions, and sits between Blind Retry and your actual Diagnose+Revise contribution.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
