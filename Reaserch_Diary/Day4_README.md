# Day 4 — README (Implementation Log)

**Goal for today:** Take the bug-fix attempt from Day 3 and actually check — using the real test suite — whether it works. Get a real PASS or FAIL result.
**Status:** ✅ Complete. Result: FAIL (both attempts) — but we learned exactly *why*, which is itself a valuable research finding.

---

## How to explain this to your professor in 2 minutes

> "We took the AI's proposed bug fix from Day 3 and ran it through the actual test suite the real astropy project uses — using the official SWE-bench evaluation tool, which runs everything in an isolated Docker container so results are reproducible. The fix failed both times we tried it — but not because the AI's reasoning was wrong. It failed because the AI was writing its fix 'blind,' without ever seeing the real source code. This is a real, documented failure mode in AI coding agents: models generate patches from what they *assume* the code looks like, not what it actually looks like. We identified this precisely, which is exactly the kind of 'failure diagnosis' our research gap is about."

---

## What was done today

### 1. Installed the official evaluation tool
Installed `swebench` (v5.0.2), the same tool real SWE-bench research papers use to check if a proposed patch actually fixes the bug. This runs the code and its real tests inside a Docker container — not just a "looks correct" guess.

### 2. Converted Day 3's saved attempt into the required format
Built `day4_step1_make_predictions.py` to turn the saved `attempt1.txt` file into `predictions.json` — the exact format the evaluation tool expects (`instance_id`, `model_patch`, `model_name_or_path`).

### 3. Ran the evaluation — Attempt 1 (result: FAIL — malformed patch)
```
python -m swebench.harness.run_evaluation --dataset_name SWE-bench/SWE-bench_Lite --predictions_path predictions.json --max_workers 1 --run_id day4_test --instance_ids astropy__astropy-12907
```
**Result:** `Patch Apply Failed — patch unexpectedly ends in middle of line`

**What this means in plain words:** the AI's diff (its proposed code change) was written in a broken format — like a recipe with the wrong number of steps listed at the top. The patch tool couldn't even try applying it.

### 4. Fixed the prompt and retried — Attempt 2 (result: FAIL — wrong context)
We rewrote the prompt with stricter formatting rules and made sure the saved patch always ends with a proper newline. Reran with a new `run_id` (`day4_test2`, since the tool caches results by run ID).

**Result:** `Hunk #1 FAILED at 58` — the diff format was now *valid*, but it didn't match the actual code in the file.

**What this means in plain words:** the AI's diff was now written correctly, like a well-formatted recipe — but it assumed the kitchen (the actual code file) looked different than it really does. The AI was fixing code it imagined, not the code that actually exists in the file.

---

## Why two different failure types matter (this is a real finding, not a mistake)

| Attempt | Failure type | What it tells us |
|---|---|---|
| 1 | Malformed diff (broken format) | The AI can't reliably format its own output correctly |
| 2 | Valid diff, wrong context | The AI is guessing at code it has never actually seen |

These are **two distinct, separately diagnosable failure categories** — not just "it failed." This directly matches what your systematic review identified as a gap: current systems can't tell *why* something failed, only *that* it failed. You just demonstrated, with real data, two different reasons a coding agent's fix attempt can fail before ever reaching "is the logic even correct."

**Root cause identified:** the model was never shown the actual file — only the bug report. It was fixing code from memory/imagination, not from the real repository. This is why real coding agents (mentioned throughout your review — SWE-agent, AutoCodeRover, RepairAgent) always read the actual repository files before proposing a fix.

---

## Files produced today

| File | Purpose | Location |
|---|---|---|
| `day4_step1_make_predictions.py` | Converts a saved attempt into the harness's required format | `06_Methodology/code/` |
| `predictions.json` | The formatted prediction fed to the evaluation tool | `06_Methodology/code/` |
| `gemini-3.6-flash-attempt1.day4_test.json` | Evaluation report, Attempt 1 (malformed patch) | `06_Methodology/code/` |
| `gemini-3.6-flash-attempt1.day4_test2.json` | Evaluation report, Attempt 2 (context mismatch) | `06_Methodology/code/` |

---

## Issues hit and how they were resolved

1. **`KeyError: 'image'`** — the dataset name `princeton-nlp/SWE-bench_Lite` is an older copy without pre-built Docker image references. Fixed by switching to `SWE-bench/SWE-bench_Lite`, the current official dataset.
2. **Malformed patch** — fixed by rewriting the prompt with explicit, strict diff-formatting rules, and by guaranteeing a trailing newline when saving the patch.
3. **Result caching confusion** — the harness reuses cached results if you rerun the same `run_id`. Fixed by using a new `run_id` for each new attempt (`day4_test` → `day4_test2`).

---

## Next step (Day 5)

Stop asking the AI to guess what the code looks like. Instead: **fetch the real file content directly from GitHub** (at the exact commit the bug report is based on) and give that real code to the model before asking for a fix. This directly targets the root cause identified today. Script already prepared: `day5_step1_attempt_with_context.py`.

---
*Part of the implementation log for: Self-Reflection and Failure Recovery in Agentic AI Coding Systems.*
