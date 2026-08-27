# Day 1 Summary — Research Gap, Clarifications & Plan

**Date logged:** Day 1 of the project
**Project:** Self-Reflection and Failure Recovery in Agentic AI Coding Systems
**Stage:** Steps 1-3 complete (review → candidate gaps → validated against 2026 literature). Today = setup day, Step 4 starts tomorrow.

---

## 1. THE RESEARCH GAP (final, validated)

> While recent literature (2023–2026) has made substantial progress in diagnosing why autonomous coding agents fail — through failure taxonomies, root-cause localization, and process-level trajectory analysis — this diagnostic capability has not been coupled with an evaluated recovery mechanism for repository-level software engineering tasks. Existing self-reflection approaches (e.g., Reflexion, SELF-REFINE) improve reasoning without diagnosing the cause of failure, while existing diagnosis approaches (e.g., AgentDebug and its 2026 successors) identify root causes without using that diagnosis to drive a structured, re-executed repair attempt — and where diagnosis-plus-recovery has been evaluated (AgentDebug/AgentDebugX), it has been tested only on general agent environments (ALFWorld, GAIA, WebShop), not on repository-level coding. Consequently, it remains unknown whether an integrated loop — detect failure → diagnose root cause → reflect → revise the approach → re-execute — actually improves task recovery on repository-level coding benchmarks compared to simple retry or reflection-only baselines, and no established metrics exist to measure that improvement beyond final task success.

### Plain-language version
Everyone in 2026 is good at explaining **why** a coding AI agent failed. Nobody has built something that takes that explanation, actually changes what the agent does, tries again, and proves — with numbers — that it worked better than just retrying blindly. That is the gap. We are the doctor who cures the patient and checks they got better, not just the detective who explains what went wrong.

---

## 2. WHERE THIS GAP CAME FROM

**A. From our 35-paper systematic review (2023-2025 corpus):**
- Section I: agents recognize failures but can't explain *why* → repeat repair attempts.
- Section IV-D: recovery today is reactive, doesn't distinguish reasoning errors from execution errors, doesn't store failure knowledge.
- Section V-A: "the current literature provides plenty of evidence on individual capacities like reflection, memory, planning, tools usage, debugging, and failure recovery... investigated separately... validated in completely different scenarios."
- The review's own stated opportunity: *"developing and implementing an effective failure recovery approach for autonomous coding systems based on self-reflection."*

**B. From our live 2026 web-search validation (done today's earlier session):**
Found a wave of 2026 papers that **diagnose** coding-agent failures in detail, but none that **build and test an active recovery loop** for repository-level coding:
- *Failure as a Process* (Jul 2026) — traces failure evolution on Terminal-Bench, no recovery intervention tested.
- *AgentLens*, *TRACEPROBE* — process-level diagnostics for SWE-agent/SWE-Bench.
- *RepoLaunch* — failure-pattern taxonomy on SWE-bench-Live.
- *Beyond Resolution Rates* — 9,374 trajectories studied, why agents fail, no fix mechanism built.
- *AgentDebugX* (2026 successor to our review's key reference [21]) — adds closed-loop repair, but still tested on GAIA, not coding.

**Conclusion:** the gap is confirmed still open as of the 2026 search. The field explains failure in detail; nobody has shown that *acting* on the diagnosis (not just naming it) improves recovery on real repository-level coding tasks.

---

## 3. CONFUSIONS CLEARED UP TODAY (Q&A)

**Q: What do "Candidate A" and "Candidate B" mean?**
- **Option A = "Just diagnose."** Detect a failure, explain why it happened. Stop there.
- **Option B = "Diagnose AND fix, then prove it worked."** Detect → diagnose → change the approach → re-execute → measure if it actually helped vs. blind retry.
- Option A is now crowded (lots of 2026 papers do this). **Option B is our gap — the one we are pursuing.**

**Q: Will this whole project cost me anything?**
- Research/writing work with Claude: free.
- Running the AI agent experiments: **free**, using Google Gemini API's free tier (Gemini 2.5/3 Flash models, ~1,500 requests/day, no credit card required).
- ⚠️ Trap to avoid: never add a credit card / enable billing on the API project — some providers silently kill the free tier and start charging from the first token the moment billing is attached.
- Running the actual coding tasks: free, runs on a normal laptop, no GPU needed.
- Task data (SWE-bench Lite): free, public dataset.
- Submitting the paper normally (non-open-access): typically free. Open-access publishing later would cost money, but that's an optional future decision, not needed now.
- **Bottom line: $0 if we stick to the free-tier plan.**

**Q: I also want to learn DSA and web development alongside this — is that realistic in 1-2 months?**
- Yes, if research gets priority time and DSA/web dev become a **daily light habit** (30-45 min each) rather than big blocks, since the paper has a real deadline and DSA/web dev don't need to be finished this month — just built consistently.
- Claude will write the repetitive/boilerplate research code (agent loop skeleton, baseline scripts) so the manual coding burden on the research side stays low, leaving you energy for DSA/web dev and placement prep.

---

## 4. THE SCOPED EXPERIMENT (Step 4 methodology, locked in)

Given: 1-2 months, beginner coder, no confirmed budget → keep it small and self-built (no heavy agent frameworks like OpenHands).

**Tasks:** 15-20 tasks from SWE-bench Lite (small, real GitHub bug-fix issues)

**Three conditions to compare:**
| Condition | What it does |
|---|---|
| Blind Retry (baseline) | Fails, retries with no analysis |
| Reflection-only (baseline) | Fails, writes a reflection, retries |
| Diagnose + Revise (our method) | Fails, diagnoses the specific cause, revises approach based on that, retries |

**Metrics:** task success rate, attempts needed, whether the same mistake repeats, API cost.

**Research question:**
> Does an integrated failure-recovery loop — combining root-cause diagnosis with self-reflection-guided revision and re-execution — improve task recovery on repository-level coding tasks, compared to retry-based and reflection-only baselines?

---

## 5. DAILY RHYTHM (going forward)

| Block | Suggested time | What |
|---|---|---|
| Research | ~2-3 hrs | Today's specific task (given each day) |
| DSA | 30-45 min | 1 problem/day, topic-wise |
| Web dev | 30-45 min | Short focused lesson/build |

---

## 6. TODAY'S TASK LOG (Day 1)

- [ ] Create a free Google AI Studio account, generate a Gemini API key — **no billing/credit card attached**
- [ ] Save the API key safely (not shared anywhere)
- [ ] Browse ONE SWE-bench Lite example on Hugging Face to see what a real task looks like (no need to fully understand it yet)
- **Stopped here today — no coding yet.** Tomorrow: first Python script + first live API call.

---
*File 3 of the project (alongside `research_review_analysis.md`, `research_candidate_gaps.md`, and `research_gap_final.md`). Keep all four together for future reference.*
