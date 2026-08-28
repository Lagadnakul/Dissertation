# Day 7 — README (Implementation Log)

**Goal for today:** Scale the pipeline from 5 tasks to 20 tasks, and identify the real "failure pool" — the subset of tasks that don't succeed on the first try. This pool is what the actual recovery-method comparison (Blind Retry vs. Reflection-only vs. Diagnose+Revise) will run on.
**Status:** ✅ Core goal achieved. 14/20 tasks fully tested. 6/20 pending — blocked by a free-tier daily API quota, not by any bug. Resumes automatically once the quota resets.

---

## How to explain this to your professor in 2 minutes

> "We scaled our pipeline from testing 1 bug to testing 20 real bugs automatically, across two different open-source projects (astropy and Django). Of the 14 we were able to fully test today, 10 passed on the first attempt and 4 failed in two distinct ways — one genuine logic failure, and three malformed-patch failures. That roughly 29% failure rate is actually a good outcome for our research: it means there are enough real failures to meaningfully test whether our recovery method helps, without needing to artificially search for harder bugs. The remaining 6 tasks are paused because we hit Google's free-tier daily limit of 20 requests — a real, expected constraint of doing this research on a zero-cost budget, and one we're documenting explicitly rather than hiding, since it's a legitimate practical limitation worth stating in the methodology section."

---

## What was done today

### 1. Scaled the pipeline from 5 to 20 tasks
Extended Day 6's single-attempt pipeline (`day7_step1_generate_full_pilot.py`) to run across the first 20 SWE-bench Lite tasks instead of 5, spanning multiple repositories (astropy, Django). Kept the "oracle file localization" approach from Day 6 (extracting the target file from the task's own gold-patch metadata, not its content).

### 2. Hit and diagnosed a real infrastructure constraint: the free-tier daily quota
After roughly 20 total API calls in one day (including reused attempts from earlier days), every further request returned:
```
429 RESOURCE_EXHAUSTED - Quota exceeded for metric: generate_content_free_tier_requests, quotaValue: '20'
```
**This is a hard daily cap on Gemini's free tier for this model** — not a bug, not something fixable by retrying immediately. Confirmed by retrying later in the day and getting the identical error again, meaning the quota window hadn't reset yet.

**Six tasks remain un-generated as a direct result:** `astropy-7746`, `django-11099`, `django-11283`, `django-11422`, `django-11564`, `django-11620`. These are marked `BLOCKED (no_attempt_file)` in today's results table — not failures of the model, simply not-yet-attempted.

### 3. Hit and resolved a second Docker connectivity issue (WSL-specific)
Docker briefly became unreachable again (`Connection aborted... No such file or directory`) after switching to WSL. Resolved by confirming WSL Integration was enabled in Docker Desktop's settings (Settings → Resources → WSL Integration) and restarting Docker Desktop.

### 4. Ran evaluation on all 14 available attempts
```
python3 -m swebench.harness.run_evaluation --dataset_name SWE-bench/SWE-bench_Lite --predictions_path predictions_pilot20.json --max_workers 2 --run_id day7_test
```
All 14 completed cleanly (no crashes, no CRLF issues — WSL fix from Day 5 holding steady).

### 5. Built the results table and failure pool
```
python3 day7_step3_extract_failure_pool.py gemini-3.6-flash-blindretry-attempt1.day7_test.json
```

---

## Full results table (as of today)

| Task ID | Result |
|---|---|
| astropy__astropy-12907 | PASS |
| astropy__astropy-14365 | PASS |
| astropy__astropy-14995 | PASS |
| astropy__astropy-6938 | PASS |
| django__django-10914 | PASS |
| django__django-10924 | PASS |
| django__django-11001 | PASS |
| django__django-11049 | PASS |
| django__django-11133 | PASS |
| django__django-11179 | PASS |
| django__django-11019 | **FAIL** (genuine logic failure — real test candidate for recovery) |
| astropy__astropy-14182 | **ERROR** (malformed patch — patch apply failure) |
| django__django-11039 | **ERROR** (malformed patch — "only garbage found in patch input") |
| django__django-11583 | **ERROR** (malformed patch — patch apply failure) |
| astropy__astropy-7746 | PENDING (quota) |
| django__django-11099 | PENDING (quota) |
| django__django-11283 | PENDING (quota) |
| django__django-11422 | PENDING (quota) |
| django__django-11564 | PENDING (quota) |
| django__django-11620 | PENDING (quota) |

**Summary of the 14 fully tested tasks:** 10 PASS (71%), 4 did not succeed (29%) — 1 genuine logic failure, 3 malformed-patch errors.

---

## The real failure pool (usable today for planning Day 8+)

```
django__django-11019   (genuine logic failure)
astropy__astropy-14182 (malformed patch)
django__django-11039   (malformed patch)
django__django-11583   (malformed patch)
```

**4 confirmed failing tasks**, spanning two distinct failure categories (logic vs. format) — a legitimate, if modest, starting pool for the recovery-method comparison. This will very likely grow once the remaining 6 tasks are generated (based on today's ~29% failure rate, expect roughly 1-2 more failures among them).

---

## Why this matters for the paper

Today confirms the strategic concern raised at the start of the day: **there IS enough natural failure in this task set to make the recovery comparison meaningful** — it's not the "everything passes trivially" scenario that would have undermined the whole research question. The 29% failure rate, combined with genuinely distinct failure types (logic vs. formatting), gives real material to diagnose and recover from.

**Free-tier rate limits as a documented methodological constraint:** worth one sentence in the paper's limitations — reproducing or extending this study at larger scale requires either a paid API tier or multi-day pacing, which is a real, citable constraint of zero-budget LLM-agent research.

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day7_step1_generate_full_pilot.py` | Generates attempts across 20 tasks (skips existing) | `06_Methodology/code/` |
| `day7_step2_make_predictions_pilot20.py` | Builds predictions.json + skipped-task log | `06_Methodology/code/` |
| `day7_step3_extract_failure_pool.py` | Builds the final results table + failure_pool.json | `06_Methodology/code/` |
| `predictions_pilot20.json` | 14 evaluated predictions | `06_Methodology/code/` |
| `skipped_pilot20.json` | Log of skipped/blocked tasks with reasons | `06_Methodology/code/` |
| `failure_pool.json` | Current failing task list (to be updated once 6 pending tasks resolve) | `06_Methodology/code/` |
| `gemini-3.6-flash-blindretry-attempt1.day7_test.json` | Full evaluation report | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

1. **Skipped straight to Step 3 without running the harness** — a workflow slip, not a bug. Resolved by running the missing evaluation command.
2. **Free-tier daily quota (20 requests/day) reached** — genuine external constraint, not fixable today. Resolved by pausing the remaining 6 tasks until quota resets (~24 hours from first request).
3. **Docker unreachable again after switching to WSL** — resolved by enabling WSL Integration in Docker Desktop settings and restarting.
4. **3 malformed-patch errors** (`astropy-14182`, `django-11039`, `django-11583`) — not fixed today; these are now valid entries in the failure pool for the recovery experiment to act on, rather than something to force-correct at the baseline stage.

---

## Next step (Day 8)

1. Rerun `day7_step1_generate_full_pilot.py` once the quota resets to pick up the final 6 tasks (automatic — it skips everything already done).
2. Merge the final results into one complete 20-task table and a finalized `failure_pool.json`.
3. Begin building the three recovery conditions (Blind Retry, Reflection-only, Diagnose+Revise) to run specifically on the failure pool.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
