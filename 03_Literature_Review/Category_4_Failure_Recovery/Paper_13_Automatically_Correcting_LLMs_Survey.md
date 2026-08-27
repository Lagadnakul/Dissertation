# Paper 13
## Title
Automatically Correcting Large Language Models: Surveying the Landscape of Diverse Self-Correction Strategies

**Authors:** Liangming Pan, Michael Saxon, Wenda Xu, Deepak Nathani, Xinyi Wang, William Yang Wang

**Year:** 2023 (Survey Paper)

**Category:** Self-Correction Survey

---

## 1. Problem Statement

Although Large Language Models achieve impressive performance, they still suffer from hallucinations, incorrect reasoning, toxic outputs, and flawed code generation. Existing correction methods are scattered across different research areas, making it difficult to understand the complete landscape of self-correction techniques.

---

## 2. Methodology

This paper presents a comprehensive survey of self-correction methods for LLMs.

The authors classify existing techniques into three major categories:

• Training-Time Correction
• Generation-Time Correction
• Post-Hoc Correction

They also propose a conceptual framework consisting of:

- Language Model (Generator)
- Critic Model (Provides Feedback)
- Refine Model (Improves Output)

The paper reviews different feedback sources including:

- Self-feedback
- External tools
- Knowledge bases
- Reward models
- Human feedback

---

## 3. Results

• Presents one of the earliest comprehensive taxonomies of LLM self-correction.
• Summarizes major self-correction techniques.
• Explains advantages and limitations of each approach.
• Highlights future research directions for autonomous AI systems.

---

## 4. Limitations

• Survey paper only; no new framework proposed.
• Does not implement or experimentally compare methods.
• Published before many recent Agentic AI coding systems.

---

## 5. Difference from My Research

This paper surveys existing self-correction techniques across many NLP tasks.

My dissertation focuses specifically on designing and evaluating a self-reflection-based failure recovery framework for Agentic AI Coding Systems, where coding agents automatically analyze failures, reflect on mistakes, revise their reasoning, and recover during software engineering tasks.

---

## Key Contribution

Provides the theoretical foundation for self-correction and explains how automated feedback can improve LLM reliability.

---

## Important Keywords

- Self-Correction
- Automated Feedback
- Self-Reflection
- Critic Model
- Refine Model
- Hallucination
- Failure Recovery
- Agentic AI
- Large Language Models
- Survey