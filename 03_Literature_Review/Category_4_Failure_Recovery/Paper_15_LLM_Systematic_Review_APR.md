# Paper 15

## Title

A Systematic Literature Review on Large Language Models for Automated Program Repair

**Authors:** Quanjun Zhang et al.

**Year:** 2026 (ACM TOSEM)

**Category:** Systematic Literature Review (Survey)

---

## 1. Problem Statement

Large Language Models (LLMs) have rapidly become one of the most successful approaches for Automated Program Repair (APR). Hundreds of repair techniques have recently been proposed, making it difficult for researchers to understand the current progress, available methods, challenges, and future research opportunities.

This paper provides the first comprehensive systematic literature review of LLM-based Automated Program Repair research.

---

## 2. Methodology

The authors performed a Systematic Literature Review (SLR).

They collected papers published between **2020 and September 2025** using:

- Google Scholar
- ACM Digital Library
- IEEE Xplore

The review process included:

- Manual Search
- Automated Search
- Inclusion & Exclusion Criteria
- Quality Assessment
- Forward & Backward Snowballing

Final dataset:

- **189 high-quality research papers**

The survey analyzes:

- Publication trends
- Popular LLMs
- Program repair scenarios
- Model adaptation techniques
- Benchmarks
- Datasets
- Challenges
- Future research directions

---

## 3. Results

Major findings include:

• Reviewed **189 LLM-based Automated Program Repair papers.**

• Identified **78 different Large Language Models** used for program repair.

• GPT-3.5 and GPT-4 are the most widely used models.

• Program repair research has rapidly increased since 2020.

• Java and Python are the most commonly repaired programming languages.

• Four major adaptation strategies are widely used:

- Fine-tuning
- Few-shot Prompting
- Zero-shot Prompting
- Agent-based Repair

• Agent-based repair has recently become an important research direction because agents can plan, execute, evaluate, and iteratively refine repairs.

---

## 4. Limitations

• Survey paper only; no new repair framework is proposed.

• Includes studies only until September 2025.

• Results depend on the quality of published literature.

• Rapidly evolving LLMs may make some observations outdated.

---

## 5. Difference from My Research

This paper summarizes the entire landscape of LLM-based Automated Program Repair and identifies current research trends, challenges, and future opportunities.

My dissertation proposes a **new Self-Reflection-Based Failure Recovery Framework** specifically for Agentic AI Coding Systems. Rather than reviewing existing research, my work develops a framework where coding agents analyze failures, generate reflective feedback, revise reasoning, and iteratively recover from unsuccessful execution attempts.

---

## Key Contribution

Provides the first comprehensive survey of LLM-based Automated Program Repair by reviewing 189 research papers and identifying the current state, major challenges, and future directions of the field.

---

## Important Keywords

- Automated Program Repair
- APR
- Large Language Models
- LLM
- Program Repair
- GPT-4
- GPT-3.5
- CodeT5
- CodeLlama
- Agent-based Repair
- Fine-tuning
- Zero-shot Prompting
- Few-shot Prompting
- Self-Reflection
- Self-Correction
- Failure Recovery
- Software Engineering