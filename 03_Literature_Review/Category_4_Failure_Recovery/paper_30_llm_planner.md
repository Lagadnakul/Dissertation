# Paper 30

## File Name
paper_30_llm_planner.md

## Category
LLM-Based Planning for Embodied Agents / Agent Planning

## Paper Title
LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models

## Authors
Chan Hee Song, Jiaman Wu, Clayton Washington, Brian M. Sadler, Wei-Lun Chao, Yu Su

## Year
2023 (ICCV)

---

# 1. Problem Statement

Most embodied AI agents require thousands of labeled demonstrations to learn planning tasks. This makes training expensive and limits their ability to quickly learn new tasks.

Existing LLM-based planners also suffer from several limitations:

- Generate only static plans
- Cannot adapt when the environment changes
- Require predefined admissible actions
- Lack physical grounding to real environments

The paper aims to build a planning framework that allows an LLM to generate plans, understand the surrounding environment, and dynamically update its plan whenever execution fails. :contentReference[oaicite:0]{index=0}

---

# 2. Methodology

The authors propose **LLM-Planner**, a few-shot planning framework for embodied agents.

The framework consists of:

### Step 1 — Receive Natural Language Instruction

Example:

> "Cook a potato and put it into the recycle bin."

↓

### Step 2 — LLM Generates High-Level Plan

Instead of predicting every low-level robot action, GPT-3 generates a sequence of high-level subgoals like:

- Navigate to fridge
- Open fridge
- Pick potato
- Heat potato
- Put potato into recycle bin

↓

### Step 3 — Low-Level Planner Executes

A traditional navigation planner converts each high-level goal into robot actions.

↓

### Step 4 — Environment Observation

The robot continuously detects objects around it using an object detector.

↓

### Step 5 — Grounded Re-Planning

If execution fails or takes too long:

- Current visible objects
- Completed tasks
- Current instruction

are fed back into GPT-3.

The LLM generates a **new grounded plan** based on the updated environment.

This creates a closed-loop planning system instead of a one-time static plan. :contentReference[oaicite:1]{index=1}

---

# 3. Dataset / Benchmark

### Dataset

**ALFRED**

Contains:

- 207 environments
- 115 object categories
- 4,703 household tasks
- Long-horizon embodied navigation tasks

Example tasks:

- Heat bread
- Put apple in fridge
- Slice potato
- Clean cup

Evaluation Metrics:

- Success Rate (SR)
- Goal Condition (GC)
- High-Level Planning Accuracy (HLP Accuracy)

:contentReference[oaicite:2]{index=2}

---

# 4. Results

Major findings:

- Uses **less than 0.5%** of paired training data.
- Achieves performance competitive with fully supervised baselines.
- Outperforms existing few-shot planning approaches.
- Dynamic grounded re-planning improves task success compared to static planning.
- Requires far fewer GPT-3 calls than ranking-based methods like SayCan.
- Demonstrates strong sample efficiency for embodied planning. :contentReference[oaicite:3]{index=3}

---

# 5. Strengths

- Introduces dynamic grounded re-planning.
- Few-shot learning greatly reduces annotation cost.
- Uses GPT-3 without fine-tuning.
- Can adapt when execution fails.
- Integrates easily with existing embodied agents.
- Uses real environment observations for planning.
- Highly scalable for new tasks.
- Strong benchmark performance on ALFRED. :contentReference[oaicite:4]{index=4}

---

# 6. Limitations

- Depends on GPT-3 quality.
- Performance still depends on low-level controller.
- Object detection errors can affect planning.
- Mainly evaluated in simulated environments.
- Limited to household navigation tasks.
- Still not suitable for highly complex real-world robotics without further improvements. :contentReference[oaicite:5]{index=5}

---

# 7. Relation to My Research

This paper is **highly relevant** to my dissertation.

My dissertation focuses on:

> **Self-Reflection-Based Failure Recovery Framework for Agentic AI Coding Systems**

LLM-Planner provides several ideas directly applicable to my work:

- Dynamic re-planning after failure
- Closed-loop reasoning
- Failure-triggered plan revision
- Environment-aware planning
- LLM-guided decision making
- Sample-efficient agent learning

My work extends these concepts from embodied robotics to autonomous coding agents by incorporating self-reflection, failure analysis, memory, and iterative recovery.

---

# 8. Key Contribution

The main contribution is the introduction of **LLM-Planner**, a framework that combines:

- Few-shot prompting
- High-level task planning
- Dynamic grounded re-planning
- Environmental feedback

to enable LLMs to act as adaptive planners for embodied agents while requiring only a very small amount of training data. :contentReference[oaicite:6]{index=6}

---

# 9. Keywords

- Large Language Models
- GPT-3
- Embodied AI
- Agent Planning
- Grounded Planning
- Dynamic Re-planning
- High-Level Planning
- Few-Shot Learning
- ALFRED
- Vision-Language Navigation
- Autonomous Agents
- Robotics

---

# My Notes

Importance:
⭐⭐⭐⭐⭐

Useful Ideas:

- Failure-triggered replanning
- Closed-loop agent architecture
- Environment-aware reasoning
- High-level planning with LLMs
- Grounded execution
- Dynamic plan correction
- Few-shot prompting
- Hierarchical planning architecture

Why I Selected This Paper:

This paper is one of the closest works to my dissertation because it demonstrates how an LLM can revise its plans after encountering failures by using environmental feedback. Although the work focuses on embodied agents, its concepts of dynamic replanning, adaptive reasoning, and failure-aware decision making provide a strong foundation for designing my Self-Reflection-Based Failure Recovery Framework for Agentic AI Coding Systems.