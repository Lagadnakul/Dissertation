# Paper 19

## Title
A Self-Improving Coding Agent

## Authors
Maxime Robeyns, Martin Szummer, Laurence Aitchison

## Year
2025

---

## 1. Problem Statement

Current LLM-based coding agents can solve software engineering tasks but cannot autonomously improve their own architecture or codebase. Existing approaches usually require a separate meta-agent or manual intervention for optimization.

---

## 2. Methodology

The authors propose a Self-Improving Coding Agent (SICA) that can modify its own source code through reflection and benchmarking.

Main methodology:

- Self-referential coding agent
- Autonomous code editing
- Reflection-based improvement loop
- Benchmark-driven optimization
- Archive of previous agent versions
- Evaluation using SWE-Bench Verified and LiveCodeBench

---

## 3. Results

- SWE-Bench Verified performance improved from **17% to 53%**
- Improved LiveCodeBench performance
- Reduced execution time
- Lower operational cost
- Successfully improved its own coding framework over multiple iterations

---

## 4. Limitations

- High computational cost during self-improvement
- Improvement depends on benchmark quality
- Difficult to generate consistently novel improvement ideas
- Does not update LLM weights; only modifies the agent framework
- Limited evaluation iterations

---

## 5. Difference from My Research

This paper develops a self-improving coding agent capable of editing its own codebase.

My research proposes a **Self-Reflection-Based Failure Recovery Framework** that enables coding agents to analyze failures, generate reflective feedback, revise reasoning, and recover from unsuccessful execution attempts instead of focusing only on self-improvement.

---

## Key Contribution

Introduced the first self-improving coding agent (SICA) capable of autonomously editing and optimizing its own codebase using reflection, benchmarking, and iterative improvement.

---

## Keywords

- Self-Improving Agent
- Coding Agent
- Self-Reflection
- Autonomous Software Engineering
- SWE-Bench
- LiveCodeBench
- Agentic AI
- Failure Recovery
- Meta-Agent
- LLM Agents