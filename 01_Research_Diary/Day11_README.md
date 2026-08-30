# Day 11 — README (Implementation Log)

**Goal for today:** Build and run Diagnose + Revise - your core research contribution - feeding the model REAL test failure evidence instead of guesswork, and measure whether it can fix genuine logic failures that Blind Retry and Reflection-only could not.
**Status:** Complete, with a major methodological correction made mid-day. Result: 1/5 recovered (a formatting-only case), 0/4 genuine logic failures recovered on this first attempt.

---

## How to explain this to your professor in 2 minutes

> "Today we tested our core method: showing the model the real test failure output and asking it to diagnose the specific cause before revising. The first attempt used the standard unified-diff format and failed completely - all 5 patches were malformed and couldn't even be applied, regardless of whether the underlying reasoning was correct. We diagnosed this as a structural problem: asking an LLM to compute exact line numbers is inherently unreliable. We fixed it by switching to a SEARCH/REPLACE format - the model shows exact original code and its replacement, with no line numbers at all - and we generate the actual diff ourselves in Python, guaranteeing it's always valid. This completely eliminated malformed patches: 5 out of 5 applied cleanly. One task, which had originally failed only due to bad formatting, now passed. However, the 4 tasks that were genuine logic failures still failed even with real test evidence and a working patch mechanism. This is an honest, real result: on this small sample, single-shot diagnosis-and-revise doesn't yet solve the hardest bugs, but we've cleanly separated 'the model can't format its answer' from 'the model's reasoning is wrong' - which is itself a meaningful contribution, since most existing evaluations conflate the two."

---

## What was done today

### 1. First attempt - unified diff format (failed completely)
`day11_step1_diagnose_revise.py` fed the model real test evidence (actual pytest output for genuine failures, actual patch-apply errors for formatting failures) collected via `day11_step0_collect_evidence.py`, and asked for a diagnosis + a standard unified diff.

**Result: 5/5 tasks returned ERROR - every single patch was malformed and could not be applied**, regardless of whether the diagnosis itself was sound. This blocked any real conclusion about whether diagnosis helps.

### 2. Hit a new infrastructure constraint: per-minute token limit
Partway through generation, hit `429 RESOURCE_EXHAUSTED` on `generate_content_free_tier_input_token_count` - a separate, per-minute cap (250,000 tokens/minute), distinct from the daily 20-request cap seen earlier. Caused by these prompts being much larger (full file + previous attempt + real test evidence). Resolved by retrying with longer pauses (60s) between calls and truncating long evidence text to its most informative final ~3000 characters.

### 3. Root-caused the malformed-patch problem and rebuilt the mechanism
Recognized that the repeated malformed-patch failures across nearly every day of this project (Day 6 through Day 11) share one root cause: asking an LLM to compute exact line numbers and hunk headers is inherently unreliable, independent of whether its actual code reasoning is correct.

**Fix:** rebuilt the generation step (`day11b_diagnose_revise_searchreplace.py`) to ask the model for SEARCH/REPLACE blocks instead - exact original code and its replacement, no line numbers at all (the same approach used by real tools like Aider). The actual find-and-replace is performed in Python against the real file content already fetched, and the final unified diff is generated programmatically with `difflib` - guaranteed syntactically valid every time, since a computer (not the model) is doing the line counting.

### 4. Re-ran with the new mechanism - complete success at the formatting level
```
python3 -m swebench.harness.run_evaluation --dataset_name SWE-bench/SWE-bench_Lite --predictions_path predictions_diagnoserevise_v2.json --max_workers 2 --run_id day11b_tes
```
**Result: 5/5 patches applied cleanly, 0 errors.** The malformed-patch failure category was completely eliminated.

---

## Final results table (using the corrected SEARCH/REPLACE mechanism)

| Task | Original type (Day 8) | Diagnose+Revise (v2) result |
|---|---|---|
| astropy-7746 | Genuine logic FAIL | Still FAIL |
| django-11019 | Genuine logic FAIL | Still FAIL |
| django-11283 | Genuine logic FAIL | Still FAIL |
| django-11564 | Genuine logic FAIL | Still FAIL |
| django-11620 | Malformed patch ERROR | PASS |

**Recovery rate on genuine logic failures: 0/4. Recovery rate overall: 1/5 (the one formatting-only case).**

---

## The key finding (important - write this down precisely)

**Even with real, ground-truth test failure evidence and a fully reliable patch mechanism, this model could not fix any of the 4 genuine logic failures on a single diagnose-and-revise attempt.** This matches the 0/4 result from both Blind Retry and Reflection-only - meaning, across all three conditions tested so far, no recovery strategy has fixed a genuine logic failure in this sample.

**This is a legitimate, citable, honestly-reported finding - not a failed experiment.** It demonstrates two separate things clearly:
1. **Patch-formatting reliability and reasoning correctness are independent failure modes.** Fixing the tooling (SEARCH/REPLACE) recovered exactly the one task whose real problem was formatting, and nothing else - proof that the fix targeted the right layer.
2. **Single-shot diagnosis, even grounded in real evidence, has a limit.** These 4 remaining bugs may require deeper repository context (this pipeline still only shows one file), multiple iterative attempts, or fundamentally different reasoning support to solve - a natural, well-motivated direction for future work or an additional experiment if time permits (a second revision round).

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day11_step0_collect_evidence.py` | Pulls real test/patch-error evidence from Day 8 logs | `06_Methodology/code/` |
| `day11_step1_diagnose_revise.py` | First attempt (unified diff format) - superseded | `06_Methodology/code/` |
| `day11_step1b_retry_missing.py` | Retry helper for the per-minute token limit | `06_Methodology/code/` |
| `day11b_diagnose_revise_searchreplace.py` | Final, working mechanism (SEARCH/REPLACE + programmatic diff) | `06_Methodology/code/` |
| `predictions_diagnoserevise_v2.json` | Final 5 predictions, all validly formatted | `06_Methodology/code/` |
| `apply_log_v2.json` | Per-task log of how each SEARCH/REPLACE edit was applied | `06_Methodology/code/` |
| `gemini-3.6-flash-diagnoserevise-v2-searchreplace.day11b_tes.json` | Final evaluation report | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

1. **100% malformed-patch rate under unified diff format** - root-caused as a structural LLM limitation (unreliable line-number computation), not a prompt-wording issue. Resolved by switching to SEARCH/REPLACE + programmatic diff generation.
2. **Per-minute input token quota** (separate from the daily request quota) - resolved with longer pacing (60s) and evidence truncation.
3. **Run-id typo** (`day11b_tes` vs `day11b_test`) caused a file-not-found error when viewing results - resolved by matching the exact filename actually produced.

---

## Important note for Day 12

**Blind Retry (Day 9) and Reflection-only (Day 10) were tested using the old, unreliable unified-diff format.** Their malformed-patch cases may have been masking correct fixes, the same way `django-11620` was here. These need to be retested using the same SEARCH/REPLACE mechanism before any final 3-way comparison can be considered fair.

## Next step (Day 12)

Retrofit Blind Retry and Reflection-only with the SEARCH/REPLACE mechanism - specifically re-testing only the tasks that failed due to malformed patches under the old method (not tasks that already cleanly failed on real content, which aren't affected by the tooling change) - then produce the final, fair, apples-to-apples 3-condition comparison table.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
