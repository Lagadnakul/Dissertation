# Paper 16

## Title

SWE-Bench: Can Language Models Resolve Real-World GitHub Issues?

## Authors

Carlos E. Jimenez
John Yang
Alexander Wettig
Shunyu Yao
Kexin Pei
Ofir Press
Karthik Narasimhan

## Conference

ICLR 2024

---

# 1. Problem

Existing coding benchmarks like HumanEval are too simple and cannot evaluate real-world software engineering abilities.

Real software development requires:

- Understanding large repositories
- Reading GitHub issues
- Editing multiple files
- Running tests
- Fixing real software bugs

There was no benchmark to evaluate these abilities.

---

# 2. Proposed Solution

The authors introduce SWE-bench, a benchmark for evaluating AI coding agents using real GitHub issues.

Instead of solving small coding questions, models receive:

- Real GitHub Issue
- Complete Repository
- Existing Codebase

The model must generate a patch that fixes the issue.

The generated patch is validated using the repository's real unit tests.

---

# 3. Dataset

SWE-bench contains

- 2,294 real GitHub issues
- 12 popular Python repositories
- Real pull requests
- Real bug fixes
- Real software tests

Examples include:

- Django
- Scikit-Learn
- SymPy
- Matplotlib
- Flask
- Requests
- PyTest
- Sphinx

---

# 4. Workflow

GitHub Issue

↓

Repository Snapshot

↓

LLM

↓

Generate Patch

↓

Apply Patch

↓

Run Unit Tests

↓

Issue Fixed or Failed

---

# 5. Evaluation Metric

Main Metric:

Resolution Rate

A task is considered solved only if:

✔ Patch applies successfully

AND

✔ All related tests pass

This makes evaluation reliable and objective.

---

# 6. Key Results

Best model at the time:

Claude 2

Resolved only

1.96%

of 2,294 issues.

This demonstrates that repository-level software engineering is still very challenging for LLMs.

---

# 7. Main Contributions

• Introduced SWE-bench benchmark

• 2,294 real GitHub issues

• Repository-level software engineering tasks

• Automatic execution-based evaluation

• Real unit testing

• Release of SWE-Llama fine-tuned models

---

# 8. Advantages

✔ Real-world benchmark

✔ Large repositories

✔ Multiple file editing

✔ Long-context reasoning

✔ Objective evaluation

✔ Continuously expandable

---

# 9. Limitations

- Only Python repositories
- Requires large context windows
- Difficult retrieval of relevant files
- Current LLMs achieve very low success rates
- Focuses mainly on bug fixing

---

# 10. Relation to My Dissertation

This paper is highly relevant because my proposed Self-Reflection-Based Failure Recovery Framework will be evaluated on repository-level coding tasks.

SWE-bench can serve as the primary benchmark for evaluating:

- Recovery Success Rate
- Task Completion Rate
- Number of Recovery Attempts
- Reflection Quality
- Token Cost
- Execution Time

---

# 11. Research Gap

SWE-bench provides a benchmark but does not improve how coding agents recover after failure.

It evaluates coding agents but lacks a self-reflection-based failure recovery mechanism.

This creates an opportunity to design a framework where agents analyze failures, generate reflections, revise reasoning, and retry tasks to improve success rates.

---

# 12. Key Takeaway

SWE-bench has become the standard benchmark for evaluating autonomous AI coding agents on real-world software engineering tasks and serves as the foundation for measuring improvements in future failure recovery systems.