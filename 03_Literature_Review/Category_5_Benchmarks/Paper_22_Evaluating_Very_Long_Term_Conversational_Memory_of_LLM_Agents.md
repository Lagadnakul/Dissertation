# Paper 22

## File Name

Paper_22_Evaluating_Very_Long_Term_Conversational_Memory_of_LLM_Agents.md

## Category

Category 5 – Agent Memory Evaluation

## Paper Title

Evaluating Very Long-Term Conversational Memory of LLM Agents

## Authors

Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, Yuwei Fang

## Year

2024 (ACL)

---

## 1. Problem Statement

Most existing conversational AI systems are evaluated only on short conversations consisting of a few chat sessions. These benchmarks cannot accurately measure whether an LLM agent can remember information over very long periods. The authors aim to create a benchmark for evaluating long-term conversational memory.

---

## 2. Methodology

The authors introduce **LOCOMO (Long Conversational Memory)**, a benchmark for evaluating long-term memory in LLM agents.

Their pipeline consists of:

### 1. Persona Generation
Each virtual agent is assigned a unique personality.

### 2. Temporal Event Graph
Each agent receives a timeline of life events connected through temporal and causal relationships.

### 3. Memory-Based Agent
Each agent maintains:
- Short-term memory
- Long-term memory
- Reflection module
- Retrieval mechanism

### 4. Human Verification
Generated conversations are manually verified and corrected for consistency.

The benchmark evaluates three major tasks:

- Question Answering
- Event Summarization
- Multi-modal Dialogue Generation

---

## 3. Dataset / Benchmark

Dataset:
- LOCOMO

Dataset Statistics:
- Around 600 dialogue turns
- Around 16K tokens
- Up to 32 conversation sessions

Evaluation Tasks:
- Single-hop QA
- Multi-hop QA
- Temporal reasoning
- Commonsense reasoning
- Adversarial reasoning
- Event summarization
- Multi-modal dialogue generation

Models Evaluated:
- GPT-4 Turbo
- Claude 3 Sonnet
- Gemini Pro
- GPT-3.5
- Llama
- Mistral
- RAG systems

Evaluation Metrics:
- F1 Score
- FactScore
- BLEU
- ROUGE
- MMRelevance

---

## 4. Results

Main findings:

- Long-context LLMs perform better than normal LLMs.
- RAG improves memory recall.
- Temporal reasoning remains difficult.
- Multi-hop reasoning is challenging.
- Human performance is still much better than current LLMs.
- Existing models struggle with very long conversations.

---

## 5. Strengths

- First benchmark for very long conversational memory.
- Large-scale realistic conversations.
- Covers multiple reasoning tasks.
- Includes temporal and causal reasoning.
- Human-verified dataset.
- Supports multimodal conversations.

---

## 6. Limitations

- Mainly evaluates conversational agents.
- Does not evaluate software engineering tasks.
- Focuses on memory evaluation rather than memory improvement.
- Does not provide a new recovery mechanism.

---

## 7. Relation to My Research

This paper is highly relevant because my dissertation also depends on long-term memory.

My self-reflection framework can be evaluated using benchmarks similar to LOCOMO to measure whether coding agents remember previous failures, debugging attempts, and recovery history over long interactions.

---

## 8. Key Contribution

The paper introduces LOCOMO, the first benchmark specifically designed to evaluate very long-term conversational memory, temporal reasoning, and event understanding in LLM agents.

---

## 9. Keywords

- LOCOMO
- Long-Term Memory
- LLM Agents
- Conversational Memory
- Temporal Reasoning
- Event Graph
- Reflection
- Retrieval
- Multi-Hop Reasoning
- Memory Evaluation

---

## My Notes

Importance for Dissertation:
⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:
- Memory Evaluation
- Long-Term Memory
- Reflection
- Retrieval
- Event Timeline
- Temporal Reasoning

Why I Selected This Paper:

It provides one of the best benchmarks for evaluating long-term memory. Although it focuses on conversational agents, many evaluation ideas can be adapted for measuring memory and recovery performance in AI coding agents.