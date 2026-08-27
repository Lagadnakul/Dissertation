# Paper 04

## Title
SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

## Authors
John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret,
Shunyu Yao, Karthik Narasimhan, Ofir Press

## Conference
NeurIPS 2024

---

# Research Category

Category 2
AI Coding Agent Frameworks

---

# 1. What problem does this paper solve?

Existing LLMs struggle to perform complete software engineering tasks because they interact only through basic terminal commands.

They cannot efficiently:
- Navigate large repositories
- Search relevant files
- Edit code safely
- Recover from editing mistakes

The paper introduces SWE-agent, which provides a specialized Agent-Computer Interface (ACI) that allows AI agents to interact with software projects more effectively.

---

# 2. What methodology is used?

The authors developed SWE-agent based on an Agent-Computer Interface (ACI).

The framework provides:

- Repository navigation
- Intelligent file search
- File viewer
- Code editor
- Context management
- Execution of tests
- Guardrails using linting
- Continuous feedback loop

The system was evaluated using:

- SWE-bench
- SWE-bench Lite
- HumanEvalFix

Performance was compared against Shell-only agents and Retrieval-Augmented Generation (RAG) approaches.

---

# 3. What results are achieved?

Major findings include:

• SWE-agent achieved 12.47% success on SWE-bench.

• 18% success on SWE-bench Lite.

• 87.7% Pass@1 on HumanEvalFix.

• Outperformed Shell-only and RAG baselines.

• Linting and guardrails significantly improved recovery from editing errors.

• A specialized Agent-Computer Interface improves software engineering performance without changing the underlying language model.

---

# 4. What are the limitations?

- Success rate is still relatively low for complex software engineering tasks.

- Many failures occur due to incorrect implementations.

- Recovery after repeated editing mistakes remains difficult.

- Performance depends on large-context language models.

- Cannot solve every GitHub issue autonomously.

---

# 5. How is my research different?

This paper focuses on improving the interaction between AI agents and computers using an Agent-Computer Interface (ACI).

My dissertation focuses on improving failure recovery after the agent makes mistakes.

Instead of only providing a better interface, my proposed framework will introduce:

- Self-reflection
- Failure analysis
- Iterative repair
- Recovery strategy generation

to increase the success rate after intermediate failures.

---

# Key Contribution

Introduced the Agent-Computer Interface (ACI), enabling AI coding agents to interact with repositories more effectively and significantly improving software engineering performance.

---

# Important Notes for Dissertation

Useful for:

✔ Literature Review

✔ Related Work

✔ Existing AI Coding Frameworks

✔ SWE-bench Benchmark

✔ Failure Recovery Discussion

✔ Agent Workflow
