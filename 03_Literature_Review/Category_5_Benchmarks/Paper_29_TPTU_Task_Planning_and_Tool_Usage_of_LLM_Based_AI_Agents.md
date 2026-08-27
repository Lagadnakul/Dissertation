Paper_29_TPTU_Task_Planning_and_Tool_Usage_of_LLM_Based_AI_Agents.md# Paper 29

## File Name

Paper_29_TPTU_Task_Planning_and_Tool_Usage_of_LLM_Based_AI_Agents.md

## Category

Category 7 – Task Planning and Tool Usage in LLM Agents

## Paper Title

TPTU: Task Planning and Tool Usage of Large Language Model-based AI Agents

## Authors

Jingqing Ruan,
Yihong Chen,
Bin Zhang,
Zhiwei Xu,
Tianpeng Bao,
Guoqing Du,
Shiwei Shi,
Hangyu Mao,
Ziyue Li,
Xingyu Zeng,
Rui Zhao

SenseTime Research

## Year

2023 (NeurIPS 2023 Foundation Models for Decision Making Workshop)

---

## 1. Problem Statement

Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language understanding and generation. However, solving complex real-world tasks requires more than language generation. AI agents must be able to decompose complex problems into multiple subtasks, select appropriate external tools, execute them in the correct order, and summarize the final results.

Existing research primarily focuses on either task planning or tool usage separately, with limited work evaluating both capabilities together. This paper addresses this gap by proposing a unified framework for evaluating Task Planning and Tool Usage (TPTU) abilities in LLM-based AI agents. 

---

## 2. Methodology

The authors propose a structured framework called **TPTU (Task Planning and Tool Usage)** for evaluating LLM-based AI agents.

The framework identifies five essential capabilities of AI agents:

### 1. Perception

The agent receives and understands user input from different sources.

### 2. Task Planning

The agent decomposes a complex problem into multiple sequential subtasks.

### 3. Tool Usage

The agent selects and invokes appropriate external tools (e.g., SQL generators, Python generators, search engines) to solve each subtask.

### 4. Learning, Reflection, and Memory

The agent learns from previous interactions, stores useful information, reflects on failures, and improves future decision-making.

### 5. Summarization

After completing all subtasks, the agent summarizes the final solution in a clear and user-friendly manner. :contentReference[oaicite:1]{index=1}

### Proposed Agent Architectures

The paper introduces two different AI agent designs:

#### TPTU-OA (One-Step Agent)

- Plans all subtasks at once.
- Generates a complete execution plan before solving the task.
- Suitable for problems requiring global planning.

#### TPTU-SA (Sequential Agent)

- Solves one subtask at a time.
- Continuously generates the next subtask based on previous execution.
- More flexible and adaptive for dynamic environments. :contentReference[oaicite:2]{index=2}

---

## 3. Dataset / Benchmark

The evaluation framework uses realistic multi-tool reasoning tasks.

Tools used include:

- SQL Generator
- Python Generator
- Additional unrelated tools (to test tool selection)

Dataset:

- 120 manually created question-answer pairs
- Different levels of complexity
- Multi-step reasoning tasks

Evaluated Models:

- ChatGPT
- Claude
- ChatGLM-130B
- InternLM
- Ziya-13B
- Chinese-Alpaca-33B

Evaluation focuses on:

- Task planning accuracy
- Tool selection
- Tool invocation
- Sequential reasoning
- Subtask generation
- Final answer quality :contentReference[oaicite:3]{index=3}

---

## 4. Results

Major findings:

- Commercial LLMs such as ChatGPT and Claude outperform most open-source models.
- Sequential planning often provides better flexibility for complex reasoning tasks.
- LLMs occasionally fail to generate outputs in the required format.
- Agents sometimes overuse a single tool instead of selecting the most appropriate one.
- Many agents struggle to fully understand complex task requirements.
- Summarization remains a weak capability for several evaluated models. :contentReference[oaicite:4]{index=4}

---

## 5. Strengths

- Introduces a unified framework combining task planning and tool usage.
- Defines the core capabilities required for LLM-based AI agents.
- Proposes two complementary planning strategies.
- Evaluates multiple state-of-the-art LLMs.
- Uses realistic multi-tool reasoning scenarios.
- Provides valuable insights into current strengths and weaknesses of AI agents.

---

## 6. Limitations

- Limited number of evaluation tasks.
- Focuses primarily on planning and tool usage rather than autonomous software engineering.
- Does not evaluate long-term memory or advanced self-reflection in depth.
- Does not propose a new learning algorithm.
- Mainly serves as an evaluation framework rather than a complete agent architecture.

---

## 7. Relation to My Research

This paper is highly relevant to my dissertation because task planning and tool usage are fundamental components of autonomous AI coding systems.

My dissertation focuses on developing a **Self-Reflection-Based Failure Recovery Framework for Agentic AI Coding Systems**.

Before an AI coding agent can recover from failures, it must first correctly decompose tasks, select suitable tools, execute them effectively, and learn from execution feedback. The TPTU framework provides a strong conceptual foundation for understanding these capabilities and highlights the importance of integrating planning, tool usage, memory, and reflection into reliable AI agents.

---

## 8. Key Contribution

The paper introduces the **TPTU framework**, a unified evaluation framework for assessing task planning and tool usage abilities of LLM-based AI agents. It also proposes two agent architectures—One-Step Agent (TPTU-OA) and Sequential Agent (TPTU-SA)—to study different planning strategies for complex multi-step tasks. 

---

## 9. Keywords

- Task Planning
- Tool Usage
- LLM Agents
- AI Agents
- Sequential Planning
- One-Step Planning
- Tool Selection
- External Tools
- Reflection
- Memory
- Large Language Models
- Autonomous Agents

---

## My Notes

Importance for Dissertation:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Task decomposition
- Tool selection
- Sequential reasoning
- One-step planning
- Reflection and memory
- Multi-tool execution
- Agent architecture
- AI workflow

Why I Selected This Paper:

This paper provides one of the earliest structured frameworks for understanding how LLM-based AI agents should plan tasks and use external tools. The proposed TPTU framework identifies task planning, tool usage, memory, reflection, and summarization as the core capabilities of intelligent agents. These concepts closely align with my dissertation, where effective planning, tool execution, and self-reflection are essential for building reliable failure recovery mechanisms in autonomous AI coding systems.