# Paper 06

## Title

OpenHands: An Open Platform for AI Software Developers as Generalist Agents

## Authors

Xingyao Wang et al.

---

## Conference

ICLR 2025

---

# Research Category

Category 2

Agentic AI Coding Systems

---

# 1. What problem does this paper solve?

Most existing AI agent frameworks are designed for specific tasks and provide limited support for real-world software engineering.

They often lack:

- A realistic software development environment
- Safe code execution
- Web browsing capability
- Multi-agent collaboration
- Standardized evaluation
- Extensible tools for developers

OpenHands solves this problem by providing a complete open-source platform where AI agents can work like human software developers.

The platform allows agents to:

- Write code
- Execute terminal commands
- Browse the web
- Debug programs
- Collaborate with other agents
- Solve real software engineering tasks

---

# 2. What methodology is used?

The authors introduce **OpenHands**, an open-source framework for developing and evaluating AI software engineering agents.

The framework consists of five major components:

### 1. Agent Abstraction

Defines how an AI agent observes its environment and generates actions.

### 2. Event Stream

Stores the complete history of:

- User instructions
- Agent actions
- Execution results
- Previous observations

This allows the agent to reason over its entire execution history.

### 3. Runtime Environment

Provides a secure Docker sandbox containing:

- Bash terminal
- Python (IPython)
- Chromium web browser

Agents execute commands safely inside this environment.

### 4. Agent Skills Library

Provides reusable tools such as:

- File editing
- PDF reading
- Image parsing
- Code editing
- Navigation utilities

These skills extend the capabilities of AI agents.

### 5. Multi-Agent Delegation

Allows specialized agents to cooperate.

For example:

- CodeAct Agent handles coding tasks.
- Browsing Agent handles web browsing.
- Other specialized agents solve subtasks.

The framework also includes an evaluation system supporting **15 benchmarks**, including SWE-Bench, WebArena, HumanEvalFix, ToolQA, GAIA, and AgentBench.

---

# 3. What results are achieved?

Major findings include:

• Successfully created a complete open-source platform for AI software engineering agents.

• Supports more than **10 different agent implementations**.

• Evaluated agents on **15 public benchmarks**.

• CodeActAgent achieved:

- **26% success rate on SWE-Bench Lite**
- **79.3% on HumanEvalFix**
- **76.5% on ML-Bench**
- Competitive performance on WebArena and AgentBench.

• OpenHands has:

- **32K+ GitHub stars**
- **2.1K+ contributions**
- **188+ contributors**

demonstrating strong community adoption.

---

# 4. What are the limitations?

- Current benchmark performance is still below expert human developers.

- Performance depends heavily on the underlying LLM.

- Complex software engineering tasks remain difficult.

- Long reasoning chains increase computational cost.

- Failure recovery mainly relies on repeated execution and agent reasoning.

- No dedicated self-reflection or structured failure recovery framework is proposed.

---

# 5. How is my research different?

OpenHands provides an excellent platform for building AI coding agents, but its primary goal is to execute software engineering tasks.

My dissertation focuses specifically on improving **failure recovery** in agentic AI coding systems.

Instead of only providing an execution platform, my framework introduces:

- Self-reflection after failures
- Failure classification
- Root cause analysis
- Recovery strategy generation
- Iterative repair planning
- Memory of previous failures

to increase recovery success, reduce repeated failures, lower execution cost, and improve overall task completion.

---

# Key Contribution

Introduced one of the first comprehensive open-source platforms for building, running, evaluating, and extending AI software engineering agents with secure execution, browser interaction, multi-agent collaboration, and standardized benchmarking.

---

# Important Notes for Dissertation

Useful for:

✔ Literature Review

✔ Agentic AI Coding Systems

✔ AI Software Engineering Platforms

✔ Multi-Agent Collaboration

✔ Event Stream Architecture

✔ Tool Use in AI Agents

✔ Benchmark Evaluation

✔ Failure Recovery Motivation

✔ Related Work