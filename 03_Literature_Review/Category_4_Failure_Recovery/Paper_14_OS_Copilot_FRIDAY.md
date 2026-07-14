# Paper 14

## Title

OS-Copilot: Towards Generalist Computer Agents with Self-Improvement

**Authors:** Zhiyong Wu et al.

**Year:** 2024 (ICLR 2024)

**Category:** Agentic AI / Self-Improving Computer Agents

---

## 1. Problem Statement

Most existing AI agents are designed to operate within a single environment, such as web browsers, command-line interfaces, or specific applications. These agents struggle to perform complex operating system-level tasks and cannot effectively learn new skills or recover from failures when interacting with unfamiliar software.

---

## 2. Methodology

The authors propose **OS-Copilot**, a framework for building general-purpose operating system agents.

Using this framework, they develop **FRIDAY (Fully Responsive Intelligence Devoted to Assisting You)**, a self-improving AI assistant capable of performing diverse computer tasks.

The architecture consists of five major components:

- Planner
- Configurator (Working Memory + Declarative Memory + Procedural Memory)
- Actor (Executor)
- Critic
- Refiner

The workflow is:

User Task
↓

Planner decomposes task into subtasks

↓

Configurator retrieves tools, memory, and knowledge

↓

Executor performs actions

↓

Critic evaluates execution

↓

Refiner corrects mistakes

↓

Updated tools and memory are stored for future tasks

The framework also introduces **self-directed learning**, enabling FRIDAY to autonomously learn how to use previously unseen applications such as Excel and PowerPoint.

---

## 3. Results

• FRIDAY achieved **40.86% success** on GAIA Level-1 tasks, outperforming previous state-of-the-art methods by approximately **35%**.

• Successfully solved **20.13%** of GAIA Level-2 tasks.

• Achieved **6.12%** success on difficult Level-3 tasks where previous systems achieved **0%**.

• After self-directed learning, FRIDAY improved spreadsheet task performance from **0% to 60%**, surpassing SheetCopilot.

• Demonstrated strong generalization across multiple operating system applications.

---

## 4. Limitations

• Currently supports Linux and macOS only.

• Relies heavily on prompt engineering instead of model fine-tuning.

• Limited support for closed-source graphical applications.

• Multimodal interaction capabilities remain limited.

• Evaluation of OS-level task completion is challenging because no clear ground truth exists.

---

## 5. Difference from My Research

OS-Copilot develops a general-purpose operating system assistant capable of planning, executing, self-correcting, and learning new computer skills across many applications.

My dissertation focuses specifically on **failure recovery in Agentic AI Coding Systems**. Instead of creating a universal OS assistant, I propose a self-reflection framework that analyzes execution failures, generates reflective feedback, revises reasoning, and improves recovery during software engineering tasks such as repository navigation, debugging, code generation, and tool execution.

---

## Key Contribution

Introduces one of the first complete architectures for self-improving operating system agents by integrating planning, memory, execution, self-criticism, self-refinement, and self-directed learning into a unified framework.

---

## Important Keywords

- OS-Copilot
- FRIDAY
- Generalist AI Agent
- Operating System Agent
- Planner
- Working Memory
- Declarative Memory
- Procedural Memory
- Critic
- Refiner
- Self-Correction
- Self-Reflection
- Self-Directed Learning
- Failure Recovery
- Agentic AI
- Tool Learning
- GAIA Benchmark