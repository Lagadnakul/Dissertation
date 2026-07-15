# Paper 17 – AgentBench: Evaluating LLMs as Agents

**Title:**
AgentBench: Evaluating LLMs as Agents

**Authors:**
Xiao Liu et al.

**Conference:**
ICLR 2024

---

# 1. Problem Statement

Existing benchmarks mainly evaluate Large Language Models on static NLP tasks. However, they do not measure how well LLMs behave as autonomous agents that must reason, make decisions, interact with environments, and complete multi-step tasks.

---

# 2. Methodology

The authors propose AgentBench, a benchmark for evaluating LLM-based agents across eight interactive environments.

The benchmark evaluates:

- Operating System
- Database
- Knowledge Graph
- Digital Card Game
- Lateral Thinking Puzzle
- House Holding
- Web Shopping
- Web Browsing

A total of 29 LLMs are evaluated, including GPT-4, Claude, Llama, Vicuna, CodeLlama, and other open-source models.

The benchmark measures:

- Multi-step reasoning
- Decision making
- Tool usage
- Instruction following
- Planning ability
- Task completion

:contentReference[oaicite:0]{index=0}

---

# 3. Results

Major findings include:

- GPT-4 achieved the highest overall performance.
- Open-source models still lag behind commercial models.
- Most failures were caused by:
  - Poor long-term reasoning
  - Weak decision making
  - Weak instruction following
- Better alignment training significantly improves agent performance.

:contentReference[oaicite:1]{index=1}

---

# 4. Limitations

- It is only an evaluation benchmark.
- It does not propose a new failure recovery mechanism.
- It evaluates existing LLM agents rather than improving them.
- Reflection and recovery are not the primary focus.

---

# 5. How My Research is Different

This paper evaluates whether an AI agent succeeds or fails.

My research focuses on what happens **after the failure**.

Instead of only measuring performance, I propose a Self-Reflection-Based Failure Recovery Framework that enables the agent to:

- Analyze its own failure
- Reflect on the mistake
- Generate improved reasoning
- Repair its previous solution
- Retry automatically until successful

Therefore, my work extends beyond benchmarking by introducing an autonomous recovery framework for coding agents.

---

# Why This Paper is Useful

This paper provides:

- Standard benchmark for agent evaluation
- Failure analysis of LLM agents
- Common reasons for agent failures
- Motivation for building better recovery systems

It strongly supports the motivation of my dissertation because it demonstrates that current AI agents frequently fail in long-term reasoning and decision making, highlighting the need for automatic failure recovery.
