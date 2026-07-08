# Paper 02

## Title

AutoCodeRover: Autonomous Program Improvement

---

## Authors

Yuntong Zhang

Haifeng Ruan

Zhiyu Fan

Abhik Roychoudhury

---

## Publisher

ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA)

---

## Year

2024

---

## Category

Failure Recovery

Program Repair

Autonomous Software Engineering

---

## Importance

⭐⭐⭐⭐⭐ (5/5)

Core Research Paper

---

# Research Problem

Current AI coding assistants such as GitHub Copilot mainly generate code but cannot autonomously improve existing software. Real software engineering also involves fixing bugs, adding features, understanding large codebases, and maintaining software. Existing LLM-based agents struggle to identify the correct bug location and understand project structure before generating a fix.

---

# Methodology

The authors proposed a new framework called **AutoCodeRover**.

Instead of directly asking an LLM to generate a patch, AutoCodeRover performs the following workflow:

• Reads the GitHub issue.

• Searches relevant project files using Abstract Syntax Tree (AST).

• Retrieves important classes, methods, and code snippets through Context Retrieval APIs.

• Performs iterative context search to better understand the issue.

• Uses Spectrum-Based Fault Localization (SBFL) when test cases are available.

• Generates a software patch.

• Validates the generated patch using test cases and retries if necessary.

---

# Workflow

GitHub Issue

↓

Issue Understanding

↓

Context Retrieval

↓

AST-Based Code Search

↓

Fault Localization (Optional)

↓

Patch Generation

↓

Patch Validation

↓

Final Patch

---

# Key Findings

• AutoCodeRover successfully automates program improvement.

• AST-based code search improves understanding of large software projects.

• Iterative context retrieval helps identify the root cause more accurately.

• Fault Localization further improves repair performance.

• The framework performs autonomous software maintenance with low cost.

---

# Results

The framework was evaluated on SWE-bench and SWE-bench Lite.

Main results:

• Solved 57 GitHub issues on SWE-bench Lite.

• Achieved 19% success rate (Pass@1).

• Achieved 26% success rate (Pass@3).

• Average execution time: about 4 minutes per issue.

• Average cost: only $0.43 per issue.

• Outperformed Swe-agent on SWE-bench Lite while using significantly fewer tokens.

---

# Limitations

• The framework mainly focuses on bug fixing and feature implementation.

• It does not perform explicit self-reflection before generating a repair.

• Error analysis is limited.

• The repair process is mostly retrieval-driven instead of reflection-driven.

• It still struggles with difficult software engineering tasks.

• Better reasoning and recovery strategies are required.

---

# Research Gap

Although AutoCodeRover improves autonomous software repair using AST-based search and iterative context retrieval, it does not include a dedicated Self-Reflection mechanism that allows the AI to analyze its own mistakes before attempting another repair.

There is also no Failure Recovery Framework that repeatedly learns from previous failed attempts.

This creates an opportunity for future research.

---

# Relation to My Dissertation

AutoCodeRover is one of the closest existing works to my dissertation.


• Detect failures

• Analyze why they failed

• Perform self-reflection

• Generate improved repair strategies

• Iteratively recover until the task succeeds

Instead of only retrieving better code context, my framework focuses on intelligent recovery after failures.

---

# Keywords

AutoCodeRover

Program Repair

Autonomous Software Engineering

Large Language Models

GitHub Issues

AST

Context Retrieval

Fault Localization

Patch Generation

SWE-bench

Failure Recovery

Self-Reflection

---

# Five Research Questions

## 1. What problem does the paper solve?

The paper solves the problem of automatically improving existing software by fixing GitHub issues without human intervention.

---

## 2. What methodology is used?

The authors propose AutoCodeRover, which combines:

• LLM

• AST-Based Code Search

• Context Retrieval APIs

• Spectrum-Based Fault Localization

• Patch Generation

• Patch Validation

---

## 3. What results are achieved?

AutoCodeRover successfully solved real GitHub issues with:

• 19% Pass@1

• 26% Pass@3

• 57 issues solved

• Average cost of $0.43

• About 4 minutes per issue

---

## 4. What are the limitations?

The framework lacks:

• Self-Reflection

• Intelligent Failure Analysis

• Iterative Recovery Strategy

• Learning from previous failed attempts

---

## 5. How is my research different?

AutoCodeRover focuses on retrieving better code context and generating patches.

My dissertation proposes a Self-Reflection-Based Failure Recovery Framework where AI first understands why it failed, reflects on the failure, modifies its strategy, and retries until the task is completed successfully.

---

# One-Line Summary

AutoCodeRover introduces an autonomous software engineering framework that combines LLMs, AST-based code search, and fault localization to automatically resolve GitHub issues, providing a strong baseline for future research on self-reflection-based failure recovery.

---

# Can This Paper Help My Framework?

## Yes ✅

Ideas I can reuse:

• Context Retrieval

• AST-Based Code Search

• Patch Validation

• SWE-bench Evaluation

• GitHub Issue Workflow

---

## What limitation can I solve?

• Add Self-Reflection Layer

• Add Failure Analysis Module

• Add Iterative Repair Loop

• Improve autonomous recovery after failed patch generation

---

## Which experiment can I adopt?

Evaluate my framework on SWE-bench Lite using:

• Task Success Rate

• Recovery Success Rate

• Execution Time

• Cost

• Number of Repair Attempts

---

## Which evaluation metrics can I borrow?

• Pass@1

• Pass@3

• Success Rate

• Cost per Task

• Execution Time

• Patch Correctness

---

# Citation

Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous Program Improvement. Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2024).