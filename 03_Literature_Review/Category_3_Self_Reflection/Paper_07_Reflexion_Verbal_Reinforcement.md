# Paper 07

## Title
Reflexion: Language Agents with Verbal Reinforcement Learning

## Authors
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, Shunyu Yao

## Year
2023

## Conference
NeurIPS 2023

---

# 1. What problem does this paper solve?

Traditional LLM agents usually repeat the same mistakes because they do not learn from previous failures during inference.

Existing reinforcement learning methods require expensive model training and fine-tuning, making them difficult to apply for autonomous AI agents.

The paper proposes a self-reflection mechanism that allows AI agents to improve after every failed attempt without changing the model weights.

---

# 2. What methodology is used?

The paper introduces a framework called **Reflexion**.

The framework consists of three main components:

• Actor (LLM) → Performs the task.

• Evaluator → Checks whether the task succeeded or failed.

• Self-Reflection Module → Analyzes the failure and generates natural language feedback.

The generated reflection is stored in an **episodic memory**.

During the next attempt, the agent reads its previous reflections before solving the task again.

The improvement loop is:

Task
↓

Failure

↓

Evaluation

↓

Self-Reflection

↓

Memory Update

↓

Retry

↓

Better Result

No model retraining or fine-tuning is required.

---

# 3. What results are achieved?

Reflexion significantly improves AI agent performance across multiple domains.

Major experimental results include:

• HumanEval Coding Benchmark:
91% Pass@1 accuracy
(previous GPT-4 achieved around 80%)

• ALFWorld:
22% improvement

• HotPotQA:
20% improvement

The study demonstrates that self-reflection enables agents to learn from mistakes much more effectively than repeated prompting alone.

---

# 4. What are the limitations?

• Depends on the quality of self-generated reflections.

• Cannot guarantee optimal recovery in every failure.

• Limited memory window because of LLM context length.

• Less effective in highly exploratory environments requiring completely new strategies.

• Performance depends on the strength of the underlying LLM.

---

# 5. How is my research different?

This paper focuses on improving agent performance using self-reflection and memory.

My dissertation extends this concept by proposing a complete **Failure Recovery Framework** specifically designed for **Agentic AI Coding Systems**.

Instead of only generating reflections, my framework will:

• Detect failures automatically

• Classify failure types

• Trigger self-reflection

• Apply iterative repair

• Re-execute the task

• Measure recovery success rate, recovery time, token cost, and number of repair iterations

The goal is not only better reasoning but reliable automatic recovery from coding failures.

---

# Key Takeaway

Reflexion proves that AI agents can learn from failures using natural language self-reflection instead of expensive reinforcement learning.

This paper provides the fundamental idea that my dissertation builds upon by extending self-reflection into a complete autonomous failure recovery framework.