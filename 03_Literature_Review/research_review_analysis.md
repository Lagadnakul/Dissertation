# Research Review Analysis
## Source Document
**"Self-Reflection and Failure Recovery in Agentic AI Coding Systems: A Systematic Review"**
Manuscript: INFSOF-D-26-01742 (Information and Software Technology)
Authors: Nakul Lagad, Ramizraja Shethwala, Mohammad Arif (PIET, Parul University)
Corpus: 35 studies, published 2023–2026

**Purpose of this file:** To extract and organize, *strictly from the review itself*, what the reviewed literature addresses, how, with what evaluation, and what limitations and unresolved problems remain. No external claims are added. No research gap is invented here — only what the review documents.

> **Note on reference numbering:** Numbers like `[21]` below follow the review's IEEE reference list. The review body sometimes uses corpus IDs like "P26". One important mapping: the body text's **"P26" (Where LLM Agents Fail / AgentErrorTaxonomy, Zhu et al. 2025) = reference `[21]`** in the reference list and in Table III.

---

## 1. Problems Existing Studies Address

The review organizes the 35 studies into six thematic groups (Table I of the review):

| Group | Problem Area Addressed | Studies |
|---|---|---|
| Autonomous Coding Agents | Exploring repositories, code writing, debugging, testing, repository-level software engineering | P01–P06 → [1]–[6] |
| Self-Reflection | Reflective reasoning, iterative improvement, self-evaluation, self-debugging | P07–P12 → [7]–[12] |
| Failure Recovery | Failure detection, failure diagnosis, recovery techniques, automatic repair | P13–P17 → [13]–[17]* |
| Memory Mechanisms | Short-term, long-term, episodic memory, memory retrieval | P18–P22 |
| Planning and Tool Usage | Task decomposition, execution planning, tool selection, command execution, workflow modification | P23–P29 |
| Evaluation Benchmarks | Benchmark datasets, evaluation frameworks, task-success measurement, agent performance analysis | P30–P35 |

*Note: the review's Table III maps specific works to reference numbers that do not always align with the corpus P-numbers; per-study mapping is given where used below.

### The core underlying problem (stated by the review, Sections I–II)
- Autonomous coding agents fail due to: **wrong task interpretation, wrong planning, mistakes in repository navigation, wrong file selection, wrong code generation, improper tool use, and failed tests** (Sections I, II-B).
- Software engineering steps are interdependent, so **an error made in an early stage propagates to later stages** (cascading failures) (Sections II-B, IV-D).
- A key limitation: **"an agent can recognize the occurrence of an execution failure without being able to understand its cause, leading to inefficiency or repetition of repair attempts"** (Section I).

### Problems addressed per study (from Table III)

**Repository / coding agent frameworks:**
- [3] AutoCodeRover — exploring repositories, locating failures, proposing patches, validating them.
- [4] SWE-agent — improving navigation, editing, testing, debugging via agent–computer interface design.
- [5] RepairAgent — autonomously localizing faults, generating patches, executing tools, validating repairs iteratively.
- [6] OpenHands — providing an open platform for building, running, and evaluating generalist software agents.
- [1] LLM-based multi-agent systems survey — coordination and architectural problems across the SDLC.
- [2] AI Teammates / SE 3.0 — how autonomous coding agents reshape software engineering in practice.

**Self-reflection and iterative reasoning:**
- [7] Reflexion — using verbal self-feedback to improve future attempts without weight updates.
- [8] SELF-REFINE — separating generation, self-evaluation, and refinement without retraining.
- [9] Renze & Guven — empirical study of reflective reasoning's effect on problem-solving.
- [10] Self-Debug — evaluating generated programs, understanding execution feedback, debugging logical errors.
- [11] ExpeL — gaining, storing, and using lessons from successful and unsuccessful experiences.
- [12] Reflective multi-agent collaboration — agents exchanging comments to improve intermediate solutions.

**Failure recovery, debugging, repair:**
- [13] Survey of LLM self-correction — grouping correction methods into feedback, refinement, verification, iterative revision.
- [14] OS-Copilot — continual self-improvement through interaction, tool execution, experience reuse.
- [18] Systematic review of LLM-based automated program repair — fault localization, patch generation, validation.
- [21] (= P26) AgentErrorTaxonomy / AgentErrorBench / AgentDebug — systematic failure classification, annotated failure trajectories, root-cause localization, feedback, iterative recovery.

**Memory:**
- [15] A-MEM — dynamic association, organization, evolution, and retrieval of agent experiences.
- [16] MIRIX — episodic, semantic, procedural, resource, and knowledge memories.
- [17] LOCOMO — evaluating long-term conversational memory, temporal reasoning, consistency.

**Planning and tool use:**
- [22] TPTU — perception, planning, tool use, learning, reflection, memory, summarization.
- [23] LLM-Planner — high-level planning and dynamic grounded replanning.
- [24] API-Bank — tool calling, tool retrieval, tool-call planning, executable tool use.
- [25] Survey of tool-augmented LLMs — discovering, selecting, calling, learning to use tools.

**Benchmarks, evaluation, architectures:**
- [19] SWE-Bench — repository-level benchmark from real GitHub issues.
- [20] AgentBench — evaluating reasoning, planning, decision-making, interaction across environments.
- [26] Agent-as-a-Judge — evaluating complex agent trajectories using other agents.
- [27] RedCode — benchmarking risky code execution and generation (safety).
- [28]–[31] Surveys of agent architectures and agentic AI (reasoning, planning, memory, reflection, tool calling).
- [32] Vibe coding vs. agentic coding — conceptual differentiation of prompt-based vs. autonomous goal-oriented coding.
- [33] SICA — a self-improving coding agent that modifies itself to enhance efficiency.
- [34] 2025 AI Agent Index — documenting technical capability, autonomy, safety, transparency of 30 deployed agents.
- [35] SMART-LLM — multi-agent robot task decomposition, coalition formation, resource allocation.

---

## 2. Methods / Approaches Existing Studies Use

### Self-reflection methods (Section IV-B)
- **Verbal reinforcement / self-feedback loops:** agents generate verbal feedback from previous attempts and condition the next attempt on it (Reflexion [7]).
- **Generate → evaluate → refine loops:** separate generation, self-evaluation, and refinement stages (SELF-REFINE [8]).
- **Execution-feedback self-debugging:** run the program, interpret output, reason about logical errors, regenerate (Self-Debug [10]).
- **Experiential learning:** extract and store "lessons" from successful and unsuccessful episodes for reuse (ExpeL [11]).
- **Reflective multi-agent cooperation:** specialized agents give each other feedback on intermediate solutions [12].
- The typical reflective cycle described by the review: *generation → execution/evaluation → detection of undesirable outcome → feedback generation → modification of the next solution* (Section II-C).

### Memory methods (Sections II-E, IV-C)
- **Short-term vs. long-term memory:** short-term holds current-task context (inputs, logs, intermediate plans, tool outputs); long-term stores past failures, debugging knowledge, repository information, good solutions, tool-use experience.
- **Structured memory types:** episodic, semantic, procedural (and in MIRIX also resource and knowledge memory) [16].
- **Dynamic association and memory evolution:** A-MEM structures experiences and retrieves relevant information during future reasoning [15].
- **Memory as active reasoning support:** recent memory systems interact with reasoning, planning, and action modules during decision-making, supplying previously used solutions for navigation, tool choice, and debugging (Section IV-C).

### Planning and tool-use methods (Sections II-F, IV-E)
- **Hierarchical task decomposition:** breaking high-level goals into subtasks (exploration, dependency analysis, modification, testing, debugging, validation) [22], [23].
- **Grounded replanning:** revising plans dynamically in reaction to environment feedback (LLM-Planner [23]).
- **Tool-augmented execution:** terminals, repositories, compilers, debuggers, test frameworks, version control, documentation, APIs [4], [5], [11], [12], [25].
- **Feedback loop pattern:** choose action → invoke tool → observe output → adjust future actions (Section II-F).

### Failure recovery and repair methods (Sections II-D, IV-D)
- **Automated program repair (APR) pipeline:** fault localization → patch proposal → patch validation via test suites ([18] survey; [5] RepairAgent).
- **Iterative execution-based debugging:** repeated analysis of execution results, changing implementation approach across iterations instead of stopping at first failure (Section IV-D).
- **Failure-taxonomy-driven recovery:** classify failures, localize root cause in the agent trajectory, generate feedback, perform iterative recovery (AgentDebug, [21]).
- **The common recovery-loop structure identified by the review (Section II-D):**
  1. Failure detection (execution logs, compiler messages, test results, runtime exceptions, tool output)
  2. Failure cause identification
  3. Feedback generation
  4. Revision of the execution plan
  5. Execution of the revised plan
  6. Repeat until success or a termination criterion is met.

### Self-correction taxonomy (from survey [13], Section IV-B)
Existing correction methods grouped into: iterative improvement, feedback-based correction, verification via external information sources, self-consistency reasoning, and adaptive revision.

### Evaluation methods
- Benchmark-driven task-success evaluation (SWE-Bench [19], AgentBench [20], API-Bank [24], RedCode [27]).
- Agent-based judging of trajectories (Agent-as-a-Judge [26]).
- Documenting deployed-agent capabilities without experiments (AI Agent Index [34]).

---

## 3. Datasets / Benchmarks / Evaluation Methods Used

(Compiled from Table III "Evaluation Context" column and Section II-G.)

| Benchmark / Environment | Used by | What it measures |
|---|---|---|
| **SWE-Bench** [19] | [3], [4], [33] | Real GitHub issues; repository understanding, code modification, patch generation, test verification |
| **HumanEvalFix** | [4] | Program-level fixing tasks |
| **AgentBench** [20] | [20] | Reasoning, planning, decision-making, interaction across various interactive environments |
| **API-Bank** [24] | [24] | API call, retrieve-and-call, plan-retrieve-and-call tasks |
| **RedCode-Exec / RedCode-Gen** [27] | [27] | Code-execution risk and malicious code generation (safety) |
| **AgentErrorBench** (part of [21]) | [21] | Annotated failure trajectories; evaluated on **ALFWorld, GAIA, WebShop** |
| **LOCOMO** [17] | [17] | Long-term conversational memory benchmark |
| **ALFRED** (embodied environment) | [23] | Grounded planning/replanning |
| **AI2-THOR** simulation + physical robots | [35] | Multi-agent robot task planning |
| **LiveCodeBench + synthetic benchmarks** | [33] | Coding-agent performance alongside SWE-Bench |
| **AIDev dataset** (cited via [19] in Section II-G) | — | Large-scale AI-assisted development activity (pull requests, repository actions) |
| Literature synthesis / case studies | [1], [2], [13], [18], [25], [28]–[31], [32] | Surveys and conceptual analyses |
| Developer information for 30 deployed agents | [34] | Non-experimental documentation |

**Metrics typically used (Sections II-G, IV-D):** task success rate, execution correctness, benchmark completion, correctness of the task itself.

**What the review says benchmarks miss (Section II-G):** existing benchmarks "usually focus on the output rather than the process of reasoning, planning, memory usage, self-evaluation or recovering from failures."

---

## 4. Limitations Reported BY the Individual Studies

(Directly from Table III, "Major Limitation" column — reference numbers as in the review.)

| Ref. | Study | Reported major limitation |
|---|---|---|
| [1] | Multi-agent SE survey | Wide coverage, but lacks empirical analysis of failure-recovery integration |
| [2] | AI Teammates / SE 3.0 | Emphasizes new development techniques, not explicit root-cause identification and failure recovery |
| [3] | AutoCodeRover | Recovery strategy is still patch-based without reuse of failure knowledge between different tasks |
| [4] | SWE-agent | Depends heavily on interface design and lacks root-cause-oriented recovery |
| [5] | RepairAgent | Focuses on fixing source-code problems rather than reasoning and planning issues |
| [6] | OpenHands | Offers infrastructure and evaluation framework without dedicated failure-recovery mechanisms |
| [7] | Reflexion | Recovery depends on the quality of agent reflections and does not include detailed diagnosis of execution failures |
| [8] | SELF-REFINE | Improves outputs through iterations but has no persistent memory or detailed execution-failure diagnosis |
| [9] | Self-reflection effects | Reflection may be ineffective on some tasks and may produce incorrect reasoning |
| [10] | Self-Debug | Measures individual programs rather than repository-based coding-agent trajectories |
| [11] | ExpeL | Transfer of experience may become ineffective when tasks differ greatly from stored examples |
| [12] | Reflective multi-agent | Requires additional communication and coordination |
| [13] | Self-correction survey | Current approaches are fragmented, task-specific, and difficult to evaluate with a common methodology |
| [14] | OS-Copilot | Focuses on general computer interaction; limited specialization for repository-related code defects |
| [15] | A-MEM | Focuses on memory organization rather than failure diagnosis or recovery of coding agents |
| [16] | MIRIX | Memory coordination can be complex and introduce additional storage and computational overhead |
| [17] | LOCOMO | Evaluates conversational memory but does not consider software-engineering agents |
| [18] | LLM APR survey | Focuses on software faults and patch correctness rather than execution trajectories of autonomous agents |
| [19] | SWE-Bench | Tests final issue solving but provides limited information about intermediate failures and recovery |
| [20] | AgentBench | Provides broad evaluation but does not focus on software-specific root-cause analysis and recovery |
| [21] | AgentErrorTaxonomy / AgentDebug | Offers explicit failure analysis and iterative recovery, **but evaluates them in general agent settings (ALFWorld, GAIA, WebShop) rather than repository-level software engineering** |
| [22] | TPTU | Provides a conceptual framework but lacks evaluation in programming environments |
| [23] | LLM-Planner | Demonstrates replanning outside software engineering; lacks repository-level coding evaluation |
| [24] | API-Bank | Limited evaluation of persistent learning, root-cause identification, and long-term recovery |
| [25] | Tool-use survey | Broad survey without empirical comparison of software-engineering recovery techniques |
| [26] | Agent-as-a-Judge | Evaluation quality depends on the judging agent |
| [27] | RedCode | Assesses safety but does not address post-failure recovery |
| [28] | Agent architectures survey | Extensive architectural discussion but limited empirical analysis of failure recovery |
| [29] | Rise of Agentic AI review | Broad scope makes an in-depth study of self-reflective recovery in autonomous coding systems difficult |
| [30] | Agentic AI survey | Focuses on architectures and governance rather than coding-specific execution recovery |
| [31] | LLM autonomous agents survey | General taxonomy without a specialized recovery architecture based on root-cause analysis |
| [32] | Vibe vs. agentic coding | Provides conceptual insights but lacks extensive empirical evaluation |
| [33] | SICA | Globally optimizes agent implementation without diagnosing and recovering from individual task execution failures |
| [34] | AI Agent Index | Uses mainly publicly available information without experimental evaluation |
| [35] | SMART-LLM | Robotic-domain assumptions restrict applicability to repository-level software-engineering failure scenarios |

---

## 5. Limitations Reported BY the Systematic Review Itself

These are the review's own conclusions about the state of the field (Sections IV, V-A, V-B, VI).

### A. Fragmentation — capabilities studied separately
- "There exists a lack of cohesion in the literature regarding reflection, memory, planning, debugging, and recovery" (Section I).
- "These capabilities are investigated separately from different perspectives and are validated in completely different scenarios" (Section V-A).
- "Current investigations continue to examine each one of these aspects independently, producing fragmented autonomous workflows that cannot ensure their robustness in the course of multi-step processes" (Section IV-E).
- Conclusion (Section VI): "all of these features are studied independently. The review identified a gap related to the lack of combined failure recovery solutions that integrate reflection, cause analysis, memory, planning, and adaptive execution."

### B. Self-reflection limitations (Section IV-B)
1. Most existing models treat self-reflection as something that occurs **after execution rather than a continuous process** during execution.
2. Present models evaluate **results of execution rather than the reasoning process itself** — "reflection will only realize that there has been some sort of mistake made but will not explain why the mistake has been made and how reasoning can be changed in the future to prevent such mistakes."
3. Reflection "does not suffice to ensure robust autonomous functioning" because improvement presupposes storing information about past tasks (Section IV-B).

### C. Memory limitations (Sections II-E, IV-C)
1. Most memory systems focus on **accessing information, not analyzing the quality of memories** — faulty memories continue to affect reasoning.
2. **Poor integration** of memory with reflective reasoning and execution monitoring — the agent cannot decide which experiences to save, modify, or delete after success or failure.
3. Retrieval relies heavily on **similarity search**, which may miss valuable experiences in new situations.
4. Retrieved memories may be **irrelevant, outdated, or contradictory** (Section II-E).
5. Memory methods "mostly deal with increasing the availability of the information rather than solving the problems connected with failed execution processes" (Section IV-C).

### D. Failure-recovery limitations (Sections II-D, IV-D)
1. Most recovery mechanisms are **reactive** — "Most of the current systems do not conduct recovery until there is an actual failure."
2. Systems "reattempt previous reasoning with slight changes or develop new implementations" **without determining the reasons for failures**.
3. They lack methods for **differentiating reasoning errors from execution errors**.
4. They do not **store failure information for future use** — "agents tend to make the same reasoning errors again and again."
5. APR-style approaches "treat faults as isolated source code issues and fail to take into consideration the reasoning process behind autonomous decision making" (Section IV-D).
6. Failures are **cumulative/cascading**: "one initial reasoning error cascades into a series of planning mistakes, ultimately leading to total failure of the task" (Section IV-D).

### E. Evaluation limitations (Sections II-G, IV-D, V-A, VI)
1. Benchmarks "focus on the output rather than the process" — reasoning, planning, memory use, self-evaluation, and recovery are not measured (Section II-G).
2. "Not much work has been done on the estimation of the recovery capacity of an agent" — including finding failure reasons, changing reasoning/execution, and recovering at intermediate execution (Section IV-D).
3. "There is a lack of approaches for the assessment of the effectiveness of the failure recovery process, its efficiency, root cause detection, and proactive failure prevention" (Section VI).

### F. The one closest existing work and its boundary (Section V-A, V-B)
- Study [21] (P26: AgentErrorTaxonomy + AgentErrorBench + AgentDebug) is the only work offering explicit failure taxonomy, root-cause localization, feedback, and iterative recovery.
- **However**, it "assesses these mechanisms on ALFWorld, GAIA, and WebShop datasets and not at a software engineering level." The review states: "their results allow us to claim that failure diagnosis and recovery is possible, but **do not prove directly how these mechanisms work on coding tasks** which imply code navigation, modifications, testing, build failures, dependencies, and code execution at repository level."

---

## 6. Future-Work Directions Mentioned in the Review

(Section V-C "Future Research Directions," plus Section VI.)

1. **Integrated autonomous recovery frameworks** combining reasoning, planning, self-reflection, memory management, debugging, and adaptive execution — with interaction between components throughout the entire software-engineering process, instead of isolated recovery techniques.
2. **Root-cause analysis in autonomous coding agents** — "tracing the process of execution failures throughout several reasoning phases, separating the problem into planning mistakes and execution flaws, finding connections between navigating the repository, using tools, reasoning, and the execution process outcome."
3. **Advanced memory architectures** — beyond storage toward contextual adaptation and dynamic learning; three named directions: **dynamic memory prioritization, experience abstraction, and failure-aware memory**; memory must judge whether stored data is relevant and applicable to the current task.
4. **Recovery-oriented benchmarks and evaluation methods** — going beyond task execution to numerical metrics of recovery performance: "recovery accuracy, cause identification, adaptation, planning, execution efficiency, error avoidance, computational cost, and learning."
5. **Computational efficiency of recovery** — adaptive recovery techniques balancing robustness and cost: reflection optimization, recovery triggering, planning depth, resource-efficient reasoning.
6. **From reactive recovery to proactive execution management** — monitoring execution paths, predicting failure probability, detecting hazardous reasoning patterns, planning ahead; "predictive failure detection, uncertainty-based planning, and continuous execution monitoring."

---

## 7. Unresolved Problems / Open Challenges That Appear Repeatedly

Each item below recurs in multiple places in the review (Table III limitations, Section IV subsections, Section V, Section VI).

### 7.1 No root-cause-oriented recovery in coding agents (most frequent)
Appears in limitations of: [2], [4], [7], [8], [15], [20], [24], [31], [33]; and in Sections I, II-D, IV-D, V-A, V-C, VI.
Agents detect *that* a failure occurred but not *why*; they retry with slight variations and repeat the same reasoning errors.

### 7.2 No integration of reflection + root-cause analysis + memory + planning + recovery
Appears in limitations of: [1], [3], [6], [8], [13], [28]; and in Sections I, IV-E, V-A, V-B, VI.
All components exist individually; no evaluated system combines them into one recovery process for coding.

### 7.3 The only explicit failure-recovery system [21] is not validated on repository-level coding
Stated in Table III ([21]), Section V-A, and Section V-B. Evaluated on ALFWorld, GAIA, WebShop — leaving "the problem of coding uncovered" (Section V-B).

### 7.4 Memory is not connected to failure, reflection, or execution monitoring
Appears in limitations of: [3], [8], [11], [15], [24]; and in Sections II-E, IV-C.
Memory stores and retrieves, but does not learn from failures, judge memory quality, or decide what to save/update/delete after success or failure.

### 7.5 Reflection is post-execution and outcome-focused, not continuous or cause-aware
Appears in limitations of: [7], [8], [9]; and in Section IV-B.
Reflection detects that a mistake happened but does not explain why or how to prevent recurrence.

### 7.6 Evaluation measures final outcomes, not the recovery process
Appears in limitations of: [19], [20], [24], [26], [27]; and in Sections II-G, IV-D, V-A, VI.
No standard metrics for recovery accuracy, diagnosis quality, repeated-failure reduction, recovery latency, or recovery cost.

### 7.7 Recovery is reactive, not proactive
Sections II-D, IV-D, V-C. Systems wait for an actual failure; no prediction of failure probability or detection of hazardous reasoning patterns.

### 7.8 Fragmented, task-specific methods hard to compare
Limitations of [13], [25]; Section V-A. Approaches are validated in completely different scenarios with no common methodology.

---

## 8. Findings Most Relevant to Failure Recovery and Self-Reflection in Agentic Coding Systems

1. **The recovery-loop structure is known but incompletely implemented** (Section II-D): detection → cause identification → feedback → plan revision → re-execution. The review finds existing systems typically implement detection and retry, but skip genuine cause identification and failure-memory storage.

2. **Study [21] (AgentErrorTaxonomy / AgentErrorBench / AgentDebug) is the single most relevant prior work.** It is the only reviewed study rated "E" on all five capabilities (self-reflection, memory, planning, tool use, recovery) in Table III, and the only one with an explicit failure taxonomy + root-cause localization + iterative recovery. Its decisive boundary: evaluation only in general agent environments (ALFWorld, GAIA, WebShop), not repository-level coding (Sections V-A, V-B).

3. **Reflection works but is insufficient alone** (Section IV-B): Reflexion [7], SELF-REFINE [8], Self-Debug [10], and the empirical study [9] show reflection improves task performance ("reflection acts as an internal supervisor"), yet it is post-execution, outcome-focused, quality-dependent, and may even produce incorrect reasoning [9].

4. **Failures in coding agents are cumulative and multi-type** (Section IV-D): failures arise at task interpretation, planning, repository navigation, file selection, code generation, tool use, API invocation, compilation, testing, and debugging — and "one initial reasoning error cascades into a series of planning mistakes." Recovery may require revising code, changing the plan, modifying tool actions, retrieving experience, or re-interpreting the task (Section V-B).

5. **Memory could support recovery but currently does not** (Sections II-E, IV-C): memory is positioned to supply "previous debugging experience, execution trace, patches, and failure recovery methods whenever similar failures would occur," yet current systems fail to combine memory with reflection, execution monitoring, and failure analysis.

6. **The review explicitly defines the research opportunity** (Section V-A): "It must be noted that the research opportunity in question is not about inventing failure recovery per se. On the contrary, it lies in **developing and implementing an effective failure recovery approach for autonomous coding systems based on self-reflection**. This kind of research can be developed on the basis of previous failure analysis studies." It is framed as "a **coding-specific integration and evaluation issue** rather than as something new in the field of failure recovery or root-cause analysis."

7. **The review states the core unresolved question** (Section V-B): "whether an autonomous agent is capable of reflecting, remembering, debugging, or recovering from failure is not in question. Instead, **the key challenge is how to adapt such mechanisms to particular features of the autonomous software engineering execution.**"

8. **The review proposes a target workflow** (Fig. 3): Task Execution → Failure Detection → Root Cause Analysis → Self-Reflection → Memory Retrieval → Adaptive Replanning → Re-execution → Reliable Agentic Coding System. This is presented as "synthesized from the reviewed literature," i.e., a conceptual integration that no reviewed study has implemented end-to-end for coding.

9. **Recovery-oriented evaluation metrics are specified** (Section V-A): "failure diagnosis accuracy, recovery success rate, recovery attempts, decreased number of repeated failures, tool invocation, execution cost, recovery latency, and correctness of software." The review says these are needed to determine "whether self-reflection is truly enhancing the reliability of autonomous coding trajectories or just increasing the number of executions."

10. **Benchmark infrastructure for coding exists** (SWE-Bench [19], used by [3], [4], [33]) but reports final issue resolution, not intermediate failures or recovery behavior (Table III, Section II-G).

---

## WHAT WE KNOW SO FAR

*Summary of the strongest unresolved problems documented in the review. These are stated by the review — nothing is added.*

1. **All the pieces exist; the combination does not.** Self-reflection, memory, planning, tool use, debugging, and failure recovery are each studied and validated — but always separately, in different scenarios. No reviewed work integrates them into one recovery process for autonomous coding (Sections I, V-A, VI).

2. **Coding agents detect failures but do not diagnose them.** Existing systems recognize that execution failed, then retry with slight variations or regenerate. They lack root-cause identification, cannot distinguish reasoning errors from execution errors, and do not store failure knowledge — so they repeat the same mistakes (Sections I, II-D, IV-D).

3. **The one system that does diagnosis + recovery was never tested on coding.** AgentErrorTaxonomy/AgentErrorBench/AgentDebug [21] provides failure classification, root-cause localization, feedback, and iterative recovery, but only on general agent benchmarks (ALFWorld, GAIA, WebShop). Whether it works for repository-level coding — with code navigation, build failures, dependencies, and tests — is explicitly left unproven by the review (Sections V-A, V-B).

4. **Memory exists but is not failure-aware.** Current memory systems store and retrieve experiences but are not integrated with reflection, execution monitoring, or failure analysis; they cannot judge memory quality or decide what to save/update/delete after a failure (Sections II-E, IV-C).

5. **Reflection is after-the-fact and outcome-focused.** It tells the agent that something went wrong, not why, and it is not continuous during execution (Section IV-B).

6. **Nobody measures recovery.** Benchmarks (SWE-Bench, AgentBench, API-Bank, RedCode) measure final task success. There are no established metrics or benchmarks for recovery accuracy, diagnosis quality, repeated-failure reduction, recovery latency, or recovery cost (Sections II-G, IV-D, VI).

7. **Recovery is reactive everywhere; proactive failure prevention is an open direction** named by the review (predictive failure detection, hazardous-pattern monitoring, uncertainty-based planning) but not implemented by any reviewed study (Section V-C).

**In one sentence (the review's own framing):** the open problem is not whether agents can reflect, remember, debug, or recover — it is **how to adapt and integrate these mechanisms for repository-level software-engineering execution, and how to evaluate that recovery actually works** (Section V-B).

---
*End of analysis. This file documents only what is contained in the systematic review manuscript INFSOF-D-26-01742. No research gap has been invented, no framework proposed, and no implementation started.*
