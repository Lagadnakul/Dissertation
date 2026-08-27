# Paper 08

## Title

SELF-REFINE: Iterative Refinement with Self-Feedback

---

## Authors

Aman Madaan,
Niket Tandon,
Prakhar Gupta,
Skyler Hallinan,
Luyu Gao,
Sarah Wiegreffe,
Uri Alon,
Nouha Dziri,
Shrimai Prabhumoye,
Yiming Yang,
Shashank Gupta,
Bodhisattwa Majumder,
Katherine Hermann,
Sean Welleck,
Amir Yazdanbakhsh,
Peter Clark

---

## Year

2023

---

## Conference

NeurIPS 2023

---

# 1. What problem does this paper solve?

Large Language Models usually generate only one answer.

Even if the answer contains mistakes, there is no mechanism to review and improve it automatically.

Most previous approaches require:

• Human feedback

• Reinforcement Learning

• Fine-tuning

• Additional training data

All of these methods are expensive.

This paper proposes a simple method where the same LLM reviews its own answer, provides feedback, and improves it repeatedly without any additional training.

---

# 2. What methodology is used?

The paper introduces a framework called **SELF-REFINE**.

The framework has three major steps.

Step 1:
Generate an initial answer.

↓

Step 2:
Generate feedback about that answer.

↓

Step 3:
Rewrite the answer using the generated feedback.

↓

Repeat until the stopping condition is reached.

The complete workflow is:

Input

↓

Initial Generation

↓

Self Feedback

↓

Refined Output

↓

Repeat

↓

Final Answer

The same LLM performs all three roles:

• Generator

• Reviewer

• Refiner

No external evaluator or model training is required.

---

# 3. What results are achieved?

SELF-REFINE was evaluated on seven different tasks.

These include:

• Dialogue Generation

• Code Optimization

• Code Readability

• Mathematical Reasoning

• Sentiment Reversal

• Acronym Generation

• Constrained Text Generation

Major findings include:

• Around **20% average improvement** over one-shot generation.

• Dialogue generation improved by up to **49%**.

• Code Optimization improved from **27.3% to 36.0%** using GPT-4.

• Performance improved consistently across GPT-3.5, ChatGPT, GPT-4, and CodeX.

The study demonstrates that iterative refinement produces better outputs than generating only one response.

---

# 4. What are the limitations?

• Strong LLMs are required for effective self-feedback.

• Weak models often generate poor or incorrect feedback.

• Performance depends heavily on feedback quality.

• Mathematical reasoning showed only limited improvement because LLMs often failed to detect their own reasoning mistakes.

• Multiple refinement iterations increase inference time and token cost.

• Limited by context window size.

---

# 5. How is my research different?

SELF-REFINE focuses on improving the quality of generated outputs through repeated self-feedback.

My dissertation focuses on something different.

Instead of improving output quality only, my framework is designed specifically for **Agentic AI Coding Systems** recovering from execution failures.

My proposed framework includes:

• Automatic failure detection

• Failure type classification

• Self-reflection

• Root cause analysis

• Iterative repair

• Command re-execution

• Recovery evaluation

Unlike SELF-REFINE, my research evaluates:

• Recovery Success Rate

• Recovery Time

• Token Cost

• Number of Repair Attempts

• Recovery Efficiency

The objective is reliable autonomous recovery rather than simply improving generated text.

---

# Key Takeaway

SELF-REFINE proves that a single Large Language Model can improve its own outputs by repeatedly generating feedback and refining its previous response without additional training.

This paper provides the iterative refinement mechanism that can be integrated into my proposed Self-Reflection-Based Failure Recovery Framework for Agentic AI Coding Systems.