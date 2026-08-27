# Paper 35

## File Name

Paper_35_A_Survey_on_Large_Language_Model_Based_Autonomous_Agents.md

## Category

Category 8 – LLM-Based Autonomous Agents (Survey)

## Paper Title

A Survey on Large Language Model Based Autonomous Agents

## Authors

Lei Wang  
Chen Ma  
Xueyang Feng  
Zeyu Zhang  
Hao Yang  
Jingsen Zhang  
Zhiyuan Chen  
Jiakai Tang  
Xu Chen  
Yankai Lin  
Wayne Xin Zhao  
Zhewei Wei  
Jirong Wen

## Year

2024

---

# 1. Problem Statement

Traditional autonomous agents rely on reinforcement learning and operate in isolated environments with limited knowledge, making it difficult to achieve human-like reasoning and decision-making.

With the emergence of Large Language Models (LLMs), researchers began building autonomous agents capable of reasoning, planning, remembering, interacting with tools, and adapting to dynamic environments. However, existing research is fragmented across different architectures and applications.

This survey systematically reviews the construction, applications, evaluation methods, challenges, and future directions of LLM-based autonomous agents by proposing a unified framework. :contentReference[oaicite:0]{index=0}

---

# 2. Methodology

The authors conducted a comprehensive literature survey of LLM-based autonomous agent research.

The survey is organized into three major aspects:

### 1. Agent Construction

A unified architecture consisting of:

- Profiling Module
- Memory Module
- Planning Module
- Action Module

### 2. Agent Applications

Applications are categorized into:

- Social Science
- Natural Science
- Engineering

### 3. Agent Evaluation

Evaluation strategies include:

- Objective Evaluation
- Subjective Evaluation

The paper also summarizes current research challenges and future directions for autonomous agents. :contentReference[oaicite:1]{index=1}

---

# 3. Dataset / Benchmark

This is a survey paper and does not introduce a new dataset.

Instead, it reviews numerous autonomous agent frameworks and benchmarks, including:

- Generative Agents
- AutoGPT
- Voyager
- ChatDev
- MetaGPT
- HuggingGPT
- Reflexion
- ReAct
- Tree of Thoughts (ToT)
- Chain of Thought (CoT)
- ToolFormer
- ToolBench
- Gorilla
- MemoryBank
- GITM
- Ghost
- DEPS
- Inner Monologue

The survey also discusses various evaluation environments such as:

- Minecraft
- Web Tasks
- Software Engineering
- Recommendation Systems
- Robotics
- Social Simulations

:contentReference[oaicite:2]{index=2}

---

# 4. Results

The survey proposes a unified architecture consisting of four core modules:

### Profiling Module

Defines the identity and role of the agent.

Examples:

- Software Engineer
- Teacher
- Doctor
- Researcher

---

### Memory Module

Stores previous experiences using:

- Short-term memory
- Long-term memory
- Hybrid memory
- Reflection memory

Memory operations include:

- Memory Reading
- Memory Writing
- Memory Reflection

---

### Planning Module

Allows agents to solve complex problems through:

- Chain of Thought (CoT)
- Tree of Thoughts (ToT)
- ReAct
- Reflexion
- Environmental Feedback
- Human Feedback
- Model Feedback

---

### Action Module

Executes decisions using:

- Internal reasoning
- External tools
- APIs
- Databases
- Knowledge Bases
- External AI models

The survey concludes that combining these four modules enables LLM agents to perform human-like autonomous reasoning and long-term task execution. :contentReference[oaicite:3]{index=3}

---

# 5. Strengths

- One of the earliest comprehensive surveys on LLM-based autonomous agents.
- Introduces a unified four-module architecture.
- Covers memory, planning, profiling, and action in detail.
- Explains memory reflection and long-term memory mechanisms.
- Discusses planning with environmental, human, and model feedback.
- Reviews numerous agent frameworks in a structured manner.
- Covers applications, evaluation, challenges, and future research directions.
- Provides clear diagrams explaining agent architecture and reasoning workflows.

---

# 6. Limitations

- Does not propose a new autonomous agent framework.
- No experimental implementation or benchmark comparison.
- Reflection and failure recovery are discussed conceptually rather than experimentally.
- Limited focus on autonomous coding agents and software engineering benchmarks such as SWE-Bench.
- Published before many recent agentic AI frameworks released in late 2024–2025.

---

# 7. Relation to My Research

This survey provides a strong theoretical foundation for my dissertation by explaining the fundamental architecture of LLM-based autonomous agents through profiling, memory, planning, and action modules. The discussion on hybrid memory, memory reflection, planning with feedback, and reasoning strategies directly supports the design principles of my proposed Self-Reflection-Based Failure Recovery Framework. However, the survey focuses primarily on general autonomous agents and does not specifically address iterative failure recovery in autonomous coding systems. My research extends these concepts by enabling coding agents to analyze failures, generate reflective feedback, revise reasoning, and recover autonomously from unsuccessful execution attempts. :contentReference[oaicite:4]{index=4}

---

# 8. Key Contribution

The paper introduces a unified four-module architecture for LLM-based autonomous agents—Profiling, Memory, Planning, and Action—and systematically reviews their construction, applications, evaluation methods, challenges, and future research directions, providing one of the earliest comprehensive foundations for modern agentic AI research. :contentReference[oaicite:5]{index=5}

---

# 9. Keywords

- Autonomous Agents
- Large Language Models
- LLM Agents
- Agent Architecture
- Memory Module
- Planning Module
- Action Module
- Profiling Module
- Memory Reflection
- Long-Term Memory
- Hybrid Memory
- Chain of Thought
- Tree of Thoughts
- ReAct
- Reflexion
- AutoGPT
- Generative Agents
- MetaGPT
- ChatDev
- HuggingGPT
- Tool Use
- AI Agents

---

# My Notes

Importance:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Unified four-module architecture
- Profiling module
- Hybrid memory
- Memory reflection
- Long-term memory
- Planning with feedback
- Environmental feedback
- Human feedback
- Model feedback
- Action module
- External tool usage
- Agent evaluation
- Agent applications
- Future research challenges

Why I Selected This Paper:

This paper is one of the foundational surveys on LLM-based autonomous agents. It introduces a unified architecture consisting of profiling, memory, planning, and action modules, which forms the conceptual basis of many modern agentic AI systems. Its detailed discussion of memory reflection, planning with feedback, and hybrid memory directly supports the architectural design of my dissertation. Although it does not implement a self-reflection-based failure recovery framework for coding agents, it provides the theoretical background and identifies research challenges that motivate my proposed framework.