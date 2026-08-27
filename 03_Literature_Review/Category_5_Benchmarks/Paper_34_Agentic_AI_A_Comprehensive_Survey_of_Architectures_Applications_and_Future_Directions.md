# Paper 34

## File Name

Paper_34_Agentic_AI_A_Comprehensive_Survey_of_Architectures_Applications_and_Future_Directions.md

## Category

Category 8 – Agentic AI Surveys and Comprehensive Reviews

## Paper Title

Agentic AI: A Comprehensive Survey of Architectures, Applications, and Future Directions

## Authors

Mohamad Abou Ali  
Fadi Dornaika  
Jinan Charafeddine

## Year

2026 (Accepted: 2025)

---

# 1. Problem Statement

Agentic AI has rapidly evolved with the emergence of Large Language Models (LLMs), autonomous agents, and multi-agent systems. However, the literature often mixes classical symbolic AI with modern LLM-based agentic systems, creating conceptual confusion known as **conceptual retrofitting**.

This survey addresses that problem by introducing a **dual-paradigm taxonomy** that clearly distinguishes **Symbolic/Classical Agentic AI** from **Neural/Generative Agentic AI**, while reviewing architectures, applications, governance, challenges, and future directions. :contentReference[oaicite:0]{index=0}

---

# 2. Methodology

The authors performed a **systematic PRISMA-based literature review**.

### Literature Search

Databases used:

- IEEE Xplore
- ACM Digital Library
- SpringerLink
- ScienceDirect
- arXiv
- Google Scholar

Search keywords included:

- Agentic AI
- Autonomous Agents
- LLM Agents
- Multi-Agent Systems
- LangChain
- AutoGen
- Prompt Chaining
- Cognitive Architectures
- BDI
- POMDP
- Symbolic Planning

The review finally analyzed:

- **90 research studies**
- Covering publications from **2018–2025**

using PRISMA screening, thematic synthesis, and paradigm classification. :contentReference[oaicite:1]{index=1}

---

# 3. Dataset / Benchmark

This paper is a systematic survey rather than an experimental study.

Instead of datasets, it analyzes:

- 90 research papers
- Symbolic AI literature
- Neural/Generative Agentic AI literature
- Multi-Agent Systems
- LLM-based frameworks

Major frameworks reviewed include:

- LangChain
- AutoGen
- CrewAI
- Semantic Kernel
- LlamaIndex

It also discusses:

- MDP
- POMDP
- BDI
- SOAR
- Deep Reinforcement Learning
- Multi-Agent Orchestration
- Neuro-Symbolic AI

:contentReference[oaicite:2]{index=2}

---

# 4. Results

Major findings include:

- Agentic AI consists of two fundamentally different paradigms:
  - Symbolic/Classical
  - Neural/Generative
- Modern LLM agents achieve autonomy through **prompt-driven orchestration**, not traditional symbolic planning.
- Multi-agent orchestration represents the current state-of-the-art for Agentic AI.
- Healthcare and legal systems favor symbolic or constrained architectures, whereas finance and adaptive applications increasingly rely on neural agentic systems.
- Ethical challenges differ across paradigms and require different governance strategies.
- The future lies in **hybrid neuro-symbolic architectures** that combine the reliability of symbolic reasoning with the adaptability of neural systems.

:contentReference[oaicite:3]{index=3}

---

# 5. Strengths

- Very comprehensive and recent survey.
- Reviews 90 studies using PRISMA methodology.
- Introduces a novel dual-paradigm taxonomy.
- Clearly differentiates symbolic AI from LLM-based Agentic AI.
- Explains evolution from Symbolic AI → Machine Learning → Deep Learning → Generative AI → Agentic AI.
- Covers architectures, orchestration frameworks, governance, applications, ethics, and future research.
- Includes high-quality diagrams explaining paradigm evolution and multi-agent workflows.

---

# 6. Limitations

- Does not propose a new Agentic AI framework.
- No experimental implementation.
- Limited discussion of coding-agent benchmarks such as SWE-Bench.
- Does not evaluate autonomous coding systems experimentally.
- Reflection and failure recovery are discussed conceptually rather than implemented.
- Hybrid neuro-symbolic architectures remain future work.

---

# 7. Relation to My Research

This paper provides an excellent theoretical foundation for my dissertation by clearly distinguishing symbolic and neural paradigms of Agentic AI and explaining how modern LLM-based agents achieve autonomy through planning, memory, prompt orchestration, tool use, and multi-agent collaboration. The proposed dual-paradigm taxonomy helps justify the architectural choices behind autonomous coding agents. However, the survey does not design or experimentally evaluate a self-reflection-based failure recovery framework for coding systems. My research extends this direction by proposing a framework that enables coding agents to detect execution failures, analyze errors, generate reflective feedback, revise reasoning, and iteratively recover from unsuccessful execution attempts. :contentReference[oaicite:4]{index=4}

---

# 8. Key Contribution

The paper introduces a **novel dual-paradigm taxonomy** that separates Symbolic/Classical Agentic AI from Neural/Generative Agentic AI, providing a unified framework for understanding architectures, applications, governance, and future research while reviewing 90 studies using a rigorous PRISMA methodology. :contentReference[oaicite:5]{index=5}

---

# 9. Keywords

- Agentic AI
- Autonomous Agents
- Artificial Intelligence
- Large Language Models
- Multi-Agent Systems
- LangChain
- AutoGen
- CrewAI
- LlamaIndex
- Symbolic AI
- Neural AI
- Neuro-Symbolic AI
- Prompt Chaining
- AI Governance
- Multi-Agent Orchestration
- Deep Reinforcement Learning
- BDI
- POMDP

---

# My Notes

Importance:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Dual-paradigm taxonomy
- Symbolic vs Neural Agentic AI
- PRISMA systematic review
- Evolution timeline of AI
- Multi-agent orchestration
- Prompt-driven orchestration
- LangChain
- AutoGen
- CrewAI
- Semantic Kernel
- LlamaIndex
- Governance models
- Neuro-symbolic future
- AI ethics
- Architecture comparison

Why I Selected This Paper:

This is one of the newest and most comprehensive surveys on Agentic AI. It systematically reviews 90 studies and introduces a novel dual-paradigm taxonomy that clearly differentiates symbolic and neural Agentic AI systems. The discussion on LLM orchestration, multi-agent workflows, governance, and future hybrid architectures strongly supports the theoretical background of my dissertation. Although it does not implement a self-reflection-based failure recovery mechanism, it identifies important research gaps that directly motivate my proposed framework for improving autonomous coding agents.