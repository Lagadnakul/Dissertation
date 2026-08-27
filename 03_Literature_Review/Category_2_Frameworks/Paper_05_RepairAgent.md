# Paper 05

## Title

RepairAgent: An Autonomous, LLM-Based Agent for Program Repair

## Authors

Islem Bouzenia

Premkumar Devanbu

Michael Pradel

---

## Conference

arXiv 2024

---

# Research Category

Category 2

AI Coding Agents & Failure Recovery

---

# 1. What problem does this paper solve?

Existing LLM-based program repair methods use fixed prompts or predefined feedback loops.

These approaches cannot:

- Autonomously explore repositories
- Gather additional debugging information
- Search for repair ingredients
- Adapt their repair strategy after failures

RepairAgent solves this problem by introducing an autonomous AI agent that can independently plan, investigate, repair, validate, and retry until the bug is fixed.

---

# 2. What methodology is used?

The authors propose RepairAgent, an autonomous LLM-based software repair framework.

The system consists of three major components:

### 1. LLM Agent

Uses GPT-3.5 as the reasoning engine.

### 2. Agent Tools

The agent can use 14 software engineering tools such as:

- Read code
- Search codebase
- Extract methods
- Find similar API calls
- Run tests
- Fault localization
- Generate method body
- Apply patches

### 3. Middleware

Controls communication between the LLM and tools.

The agent follows a finite-state workflow:

- Understand Bug
- Collect Information
- Try Repair
- Validate
- Repeat if necessary

The framework dynamically updates the prompt after every action based on newly gathered information and previous repair attempts.

---

# 3. What results are achieved?

Major findings include:

• Successfully repaired **164 real-world bugs** on the Defects4J benchmark.

• Fixed **39 bugs** that previous state-of-the-art methods could not repair.

• Achieved:

- 115 single-line bug fixes
- 46 multi-line bug fixes
- 3 multi-file bug fixes

• Average repair cost:

- 270K tokens
- Approximately **$0.14 per bug**

• Demonstrated better performance than ChatRepair, ITER, and SelfAPR on several benchmarks.

---

# 4. What are the limitations?

- Overall repair success rate is still limited for highly complex bugs.

- Multi-file and large-scale software bugs remain difficult.

- Performance depends heavily on fault localization accuracy.

- Uses GPT-3.5, so results may improve with stronger LLMs.

- Long repair cycles increase token cost.

- Sometimes proposes overly complex fixes for simple bugs.

---

# 5. How is my research different?

RepairAgent focuses on autonomous program repair using tools and dynamic planning.

However, its goal is to repair software bugs.

My dissertation focuses specifically on improving **failure recovery in agentic coding systems** after intermediate failures.

Instead of only repairing bugs, my framework will introduce:

- Self-reflection
- Failure classification
- Root cause analysis
- Recovery strategy generation
- Iterative repair planning
- Memory of previous failures

to improve recovery success, reduce repeated mistakes, and increase task completion in agentic AI coding systems.

---

# Key Contribution

Introduced the **first autonomous LLM-based program repair agent** that combines dynamic prompting, software engineering tools, and iterative planning to autonomously debug and repair software.

---

# Important Notes for Dissertation

Useful for:

✔ Literature Review

✔ Related Work

✔ Agentic AI Coding Systems

✔ Autonomous Software Repair

✔ Dynamic Prompting

✔ Tool Use by AI Agents

✔ Failure Recovery Discussion

✔ Self-Reflection Motivation

✔ Agent Workflow Design