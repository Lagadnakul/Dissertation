# Paper 26

## File Name

Paper_26_Where_LLM_Agents_Fail_and_How_They_Can_Learn_From_Failures.md

## Category

Category 2 – Failure Recovery and Self-Reflection in LLM Agents

## Paper Title

Where LLM Agents Fail and How They Can Learn From Failures

## Authors

Kunlun Zhu,
Zijia Liu,
Bingxuan Li,
Muxin Tian,
Yingxuan Yang,
Jiaxun Zhang,
Pengrui Han,
Qipeng Xie,
Fuyang Cui,
Weijia Zhang,
Xiaoteng Ma,
Xiaodong Yu,
Gowtham Ramesh,
Jialian Wu,
Zicheng Liu,
Pan Lu,
James Zou,
Jiaxuan You

University of Illinois Urbana-Champaign,
Stanford University,
AMD,
University of Toronto,
OpenManus

## Year

2025 (arXiv)

---

## 1. Problem Statement

Large Language Model (LLM) agents integrate planning, memory, reflection, and tool usage to solve complex multi-step tasks. However, these agents frequently experience cascading failures, where one early mistake propagates through subsequent reasoning and actions, ultimately causing complete task failure.

Existing research mainly identifies failure types but lacks a systematic framework for identifying root causes, debugging failures, and enabling agents to learn from their mistakes. This paper addresses that gap by proposing a structured failure taxonomy, benchmark, and debugging framework.

---

## 2. Methodology

The authors introduce three major contributions.

### 1. AgentErrorTaxonomy

A modular taxonomy that categorizes failures into five major components:

- Memory Errors
- Reflection Errors
- Planning Errors
- Action Errors
- System-Level Errors

Each category represents a different source of failure during autonomous task execution.

---

### 2. AgentErrorBench

A benchmark containing systematically annotated failure trajectories collected from real-world LLM agent environments.

The benchmark includes:

- Root-cause annotations
- Step-level error labels
- Actionable debugging feedback

Instead of labeling every visible mistake, the benchmark focuses on identifying the earliest error responsible for the complete failure.

---

### 3. AgentDebug

A debugging framework that enables agents to recover from failures through three stages:

#### Stage 1 – Fine-Grained Analysis

Analyzes every reasoning step and classifies failures using AgentErrorTaxonomy.

#### Stage 2 – Critical Error Detection

Finds the root-cause error responsible for later failures.

#### Stage 3 – Iterative Recovery

Provides targeted corrective feedback.

The agent performs another rollout using the feedback, allowing continuous learning and improved task completion.

---

## 3. Dataset / Benchmark

Benchmark:

AgentErrorBench

Collected From:

- ALFWorld
- WebShop
- GAIA

Dataset Statistics:

- 500+ failed trajectories analyzed
- 200 fully annotated trajectories
- 100 ALFWorld
- 50 WebShop
- 50 GAIA

Five Failure Categories:

- Memory
- Reflection
- Planning
- Action
- System-Level

Evaluation Metrics:

- All-Correct Accuracy
- Step Accuracy
- Root-Cause Detection Accuracy
- Task Success Rate

---

## 4. Results

Main findings:

- Error propagation is the biggest challenge in LLM agents.
- Early mistakes frequently cascade into later failures.
- Memory and reflection failures are the most common root causes.
- AgentDebug achieves 24% higher All-Correct Accuracy than the strongest baseline.
- Step Accuracy improves by approximately 17%.
- Task success improves by up to 26% across ALFWorld, GAIA, and WebShop.
- Root-cause debugging is significantly more effective than correcting every visible error.

---

## 5. Strengths

- First systematic taxonomy for LLM agent failures.
- Introduces a benchmark focused on root-cause analysis.
- Uses real agent trajectories.
- Combines debugging with iterative recovery.
- Demonstrates significant improvements across multiple environments.
- Provides actionable feedback instead of simple error detection.
- Strong experimental evaluation.

---

## 6. Limitations

- Evaluated mainly on general-purpose LLM agents rather than coding-specific agents.
- Does not focus exclusively on software engineering tasks.
- Requires repeated agent rollouts, increasing computational cost.
- Root-cause annotation currently relies on expert human labeling.
- Future work is needed for fully automated debugging.

---

## 7. Relation to My Research

This paper is one of the most important references for my dissertation.

My research focuses on designing a self-reflection-based failure recovery framework for agentic AI coding systems.

AgentDebug provides a strong foundation by showing that identifying the root cause of failures and generating targeted corrective feedback significantly improves agent performance.

However, the paper evaluates general LLM agents rather than autonomous coding agents.

My proposed framework extends these ideas to AI coding systems by combining self-reflection, failure analysis, execution history, and iterative reasoning revision to recover from software engineering failures such as debugging errors, repository navigation failures, tool execution errors, and incorrect code generation.

This paper strongly supports the motivation, literature review, and research gap of my dissertation.

---

## 8. Key Contribution

The paper introduces AgentErrorTaxonomy, AgentErrorBench, and AgentDebug, providing the first comprehensive framework for systematically identifying root-cause failures, debugging LLM agent trajectories, and enabling iterative recovery through targeted feedback.

---

## 9. Keywords

- LLM Agents
- AgentDebug
- AgentErrorTaxonomy
- AgentErrorBench
- Failure Recovery
- Root-Cause Analysis
- Self-Reflection
- Debugging
- Planning
- Memory
- Reflection
- Autonomous Agents
- Iterative Learning
- Error Propagation

---

## My Notes

Importance for Dissertation:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Root-Cause Detection
- Failure Taxonomy
- Agent Debugging
- Iterative Recovery
- Reflection
- Planning
- Memory Errors
- Error Propagation
- Corrective Feedback
- Failure Analysis

Why I Selected This Paper:

This paper is one of the closest matches to my dissertation topic. It introduces a systematic framework for understanding why LLM agents fail and how they can recover using structured debugging and targeted feedback. The concepts of error propagation, root-cause detection, and iterative recovery directly align with my proposed self-reflection-based failure recovery framework for agentic AI coding systems. It will serve as one of the primary references for defining the research gap and motivating the proposed framework.