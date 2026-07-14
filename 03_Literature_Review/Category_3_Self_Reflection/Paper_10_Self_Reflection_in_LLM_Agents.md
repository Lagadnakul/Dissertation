# Paper 10: Self-Reflection in LLM Agents: Effects on Problem-Solving Performance

## Authors
Matthew Renze, Erhan Guven

## Year
2024 (FLLM 2024)

## Category
Category 3 – Self-Reflection & Failure Recovery

---

# 1. What problem does this paper solve?

Large Language Models often make mistakes while solving problems.

Normally, after making a mistake, they simply move on without learning from it.

This paper investigates whether an LLM can improve its future performance by reflecting on its previous mistakes before attempting the task again.

---

# 2. What methodology is used?

The authors evaluated 9 popular LLMs, including:

- GPT-4
- GPT-3.5
- Claude 3 Opus
- Gemini 1.5 Pro
- Llama 2
- Mistral Large

They created a benchmark containing 1,000 multiple-choice questions from different domains.

The experiment followed these steps:

1. Model answers the question.
2. Incorrect answers are identified.
3. The model performs self-reflection on its mistake.
4. Different types of reflection are generated:
   - Retry
   - Keywords
   - Advice
   - Explanation
   - Instructions
   - Solution
   - Composite Reflection
5. The model answers the same question again using its reflection.
6. Performance before and after reflection is compared.

---

# 3. What results are achieved?

Major Findings:

- Self-reflection significantly improved performance across all tested LLMs.
- Statistical significance: p < 0.001.
- Detailed reflections (Explanation, Instructions, Solution) produced larger improvements than simple retry prompts.
- Even telling the model that it previously made a mistake improved accuracy.
- GPT-4 accuracy increased substantially after reflection.
- Composite reflection produced one of the highest overall improvements.

---

# 4. What are the limitations?

- The experiment only evaluated single-step question-answering tasks.
- It did not evaluate long-horizon software engineering tasks.
- No real coding repositories were used.
- Reflection occurred only once instead of multiple recovery cycles.
- External memory was not included.
- The framework was not tested on autonomous coding agents.

---

# 5. How is my research different?

This paper proves that self-reflection improves LLM reasoning performance.

However, it does not focus on autonomous coding agents.

My research extends this idea by developing a failure recovery framework specifically for Agentic AI Coding Systems.

Instead of solving only MCQ problems, my framework will help coding agents:

- detect failures,
- analyze why the failure occurred,
- generate self-reflection,
- repair the failed attempt,
- retry automatically,
- continue working until the task is completed successfully.

The proposed framework focuses on real software engineering workflows rather than single-step reasoning tasks.

---

# Key Contribution

This paper provides strong experimental evidence that self-reflection improves LLM performance.

It serves as one of the strongest theoretical foundations for incorporating self-reflection into autonomous failure recovery systems.

---

# Why this paper is important for my dissertation

✅ Supports self-reflection.

✅ Provides experimental evidence.

✅ Validates iterative improvement.

✅ Strengthens the motivation behind my proposed Failure Recovery Framework.

✅ One of the core papers for my Literature Review.

---

# Citation

Renze, M., & Guven, E. (2024).
Self-Reflection in LLM Agents: Effects on Problem-Solving Performance.
Proceedings of the 2nd International Conference on Foundation and Large Language Models (FLLM 2024).