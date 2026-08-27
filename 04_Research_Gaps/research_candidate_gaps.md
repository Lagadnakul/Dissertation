# STEP 2 — Candidate Research Gap Analysis
## Project: "Self-Reflection and Failure Recovery in Agentic AI Coding Systems: A Systematic Review" (35 studies)

**Primary source for this step:** `research_review_analysis.md` (Step 1 output), which itself documents only what is contained in the systematic review manuscript.

**Purpose of this file:** To generate and *candidate* research gaps from the unresolved problems identified in Step 1, analyze each one honestly, rank them, and identify the top 3 directions.

**Important ground rules followed in this file:**
- No candidate is declared "novel" or "the final gap." These are *candidates* that validation.
- No external papers are added. All references ([1]–[35]) are from our review.
- Statements use careful wording: *"the review indicates…"*, *"this appears to be underexplored…"*, *"this requires validation through additional literature."*
- For every candidate, two evidence buckets are kept strictly separate:
  - ✅ **Supported by our 35-paper review** — things the review itself documents.
  - ⚠️ **Still needs verification through additional literature** — things we cannot know from 35 papers alone, especially work published in 2025–2026 that may not be in our corpus.

---

# PART 1 — THE EIGHT CANDIDATE DIRECTIONS

---

## Candidate A — Root-Cause Analysis and Diagnosis of Failures in Repository-Level Coding Agents

### 1. Candidate research gap
Autonomous coding agents can detect *that* a failure happened, but the review indicates they generally cannot determine *why* it happened. Adapting root-cause analysis (RCA) specifically to repository-level coding trajectories — where failures can originate in task interpretation, planning, repository navigation, file selection, code generation, tool use, compilation, or testing — appears underexplored in the reviewed literature.

### 2. What existing research already does
- **Automated program repair (APR)** local fault localization in source code, patch proposal, patch validation against tests ([5] RepairAgent, [18] APR survey, [3] AutoCodeRover).
- **Self-reflection methods** detect undesirable outcomes and and generate feedback to retry ([7] Reflexion, [8] SELF-REFINE, [10] Self-Debug).
- **AgentDebug [21]** (= "P26" in the review body) already does explicit failure taxonomy, root-cause localization, feedback generation, and iterative recovery — **but only in general agent environments (ALFWorld, GAIA, WebShop), not coding**.

### 3. What appears to be missing
According to the review: a diagnosis capability that works on *coding agent trajectories* — one that can trace a failure back through repository navigation, tool calls, reasoning steps, and decisions, and distinguish **reasoning errors from execution errors** (Section IV-D, Section V-C).

### 4. Evidence from our 35-paper review
- ✅ Section I: "an agent can recognize the occurrence of an execution failure without being able to understand its cause, leading to inefficiency or repetition of repair attempts."
- ✅ Section IV-D: existing systems "lack specific methods for determining reasons for failures, as well as differentiating reasoning errors from execution errors and storing information on failures for future use."
- ✅ Table III limitations: [2] (no explicit root-cause identification), [4] (lacks root-cause-oriented recovery), [7] (no detailed diagnosis of execution failures), [8] (no execution-failure diagnosis), [20] (no software-specific root-cause analysis), [24] (limited root-cause identification), [31] (no recovery architecture based on root-cause analysis), [33] (no diagnosing individual task execution failures).
- ✅ Section V-C: future direction explicitly names root-cause analysis that traces failures "throughout several reasoning phases, separating the problem into planning mistakes and execution flaws."

### 5. Closest reviewed papers to this problem
**[21]** (AgentErrorTaxonomy / AgentErrorBench / AgentDebug) — by far the closest; the methodological template. Then [5] RepairAgent (fault localization, but code-only), [18] (APR survey), [3] AutoCodeRover.

### 6. Why the gap could matter for agentic software engineering
The review states failures are **cumulative**: "one initial reasoning error cascades into a series of planning mistakes, ultimately leading to total failure of the task" (Section IV-D). Without diagnosis, agents "tend to make the same reasoning errors again and again" (Section IV-D). Diagnosis is therefore the prerequisite for stopping cascades and for any real learning from failure.

### 7. What could potentially be investigated experimentally
- Collect execution trajectories of a coding agent on repository-level tasks (e.g., SWE-Bench-style issues [19]).
- Annot or automatically label the root cause of intermediate failures.
- Build a diagnosis step (e.g., LLM-based root-cause localization over the trajectory, following the AgentDebug idea of [21] but adapted to coding artifacts: diffs,,,, us- Compare: repair guided diagnosis vs. repair with blind retry.
- Measure: diagnosis accuracy, recovery success rate, number of repeated failures, attempts needed.

### 8. Possible research question
*"How accurately can an autonomous coding agent identify the root cause of intermediate execution failures in repository-level tasks, and does root-cause-aware repair improve recovery success compared with retry-based repair?"*

### 9. Possible contribution
A root-cause diagnosis approach for coding agent trajectories + empirical evidence on whether diagnosis actually improves repair outcomes in repository-level coding.

### 10. Difficulty of implementation: **Medium**
Needs trajectory collection and annotation and a working agent setup, but the core diagnosis step can be LLM-based ( no model training required).

### 11. Expected research value: **High**
It targets the single most repeated limitation in the whole review (

### 7.1 of the analysis file).

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ [21] already solves root-cause analysis for *general* agents; the coding adaptation is what the review says is unproven — but this needs verification.
- ⚠️ This is a fast-moving field (2025–2026). Work published after our corpus was collected may already have adapted failure diagnosis to coding agents. **Requires validation through additional literature.**

---

## Candidate B — Integration of Self-Reflection + Root-Cause Analysis + Failure Recovery

### 1. Candidate research gap
The review indicates that self-reflection, root-cause analysis, memory, planning, and recovery are each studied **independently**, and that no reviewed study combines them into a single recovery process for coding agents (Sections I, V-A, VI). An integrated recovery loop for repository-level coding — detect failure → diagnose cause → reflect → revise → re-execute — appears to be underexplored as an evaluated, coding-specific system.

### 2. What existing research already does
- Reflection without diagnosis: [7] Reflexion, [8] SELF-REFINE, [10] Self-Debug.
- Diagnosis + recovery without coding: [21] AgentDebug (general agent environments).
- Repair without reasoning diagnosis: [5] RepairAgent, [3] AutoCodeRover.
- Fragmented self-correction methods overall: [13] survey.

### 3. What appears to be missing
According to the review: a system where these components **interact throughout the whole software-engineering process**, not as isolated techniques — specifically for coding, where recovery "may need not just code fixing, but also changes in plans and tools as well as maintaining useful execution history between several iterations" (Section II-D).

### 4. Evidence from our 35-paper review
- ✅ Section V-A: "The current literature provides plenty of evidence on individual capacities like reflection, memory, planning, tools usage, debugging, and failure recovery. Nevertheless, these capabilities are investigated separately from different perspectives and are validated in completely different scenarios."
- ✅ Section VI: "The review identified a gap related to the lack of combined failure recovery solutions that integrate reflection, cause analysis, memory, planning, and adaptive execution."
- ✅ Section V-A (explicit framing): the opportunity "lies in developing and implementing an effective failure recovery approach for autonomous coding systems based on self-reflection… a coding-specific integration and evaluation issue."
- ✅ Section V-B (the core question): "the key challenge is how to adapt such mechanisms to particular features of the autonomous software engineering execution."
- ✅ Fig. 3 of the review: the integrated workflow (Task Execution → Failure Detection → Root Cause Analysis → Self-Reflection → Memory Retrieval → Adaptive Replanning → Re-execution) is presented as *synthesized from the literature* — i.e., conceptual, not implemented by any reviewed study.
- ✅ Table III: no reviewed study is rated "E" (explicit) on all five capabilities *in a repository-level coding context*.

### 5. Closest reviewed papers to this problem
**[21]** (closest — has diagnosis + reflection + iterative recovery, but not coding); [7] (reflection component); [5] (repair component); [6] OpenHands (a platform where such integration could be built); [13] (shows the fragmentation).

### 6. Why the gap could matter for agentic software engineering
This is the review's own central conclusion. If components only work in isolation, real multi-step coding tasks — where errors cascade across stages — will keep failing. The review states that evaluating integration is also the only way to learn "whether self-reflection is truly enhancing the reliability of autonomous coding trajectories or just increasing the number of executions" (Section V-A).

### 7. What could potentially be investigated experimentally
- Implement a recovery loop (failure detection → root-cause diagnosis → reflection-based revision → re-execution) on top of an existing open agent framework.
- Run it on repository-level tasks (SWE-Bench-style [19]).
- **Ablation comparison**: (a) no recovery / blind retry, (b) reflection only (Reflexion-style [7]), (c) diagnosis only, (d) integrated loop.
- Measure: task recovery rate, diagnosis accuracy, repeated-failure count, number of attempts, execution cost, final correctness.

### 8. Possible research question
*"Does an integrated failure-recovery loop that combines self-reflection with root-cause diagnosis improve repository-level coding task completion, compared with isolated reflection or retry-based recovery?"*

### 9. Possible contribution
(i) A coding-specific integrated recovery mechanism; (ii) a controlled empirical comparison showing what each component adds; (iii) evidence on whether integration beats isolated components.

### 10. Difficulty of implementation: **Medium–High**
The loop itself can be built from LLM prompting + an open agent platform, but it needs careful scoping (see ranking) and a working evaluation harness on repository tasks.

### 11. Expected research value: **High**
It directly answers the review's explicitly stated research opportunity.

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ "Integration" claims are common in this fast-moving field. Systems from late 2025–2026 (after our corpus) may already combine some of these pieces for coding. **Requires validation through additional literature.**
- ✅ Within our 35-paper corpus, the review documents that no study does this for repository-level coding.

---

## Candidate C — Failure-Aware Memory for Autonomous Coding Agents

### 1. Candidate research gap
Memory systems for agents store and retrieve experiences, but the review indicates they are **not connected to failures**: they do not decide what to save/update/delete after a failed attempt, do not judge memory quality, and are not integrated with reflection or execution monitoring (Sections II-E, IV-C). A *failure-aware* memory for coding agents appears underexplored in the reviewed literature.

### 2. What existing research already does
- [15] A-MEM — dynamic organization and retrieval of agent experiences (memory organization, not failure diagnosis).
- [16] MIRIX — episodic/semantic/procedural/resource/knowledge memory types.
- [11] ExpeL — stores lessons from successful and unsuccessful experiences (general reasoning tasks).
- [17] LOCOMO — long-term conversational memory benchmark (not software engineering).

### 3. What appears to be missing
According to the review: memory that (a) learns specifically *from failures*, (b) evaluates whether stored experiences are relevant/applicable, (c) integrates with reflection and failure analysis, and (d) is used in repository-level coding (Section II-E, IV-C). The review names "failure-aware memory" as one of three promising memory directions (Section V-C).

### 4. Evidence from our 35-paper review
- ✅ Section II-E: "the current techniques fail to combine memory with reflection, execution monitoring, and failure analysis."
- ✅ Section IV-C: "the majority of intelligent software engineering agents are still utilizing memory components that enable them to retrieve information, but not learn from past experience."
- ✅ Section IV-C limitation 1: memory systems don't analyze the quality of memories — "faulty memories will continue to affect the process of reasoning."
- ✅ Table III: [3] (no reuse of failure knowledge between tasks), [8] (no persistent memory), [11] (experience transfer can fail), [15] (memory organization, not failure/recovery), [24] (limited persistent learning).
- ✅ Section V-C: explicit future direction — "dynamic memory prioritization, experience abstraction, and failure-aware memory."

### 5. Closest reviewed papers to this problem
[15] A-MEM, [11] ExpeL, [16] MIRIX, and [21] (which uses failure feedback but is not coding-specific and whose memory aspect is rated only partial).

### 6. Why the gap could matter for agentic software engineering
Software engineering tasks are repetitive (Section IV-C). Without failure-aware memory, agents repeat the same reasoning errors across tasks; with it, they could retrieve "previous debugging experience, execution trace, patches, and failure recovery methods whenever similar failures would occur" (Section II-E).

### 7. What could potentially be investigated experimentally
- Build a failure-memory store: after each failed attempt, extract and store structured failure lessons (cause, what was tried, what worked).
- Retrieve relevant failure lessons on new tasks.
- Compare: agent with failure-aware memory vs. agent without, across a *sequence* of coding tasks.
- Measure: repeated-failure rate, task success over time, retrieval relevance.

### 8. Possible research question
*"Can a failure-aware memory mechanism reduce repeated execution failures and improve task completion in autonomous coding agents across sequential repository-level tasks?"*

### 9. Possible contribution
A failure-aware memory design for coding agents + empirical evidence on repeated-failure reduction.

### 10. Difficulty of implementation: **Medium–High**
The memory store itself is feasible; the hard part is the *evaluation design* — you need sequences of related tasks to show cross-task learning, and such task sequences are not the standard unit in SWE-Bench-style benchmarks [19].

### 11. Expected research value: **Medium–High**
Named explicitly as a future direction by the review; addresses a documented weakness.

### 12. Risk that the gap may already have been solved: **Medium–High**
- ⚠️ Agent memory is one of the most active areas right now (A-MEM [15] and MIRIX [16] are both 2025). Failure-aware or debugging-experience memory variants may already exist in 2025–2026 literature outside our corpus. **Strongly requires validation through additional literature.**
- ✅ Within our corpus, no reviewed study combines failure awareness + memory + coding.

---

## Candidate D — Adaptive Replanning After Intermediate Failures

### 1. Candidate research gap
The review indicates that replanning in response to execution feedback has been demonstrated *outside* software engineering ([23] in embodied tasks), while conceptual frameworks for agent planning ([22]) lack evaluation in programming environments. When a coding agent should revise its *plan* (rather than its code or tool choice) after an intermediate failure appears underexplored in the reviewed literature.

### 2. What existing research already does
- [23] LLM-Planner — grounded replanning, but in ALFRED embodied tasks.
- [22] TPTU — conceptual planning/tool-usage framework, no programming-environment evaluation.
- Hierarchical task decomposition improves execution efficiency (Section IV-E).
- Coding agents like SWE-agent [4] and OpenHands [6] already adjust actions based on tool feedback to some degree (Section II-F describes this feedback loop as standard).

### 3. What appears to be missing
According to the review: explicit, evaluated replanning strategies for coding — including deciding *what kind* of revision a failure requires: "revision of the code, change in the plan, modification of tool actions, retrieval of the relevant experience, or re-interpretation of the initial task description" (Section V-B).

### 4. Evidence from our 35-paper review
- ✅ Table III: [22] "lacks evaluation in programming environments"; [23] "demonstrates replanning outside software engineering and lacks repository-level coding evaluation."
- ✅ Section V-B: recovery may require different response types (code vs. plan vs. tool vs. task re-interpretation).
- ✅ Section II-F: "The agents might be doing redundant actions, choosing incorrect tools, or failing to adapt their planning strategy when encountering unexpected execution results."

### 5. Closest reviewed papers to this problem
[23] LLM-Planner, [22] TPTU, [6] OpenHands (platform), [21] (feedback-driven iterative recovery in general settings).

### 6. Why the gap could matter for agentic software engineering
Because failures cascade across interdependent steps (Section IV-D), knowing *when and how to change the plan* — rather than blindly re-executing it — could prevent small early errors from becoming total task failures.

### 7. What could potentially be investigated experimentally
- Add an explicit replanning trigger: after a detected failure, decide whether to revise code, plan, or tool strategy.
- Compare against fixed-plan-with-retry behavior on repository-level tasks.
- Measure: recovery rate after plan-related failures, task completion, wasted actions.

### 8. Possible research question
*"Does explicit adaptive replanning after intermediate failures improve repository-level coding task completion compared with retry-based execution?"*

### 9. Possible contribution
An evaluated replanning strategy for coding agents, plus evidence on which failure types need plan revision vs. code revision.

### 10. Difficulty of implementation: **Medium**

### 11. Expected research value: **Medium**
Real but narrower than A/B; replanning is one *component* of recovery rather than the recovery problem itself.

### 12. Risk that the gap may already have been solved: **Medium–High**
- ⚠️ Existing coding agents already adapt behavior based on tool feedback (Section II-F presents this feedback loop as standard in SWE-agent [4], AutoCodeRover [3], RepairAgent [5], OpenHands [6]). Showing a *clearly new* replanning contribution over what agents implicitly do may be difficult. **Requires validation through additional literature.**

---

## Candidate E — Proactive Failure Detection / Failure Prediction

### 1. Candidate research gap
The review states that "most of the current systems do not conduct recovery until there is an actual failure" (Section IV-D) — all recovery in the reviewed literature is **reactive**. Proactive failure management — predicting failure probability, detecting hazardous reasoning patterns, monitoring execution paths *before* failure happens — is named only as a future direction (Section V-C) and is not implemented by any reviewed study.

### 2. What existing research already does
- Nothing in the 35-paper corpus implements proactive failure prediction for coding agents.
- Post-hoc (after-the-fact) failure analysis exists: [21] AgentDebug.
- Trajectory judging by another agent exists: [26] Agent-as-a-Judge (evaluation, not prediction).

### 3. What appears to be missing
According to the review: "Predictive failure detection, uncertainty-based planning, and continuous execution monitoring" (Section V-C) — shifting "from reactive execution recovery to proactive execution management."

### 4. Evidence from our 35-paper review
- ✅ Section IV-D: "most of the recovery mechanisms currently available are reactive in nature."
- ✅ Section V-C: explicit future direction — "intelligent agents need to monitor execution paths, predict failure probability, detect hazardous reasoning patterns, and plan ahead."
- ✅ Section VI: "proactive failure prevention" listed among lacking assessment approaches.

### 5. Closest reviewed papers to this problem
[21] (failure analysis, but post-hoc), [26] (trajectory evaluation by agents), [27] RedCode (risk/safety benchmarking, not recovery).

### 6. Why the gap could matter for agentic software engineering
Since failures cascade (Section IV-D), catching a hazardous reasoning pattern *early* could prevent total task failure and save the compute cost of long failed trajectories (Section V-C also raises computational efficiency).

### 7. What could potentially be investigated experimentally
- Collect coding-agent trajectories labeled with where failures eventually occurred.
- Build a monitor (LLM-based or trained) that predicts, from intermediate steps, whether the trajectory is heading toward failure.
- Measure: prediction precision/recall, how early failure can be predicted, effect of early intervention on task success.

### 8. Possible research question
*"Can execution failures of autonomous coding agents be predicted from intermediate trajectory signals before the task fails, and does early intervention improve task outcomes?"*

### 9. Possible contribution
A failure-prediction approach for coding trajectories + a labeled trajectory resource.

### 10. Difficulty of implementation: **High**
Requires substantial labeled trajectory data and temporal prediction methods; intervention experiments add further complexity.

### 11. Expected research value: **High**
Genuinely forward-looking; named by the review as a next-generation direction.

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ Because the review itself names this direction, other groups may be pursuing it too; adjacent work on monitoring/oversight of agent trajectories may exist outside our corpus. **Requires validation through additional literature.**
- ✅ Within our corpus, no study implements it.

---

## Candidate F — Recovery-Oriented Evaluation Metrics for Coding Agents

### 1. Candidate research gap
The review indicates that evaluation of coding agents focuses on **final task success**, while the *recovery process itself* is not measured. Metrics such as failure diagnosis accuracy, recovery success rate, repeated-failure reduction, recovery latency, and recovery cost are named by the review (Section V-A) but are not established or validated in any reviewed study.

### 2. What existing research already does
- Task-success benchmarks: SWE-Bench [19], AgentBench [20], API-Bank [24], RedCode [27].
- Trajectory judging: [26] Agent-as-a-Judge (quality depends on the judging agent).
- Failure annotation in general settings: AgentErrorBench within [21].

### 3. What appears to be missing
According to the review: a validated set of recovery-oriented metrics for coding agents, and evidence that these metrics can distinguish systems that genuinely recover from systems that merely retry more times (Sections II-G, IV-D, V-A, VI).

### 4. Evidence from our 35-paper review
- ✅ Section II-G: benchmarks "usually focus on the output rather than the process of reasoning, planning, memory usage, self-evaluation or recovering from failures."
- ✅ Section IV-D: "not much work has been done on the estimation of the recovery capacity of an agent."
- ✅ Section V-A: explicit metric list — "failure diagnosis accuracy, recovery success rate, recovery attempts, decreased number of repeated failures, tool invocation, execution cost, recovery latency, and correctness of software."
- ✅ Section V-A: without such metrics we cannot know "whether self-reflection is truly enhancing the reliability of autonomous coding trajectories or just increasing the number of executions."
- ✅ Table III: [19] (limited info about intermediate failures and recovery), [20] (no software-specific recovery focus), [24] (limited long-term recovery evaluation), [27] (no post-failure recovery).

### 5. Closest reviewed papers to this problem
[26] Agent-as-a-Judge, [19] SWE-Bench, [21] (AgentErrorBench), [20] AgentBench.

### 6. Why the gap could matter for agentic software engineering
Measurement comes before progress: if recovery cannot be measured, no recovery method (Candidates A–E, H) can be properly validated. This is a foundational contribution that every other candidate depends on.

### 7. What could potentially be investigated experimentally
- Define a concrete metric suite (operationalizing the review's list from Section V-A).
- Compute the metrics on coding-agent trajectories (from running an agent on repository-level tasks, or on available trajectory data).
- Show the metrics discriminate between recovery strategies (e.g., retry vs. reflection vs. diagnosis-based).
- Measure: metric reliability, discriminative power, correlation with final task success.

### 8. Possible research question
*"Which metrics reliably capture the failure-recovery capability of autonomous coding agents beyond final task success rate, and do these metrics discriminate between different recovery strategies?"*

### 9. Possible contribution
A recovery-oriented metric framework for coding agents + empirical demonstration that it reveals differences invisible to task-success metrics.

### 10. Difficulty of implementation: **Low–Medium**
Mostly analysis and measurement design; the main dependency is access to agent trajectories.

### 11. Expected research value: **Medium–High**
Foundational and cited-by-everyone type of work, though less headline-grabbing than a new system.

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ Trajectory-level evaluation of agents is an active area ([26] is already in our corpus); 2025–2026 work may have proposed process metrics. **Requires validation through additional literature.**
- ✅ Within our corpus, no study establishes recovery metrics for coding agents.

---

## Candidate G — A Recovery-Oriented Benchmark for Coding Agents

### 1. Candidate research gap
The review indicates there is no benchmark that evaluates **intermediate failures and recovery** in repository-level coding. SWE-Bench [19] measures final issue resolution; AgentErrorBench (in [21]) annotates failure trajectories but only for general agent environments. A coding-specific recovery benchmark appears to be missing from the reviewed literature.

### 2. What existing research already does
- [19] SWE-Bench — real GitHub issues, final patch correctness.
- [20] AgentBench — broad agent evaluation, not software-specific recovery.
- [21] AgentErrorBench — annotated failure trajectories (ALFWorld, GAIA, WebShop).
- [27] RedCode — safety, not recovery.

### 3. What appears to be missing
According to the review: "the development of standardized recovery-oriented benchmarks would allow for the objective evaluation of autonomous coding agents" (Section V-C) — a benchmark with coding tasks, recorded intermediate failures, annotated failure causes, and recovery evaluation.

### 4. Evidence from our 35-paper review
- ✅ Table III: [19] "Tests final issue solving but provides limited information about intermediate failures and recovery."
- ✅ Section V-B: [21]'s benchmark leaves "the problem of coding uncovered."
- ✅ Section V-C: explicit future direction — "creating more comprehensive benchmark datasets and evaluation methods for autonomous recovery purposes."
- ✅ Section VI: "There is a lack of approaches for the assessment of the effectiveness of the failure recovery process."

### 5. Closest reviewed papers to this problem
[19] SWE-Bench (task source), [21] (annotation methodology), [20] AgentBench.

### 6. Why the gap could matter for agentic software engineering
Benchmarks shape a field. A recovery-oriented coding benchmark would let any future recovery method (Candidates A–F, H) be compared objectively — the review says this would "accelerate the development of autonomous software engineering systems" (Section V-C).

### 7. What could potentially be investigated experimentally
- Select repository-level tasks; run one or more coding agents; record full trajectories.
- Annotate intermediate failures and their causes (building a coding failure taxonomy).
- Evaluate baseline agents' recovery behavior under the new benchmark.
- Measure: failure-type distribution, recovery success by failure type, baseline comparisons.

### 8. Possible research question
*"How do current autonomous coding agents fail at intermediate steps of repository-level tasks, and how well do they recover from those failures under systematic evaluation?"*

### 9. Possible contribution
A recovery-oriented benchmark + coding failure annotation + baseline results.

### 10. Difficulty of implementation: **High**
Benchmark building is expensive: task curation, agent runs, careful annotation, validation, and documentation. This is typically a multi-person, multi-month effort.

### 11. Expected research value: **High**
Benchmarks tend to be highly cited and community-shaping.

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ Benchmark construction in this area is booming (SWE-Bench [19] spawned many derivatives); trajectory-level coding benchmarks may already exist in 2025–2026 literature outside our corpus. **Strongly requires validation through additional literature.**

---

## Candidate H — An Integrated Framework Combining Several of the Above

### 1. Candidate research gap
This is the umbrella candidate: the review's Fig. 3 workflow (Task Execution → Failure Detection → Root Cause Analysis → Self-Reflection → Memory Retrieval → Adaptive Replanning → Re-execution) is explicitly presented as *synthesized from the literature* — a conceptual integration that **no reviewed study implements end-to-end** for coding.

### 2. What existing research already does
All individual components exist (see Candidates A–F). Nothing in the corpus combines them into one evaluated coding system.

### 3. What appears to be missing
According to the review: "creation of integrated autonomous recovery frameworks consisting of reasoning, planning, self-reflection, memory management, debugging, and adaptive execution… future systems should provide interaction between them throughout the entire process of software engineering" (Section V-C).

### 4. Evidence from our 35-paper review
- ✅ Section V-C: integrated frameworks are the *first* named future direction.
- ✅ Section VI: "all of these features are studied independently."
- ✅ Fig. 3: the integrated workflow is presented as a synthesis, not as an implemented system.
- ✅ Table III: no study is fully explicit on all capabilities in a coding context.

### 5. Closest reviewed papers to this problem
[21] (most complete component set, wrong domain), [6] OpenHands (a platform to build on), [7], [15], [5].

### 6. Why the gap could matter for agentic software engineering
It is literally the review's main conclusion and its vision of "failure-resilient autonomous agents" (Fig. 2's last stage, labeled "Emerging direction").

### 7. What could potentially be investigated experimentally
- Build a modular recovery framework on an open agent platform.
- Include 2–3 components (e.g., diagnosis + reflection + failure memory) — *not necessarily all of Fig. 3*.
- Ablation study: each component on/off.
- Evaluate on repository-level tasks with recovery-oriented metrics (Candidate F).

### 8. Possible research question
*"Does an integrated failure-recovery framework combining root-cause diagnosis, self-reflection, and failure-aware memory outperform isolated recovery mechanisms on repository-level coding tasks?"*

### 9. Possible contribution
An integrated framework + systematic ablation evidence about which components matter.

### 10. Difficulty of implementation: **High** (as stated); **Medium–High if scoped down to 2–3 components**
The full Fig. 3 vision is too large for a single M.Tech project. A scoped version is essentially Candidate B plus a memory component.

### 11. Expected research value: **High**

### 12. Risk that the gap may already have been solved: **Medium**
- ⚠️ Integrated agent systems are appearing rapidly in 2025–2026; some may already combine reflection + memory + repair for coding. **Requires validation through additional literature.**
- Note: H overlaps heavily with B. In practice, B is the *scoped, feasible form* of H.

---

# PART 2 — RANKING OF THE CANDIDATES

**Scoring method (judgment-based heuristic, 1–5 per criterion; higher is always better):**
- For *implementation difficulty* and *risk*, the score reflects *favorability*: 5 = easy / low risk, 1 = hard / high risk.
- Scores are my assessment as a reviewer based on the Step 1 analysis; they are a decision aid, not a measurement.

| Criterion | A: RCA | B: Integrated loop | C: Failure memory | D: Replanning | E: Proactive | F: Metrics | G: Benchmark | H: Full framework |
|---|---|---|---|---|---|---|---|---|
| 1. Novelty potential | 4 | 4 | 3 | 2 | 5 | 3 | 4 | 4 |
| 2. Research significance | 5 | 5 | 4 | 3 | 4 | 4 | 5 | 5 |
| 3. M.Tech feasibility | 4 | 3 | 3 | 3 | 2 | 5 | 2 | 2 |
| 4. Implementation ease | 3 | 3 | 2 | 3 | 2 | 4 | 2 | 2 |
| 5. Benchmark/data availability | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 4 |
| 6. Quantitative experiment potential | 5 | 5 | 4 | 3 | 4 | 5 | 4 | 4 |
| 7. Strong baselines available | 4 | 4 | 3 | 2 | 2 | 4 | 3 | 4 |
| 8. Publication potential | 4 | 5 | 4 | 3 | 4 | 3 | 5 | 5 |
| 9. Low risk (not already solved) | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 3 |
| **Total (max 45)** | **36** | **37** | **28** | **24** | **28** | **35** | **31** | **33** |

## Resulting ranking

| Rank | Candidate | Total | One-line reason |
|---|---|---|---|
| **1** | **B — Integrated reflection + root-cause + recovery loop** | 37 | The review's explicitly stated opportunity; high significance; feasible when scoped |
| **2** | **A — Root-cause analysis for coding agents** | 36 | The most repeated limitation in the review; focused and measurable; core of B |
| **3** | **F — Recovery-oriented evaluation metrics** | 35 | Most feasible; foundational; needed by every other candidate |
| 4 | H — Full integrated framework | 33 | Highest ambition, but too broad as stated; B is its feasible form |
| 5 | G — Recovery-oriented benchmark | 31 | High value, but heavy effort and higher already-exists risk for an M.Tech |
| 6 | C — Failure-aware memory | 28 | Real gap, but very active area (higher risk) and harder evaluation design |
| 6 | E — Proactive failure prediction | 28 | Most novel, but high difficulty and data demands |
| 8 | D — Adaptive replanning | 24 | Narrow; much of it is already implicit in existing agents |

---

# PART 3 — TOP 3 CANDIDATE DIRECTIONS (Beginner-Friendly Explanation)

## 🥇 TOP 1 — Candidate B: An Integrated Self-Reflection + Root-Cause Recovery Loop for Coding Agents

**What exactly would we study?**
We would study what happens when a coding agent fails in the middle of a task. Right now, the review says agents mostly just *notice* the failure and *retry*. We would study whether a structured loop — *detect the failure → figure out why it happened → reflect on what to change → make the change → try again* — makes the agent succeed more often on real repository-level tasks.

**What would we build?**
A recovery module that sits on top of an existing open-source coding agent (the review mentions platforms like OpenHands [6]). The module would: (1) watch the agent's execution (logs, test results, compiler output), (2) when a failure happens, ask a diagnosis step to find the root cause in the trajectory, (3) generate a reflection based on that cause, and (4) guide a revised attempt. No new LLM training needed — this can be done with prompting and orchestration.

**What would we compare it against?**
- Baseline 1: the plain agent with simple retry (what the review says most systems effectively do).
- Baseline 2: reflection-only recovery (Reflexion-style, following [7]) — reflection *without* diagnosis.
- Baseline 3 (optional): diagnosis without structured reflection.
- Our approach: the integrated loop.

**What would we measure?**
Exactly the metrics the review itself lists (Section V-A): recovery success rate, failure diagnosis accuracy, number of recovery attempts, reduction in repeated failures, execution cost, and final task correctness.

**What would make the contribution meaningful?**
The review explicitly says the open question is *not* whether reflection or recovery can work in isolation, but **whether integrating them works specifically for repository-level coding** (Section V-B). If our experiments show the integrated loop recovers more tasks than retry or reflection alone — and we show *why* via diagnosis accuracy — that directly answers the review's stated research opportunity. That is a complete, publishable empirical contribution.

---

## 🥈 TOP 2 — Candidate A: Root-Cause Diagnosis of Failures in Coding Agents

**What exactly would we study?**
We would study one focused question: when a coding agent fails, can we automatically identify *the real reason* (wrong file chosen? wrong plan? wrong tool call? wrong code?), and does knowing the reason lead to better fixes?

**What would we build?**
A diagnosis step for coding trajectories, inspired by AgentDebug [21] (which did this for general agents). Ours would understand coding-specific artifacts: repository structure, file edits, build output, test results. It would classify each failure and locate the step in the trajectory that caused it.

**What would we compare it against?**
- Repair guided by our diagnosis vs. blind retry vs. reflection-only repair (following [7]).
- We could also compare our failure classifications against the taxonomy idea of [21].

**What would we measure?**
Diagnosis accuracy (does the identified cause match the real cause?), recovery success after diagnosis, number of repeated failures, attempts per task.

**What would make the contribution meaningful?**
"Cannot identify the cause of failure" is the single most repeated limitation across the whole review (8+ studies in Table III). The review says [21] proved diagnosis works for general agents but explicitly notes it is **unproven for coding** (Section V-B). Demonstrating that cause-aware diagnosis improves repair in repository-level coding would fill exactly that documented hole. It is also a perfect *component* of Top 1 if we later combine them.

---

## 🥉 TOP 3 — Candidate F: Recovery-Oriented Evaluation Metrics

**What exactly would we study?**
We would study *how to measure recovery*. Today, the review says, benchmarks only check "did the agent finish the task?" (Section II-G). We would define and test metrics that measure the recovery *process*: how well the agent diagnoses failures, how often it recovers, whether it stops repeating the same mistake, and how much it costs.

**What would we build?**
A metric framework — a defined, computable set of recovery metrics (operationalizing the list the review already provides in Section V-A) — plus a small experimental demonstration: run 2–3 different recovery strategies and show that our metrics reveal differences that plain task-success rate hides.

**What would we compare it against?**
Not systems vs. systems, but *metrics vs. metrics*: we would show our recovery metrics discriminate between strategies (retry vs. reflection vs. diagnosis-based) where task-success rate alone cannot.

**What would we measure?**
The metrics themselves: diagnosis accuracy, recovery success rate, repeated-failure reduction, recovery attempts, recovery latency, execution cost — and whether they reliably separate good recovery from bad.

**What would make the contribution meaningful?**
The review says we currently cannot even tell "whether self-reflection is truly enhancing reliability… or just increasing the number of executions" (Section V-A). Providing the measurement toolkit answers that. It is also the **lowest-risk, most feasible** of the top 3, and it becomes the evaluation backbone if we pursue Top 1 or Top 2 — in practice, a good M.Tech project could combine B (or A) *with* F's metrics.

---

# STEP 2 CONCLUSION

## 1. What are the 3 strongest candidate research gaps?
1. **Candidate B** — An integrated failure-recovery loop combining self-reflection and root-cause diagnosis for repository-level coding agents.
2. **Candidate A** — Root-cause analysis and diagnosis of execution failures in repository-level coding agents.
3. **Candidate F** — Recovery-oriented evaluation metrics for coding agents.

## 2. Which one appears to be the strongest overall candidate?
**Candidate B** — with an important note: B *contains* A (diagnosis is its core component) and *uses* F (recovery metrics are how it would be evaluated). So the three top candidates are not competitors — they form one coherent project: **an integrated, diagnosis-aware self-reflection recovery loop for coding agents, evaluated with recovery-oriented metrics.** If B proves too large during scoping, A is the natural fallback that still stands alone as a solid contribution.

## 3. Why?
- It matches the review's **own explicit framing** of the research opportunity: "developing and implementing an effective failure recovery approach for autonomous coding systems based on self-reflection… a coding-specific integration and evaluation issue" (Section V-A).
- It answers the review's **stated core unresolved question**: "the key challenge is how to adapt such mechanisms to particular features of the autonomous software engineering execution" (Section V-B).
- It is **feasible for an M.Tech project**: it can be built by prompting/orchestration on top of an existing open agent platform, without training new models.
- It supports **clean quantitative experiments** with natural baselines (retry, reflection-only) and available repository-level task sources (SWE-Bench-style [19]).
- It has a **clear story for publication**: the review documents the fragmentation; the project provides the first (within what we have verified) empirical test of integration in the coding domain.

## 4. What evidence from our review supports it?
- Section I: agents recognize failures but not causes → repeated repair attempts.
- Section IV-D: recovery today is reactive, cause-blind, and does not store failure knowledge.
- Section V-A: capabilities exist but "are investigated separately… validated in completely different scenarios."
- Section V-A: explicit statement that the opportunity is integration for coding, not inventing recovery itself.
- Section V-B: [21] proves diagnosis+recovery works for general agents but "do[es] not prove directly how these mechanisms work on coding tasks."
- Section VI: "lack of combined failure recovery solutions that integrate reflection, cause analysis, memory, planning, and adaptive execution."
- Table III: no reviewed study is fully explicit on all capabilities in a repository-level coding context.
- Fig. 3: the integrated workflow exists only as a conceptual synthesis.

## 5. What do we still NOT know?
These are the honest unknowns — none of them can be answered from 35 papers alone:
1. **Whether 2025–2026 work outside our corpus already did this.** Our corpus has a knowledge cutoff; this field moves fast. Someone may have published an integrated recovery system for coding agents after our review's search window.
2. **Whether [21]'s diagnosis approach actually transfers to coding.** The review says it is unproven — but we don't know *how well* it transfers until we test it.
3. **Which open agent platform is the right base** (OpenHands [6] is in our corpus as a platform, but practical suitability needs investigation).
4. **What the compute cost will be** — running repository-level agent experiments repeatedly is expensive; the review itself flags computational efficiency as a concern (Section V-C).
5. **Whether small-scale task subsets can support valid experiments** (we may not be able to run full SWE-Bench [19]; subset strategies need checking).
6. **What failure-type distribution coding agents actually show** on repository tasks — needed to design the diagnosis step.

## 6. What literature must we search next to validate it?
*(This is the plan for Step 3 — no searching has been done yet, per instructions.)*

Priority search queries, in order:
1. **Direct overlap check for Candidate B:** "failure recovery" AND ("coding agent" OR "software engineering agent") AND ("self-reflection" OR "root cause") — 2025–2026 papers, arXiv + major venues (ICSE, FSE, ASE, ISSTA, ICLR, NeurIPS).
2. **Coding-specific failure analysis:** "failure taxonomy" / "root cause analysis" / "agent debugging" for LLM coding agents or SWE-Bench trajectories.
3. **What happened after [21]:** citations and follow-ups of "Where LLM Agents Fail and How They Can Learn From Failures" (Zhu et al., 2025) — especially any that target software engineering.
4. **Recovery/process metrics:** "process evaluation" / "trajectory evaluation" / "recovery metrics" for coding agents (validates Candidate F).
5. **Integrated systems:** recent versions/papers of OpenHands, SWE-agent, AutoCodeRover, RepairAgent — check whether newer releases added explicit diagnosis/recovery components.
6. **Failure-aware memory for debugging** (to keep Candidate C's risk assessment honest).

**Decision rule for Step 3:** if searches 1–3 turn up a published system that already integrates diagnosis + reflection + recovery *for repository-level coding with empirical evaluation*, we pivot toward whatever it left open (likely Candidate F or a targeted variant of A). If they do not, Candidate B (with A as core component and F as evaluation backbone) becomes the leading proposal for the final research gap.

---
*End of Step 2. No final gap has been declared. No external literature has been added. No implementation has been started. Only `research_candidate_gaps.md` was created.*
