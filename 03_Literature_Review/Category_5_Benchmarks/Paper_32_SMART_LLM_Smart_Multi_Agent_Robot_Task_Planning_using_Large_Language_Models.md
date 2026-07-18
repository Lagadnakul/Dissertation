# Paper 32

## File Name

Paper_32_SMART_LLM_Smart_Multi_Agent_Robot_Task_Planning_using_Large_Language_Models.md

## Category

Category 7 – Multi-Agent Planning and Autonomous Agent Systems

## Paper Title

SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models

## Authors

Shyam Sundar Kannan,
Vishnunandan L. N. Venkatesh,
Byung-Cheol Min

## Year

2024 (arXiv)

---

# 1. Problem Statement

Traditional multi-robot task planning relies on manually designed algorithms that struggle to generalize across different environments and natural language instructions. These systems often require extensive modifications whenever tasks or robot capabilities change.

The paper proposes SMART-LLM, a Large Language Model-based framework that converts high-level natural language instructions into executable multi-robot task plans by automatically decomposing tasks, forming robot coalitions, allocating tasks, and generating executable plans. :contentReference[oaicite:1]{index=1}

---

# 2. Methodology

SMART-LLM performs autonomous multi-agent planning through four sequential stages.

### Stage 1 – Task Decomposition

The LLM receives:

- High-level user instruction
- Robot skills
- Environment information
- Example prompts

It decomposes the task into multiple independent sub-tasks.

---

### Stage 2 – Coalition Formation

The LLM determines:

- Which robot possesses required skills
- Whether multiple robots should collaborate
- Team formation based on capabilities

---

### Stage 3 – Task Allocation

Each sub-task is assigned to the most appropriate robot or robot team.

The system generates executable Python code for robot execution.

---

### Stage 4 – Task Execution

Generated plans are executed using robot APIs.

The framework supports:

- Sequential execution
- Parallel execution
- Multi-agent collaboration

The prompts are written in Python rather than plain English to improve reasoning and executable code generation. :contentReference[oaicite:2]{index=2}

---

# 3. Dataset / Benchmark

The authors created a benchmark dataset using the AI2-THOR simulation environment.

Dataset includes:

- 36 natural language task instructions
- 4 task categories
- 1–4 heterogeneous robots
- Ground truth task completion states

Task Categories:

- Elemental Tasks
- Simple Tasks
- Compound Tasks
- Complex Tasks

Evaluation was performed using multiple LLMs:

- GPT-4
- GPT-3.5
- Claude 3
- Llama-2

Real-world robot experiments were also conducted. :contentReference[oaicite:3]{index=3}

---

# 4. Results

Major findings include:

- SMART-LLM successfully generates executable multi-robot task plans from natural language instructions.
- GPT-4 and Claude 3 achieved the best overall performance.
- Python-based prompts improved reasoning and planning quality.
- Multi-agent planning generalized well to unseen tasks.
- The framework handled heterogeneous robot capabilities effectively.
- Real-world robot experiments confirmed successful deployment beyond simulation.
- Coalition formation significantly improved planning accuracy compared to rule-based allocation.

:contentReference[oaicite:4]{index=4}

---

# 5. Strengths

- Fully autonomous multi-agent planning framework.
- Integrates task decomposition, coalition formation, task allocation, and execution.
- Uses Python prompts to generate executable plans.
- Supports heterogeneous robot teams.
- Evaluated in both simulation and real-world settings.
- Demonstrates strong generalization across unseen tasks.
- Includes a new benchmark dataset for evaluation.

---

# 6. Limitations

- Focuses on robot task planning rather than software engineering agents.
- Depends on LLM reasoning quality.
- Performance decreases for highly complex tasks.
- No long-term memory mechanism.
- No explicit self-reflection or iterative failure recovery.
- Limited discussion of autonomous debugging or coding tasks.

---

# 7. Relation to My Research

Although SMART-LLM targets multi-robot systems rather than software engineering, its architecture closely resembles modern agentic AI workflows. The framework demonstrates how LLMs can autonomously perform task decomposition, planning, coalition formation, and execution using structured prompts. These concepts provide valuable insights for designing agentic coding systems that coordinate multiple reasoning steps. However, unlike my dissertation, SMART-LLM does not include self-reflection, failure analysis, or iterative recovery after unsuccessful executions. My proposed framework extends these autonomous planning capabilities by enabling coding agents to analyze failures, generate reflective feedback, revise their reasoning, and recover from execution errors. :contentReference[oaicite:5]{index=5}

---

# 8. Key Contribution

SMART-LLM introduces an LLM-driven framework for autonomous multi-robot task planning that integrates task decomposition, coalition formation, task allocation, and executable code generation, demonstrating effective multi-agent coordination across simulated and real-world robotic environments. :contentReference[oaicite:6]{index=6}

---

# 9. Keywords

- SMART-LLM
- Multi-Agent Systems
- Robot Task Planning
- Large Language Models
- Task Decomposition
- Coalition Formation
- Task Allocation
- Autonomous Agents
- Multi-Robot Coordination
- AI2-THOR
- LLM Planning
- Robotics

---

# My Notes

Importance for Dissertation:

⭐⭐⭐⭐☆ (4.5/5)

Useful Ideas:

- Four-stage planning pipeline
- Task decomposition
- Coalition formation
- Task allocation
- Python-based prompting
- Multi-agent coordination
- Executable code generation
- Structured reasoning workflow
- Autonomous planning

Why I Selected This Paper:

This paper demonstrates how Large Language Models can autonomously perform planning, decomposition, coordination, and execution in multi-agent systems. Although it focuses on robotics instead of coding agents, its planning architecture closely aligns with agentic AI principles and provides useful design ideas for autonomous coding frameworks. The absence of self-reflection and failure recovery further highlights the research gap that my dissertation addresses.