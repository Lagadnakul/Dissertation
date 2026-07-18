# Paper 23

## File Name

Paper_23_MIRIX_Multi_Agent_Memory_System_for_LLM_Based_Agents.md

## Category

Category 5 – Multi-Agent Memory Systems

## Paper Title

MIRIX: Multi-Agent Memory System for LLM-Based Agents

## Authors

Yu Wang, Xi Chen

## Year

2025

---

## 1. Problem Statement

Most existing memory systems for LLM agents use flat memory structures that cannot efficiently organize, retrieve, or manage different types of long-term information. They also provide poor support for multimodal memories and personalization.

---

## 2. Methodology

The authors propose **MIRIX**, a modular multi-agent memory framework.

The architecture contains six memory components:

### 1. Core Memory
Stores permanent user preferences and identity.

### 2. Episodic Memory
Stores time-based events and experiences.

### 3. Semantic Memory
Stores concepts and factual knowledge.

### 4. Procedural Memory
Stores workflows and task instructions.

### 5. Resource Memory
Stores files, documents, and multimedia resources.

### 6. Knowledge Vault
Stores sensitive information such as credentials and API keys.

Instead of using one controller, MIRIX employs multiple memory manager agents coordinated by a Meta Memory Manager.

The framework also introduces **Active Retrieval**, where the system predicts the topic first and then retrieves the most relevant memories before generating a response.

---

## 3. Dataset / Benchmark

Benchmarks:
- ScreenshotVQA
- LOCOMO

Compared Against:
- RAG
- Mem0
- MemGPT
- ChatGPT Memory
- Letta

Evaluation Metrics:
- Accuracy
- Storage Efficiency
- Retrieval Performance
- Memory Quality

---

## 4. Results

Main findings:

- 35% higher accuracy than RAG on ScreenshotVQA.
- 99.9% storage reduction.
- State-of-the-art 85.4% accuracy on LOCOMO.
- Better long-term personalization.
- Better multimodal memory retrieval.
- Efficient large-scale memory organization.

---

## 5. Strengths

- Six specialized memory types.
- Multi-agent architecture.
- Active Retrieval mechanism.
- Multimodal memory support.
- Highly scalable.
- Strong personalization.
- Efficient storage.

---

## 6. Limitations

- Focuses mainly on memory management.
- Does not include self-reflection.
- Does not target autonomous coding failure recovery.
- Requires multiple cooperating agents, increasing system complexity.

---

## 7. Relation to My Research

This paper is highly relevant because my dissertation also requires long-term memory for coding agents.

MIRIX provides an excellent architecture for organizing previous failures, debugging history, reflections, documentation, and recovery strategies.

Its multi-agent memory architecture could be integrated into a self-reflection-based failure recovery framework.

---

## 8. Key Contribution

The paper introduces MIRIX, a modular multi-agent memory system with six specialized memory types and an Active Retrieval mechanism, significantly improving long-term memory, personalization, and multimodal reasoning for LLM agents.

---

## 9. Keywords

- MIRIX
- Multi-Agent Memory
- Active Retrieval
- Episodic Memory
- Semantic Memory
- Procedural Memory
- Resource Memory
- Knowledge Vault
- Personalization
- LLM Agents

---

## My Notes

Importance for Dissertation:
⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:
- Multi-Agent Memory
- Active Retrieval
- Episodic Memory
- Semantic Memory
- Procedural Memory
- Memory Managers

Why I Selected This Paper:

Unlike traditional memory systems, MIRIX separates memory into specialized components managed by multiple agents. This design provides a scalable architecture that can be combined with self-reflection to improve failure recovery in autonomous coding agents.