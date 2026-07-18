# Paper 25

## File Name

Paper_25_RedCode_Risky_Code_Execution_and_Generation_Benchmark_for_Code_Agents.md

## Category

Category 6 – Benchmark and Evaluation for AI Coding Agents

## Paper Title

RedCode: Risky Code Execution and Generation Benchmark for Code Agents

## Authors

Chengquan Guo,
Xun Liu,
Chulin Xie,
Andy Zhou,
Yi Zeng,
Zinan Lin,
Dawn Song,
Bo Li

University of Chicago,
University of Illinois Urbana-Champaign,
Microsoft Research,
University of California Berkeley,
Virginia Tech

## Year

2024 (NeurIPS – Datasets and Benchmarks Track)

---

## 1. Problem Statement

Modern LLM-based coding agents can autonomously generate, execute, debug, and modify software. While these capabilities improve software development, they also introduce significant security and safety risks such as executing malicious code, deleting sensitive files, leaking confidential information, and generating vulnerable software. Existing benchmarks mainly evaluate code generation quality but fail to assess the safety of autonomous code agents during real execution. This paper addresses the need for a comprehensive benchmark to evaluate risky code execution and harmful code generation.

---

## 2. Methodology

The authors propose **RedCode**, a benchmark specifically designed to evaluate the safety of autonomous coding agents.

The benchmark consists of two major components:

### 1. RedCode-Exec

Evaluates whether AI coding agents can recognize and safely handle dangerous code execution tasks.

The benchmark includes:

- Python code snippets
- Bash scripts
- Natural language instructions
- Docker-based execution environment
- Real system interaction

It evaluates whether the agent executes or rejects risky operations.

---

### 2. RedCode-Gen

Evaluates whether coding agents generate malicious or harmful software when given risky programming tasks.

The benchmark tests the generation of software belonging to multiple malware families such as:

- Trojan
- Ransomware
- Spyware
- Adware
- Backdoor
- Worm
- Rootkit
- Botnet

---

### Risk Categories

The benchmark defines **25 risky scenarios** across **8 domains**, including:

- Website security
- File system
- Operating system
- Network
- Program logic
- Cyber security
- Data processing
- Software vulnerabilities

Examples include:

- Deleting sensitive files
- Unsafe deserialization
- Eval injection
- Reverse shell creation
- Privilege escalation
- Information leakage
- Network attacks
- Unsafe installations

---

### Evaluation Framework

RedCode evaluates agents using:

- Docker sandbox
- Execution monitoring
- Automated evaluation scripts
- Operation verification
- Output verification
- Attack Success Rate (ASR)
- Rejection Rate

Unlike previous work, evaluation is based on actual execution outcomes instead of only LLM-generated judgments.

---

## 3. Dataset / Benchmark

Benchmark:

- RedCode-Exec
- RedCode-Gen

Dataset Statistics:

- 4,050 risky execution test cases
- 160 malicious code generation prompts
- 25 risky scenarios
- 8 security domains

Evaluated Agent Frameworks:

- ReAct
- CodeAct
- OpenCodeInterpreter (OCI)

Foundation Models:

- GPT-4
- GPT-4o
- Claude 3.5
- GPT-3.5
- DeepSeek
- Llama 3
- Mistral
- CodeLlama
- Qwen

Evaluation Metrics:

- Attack Success Rate (ASR)
- Rejection Rate
- Safety Score
- Execution Outcome
- Malware Generation Quality

---

## 4. Results

Major findings include:

- Existing coding agents remain vulnerable to unsafe code execution.
- Agents are more likely to reject operating system attacks than logical programming errors.
- Natural language prompts lead to lower rejection rates than direct code snippets.
- GPT-4-level agents generate more sophisticated malicious software than smaller models.
- OpenCodeInterpreter demonstrates better safety performance compared to ReAct and CodeAct.
- Strong coding ability does not necessarily imply strong safety.

---

## 5. Strengths

- First comprehensive benchmark for autonomous code agent safety.
- Real Docker-based execution environment.
- Large-scale benchmark with over 4,000 execution scenarios.
- Covers both code execution and code generation.
- Includes diverse programming languages and natural language prompts.
- Uses objective execution-based evaluation instead of only LLM judgment.
- Covers multiple security domains and vulnerability types.

---

## 6. Limitations

- Focuses primarily on safety evaluation rather than failure recovery.
- Does not propose methods for automatic error correction.
- Limited to predefined risky scenarios.
- Mainly evaluates security-related failures instead of reasoning failures.
- Does not include self-reflection or adaptive recovery mechanisms.

---

## 7. Relation to My Research

This paper is highly relevant because my dissertation focuses on improving the reliability of autonomous coding agents through self-reflection-based failure recovery.

RedCode demonstrates that modern coding agents frequently execute unsafe operations or generate harmful software, highlighting the need for more intelligent recovery mechanisms.

While RedCode identifies and measures failures, my proposed framework aims to help coding agents analyze their failures, reflect on the root causes, revise their reasoning, and recover automatically instead of simply failing.

Therefore, this paper provides an important benchmark and motivation for evaluating the effectiveness of future failure recovery systems.

---

## 8. Key Contribution

The paper introduces **RedCode**, the first large-scale benchmark for evaluating the safety of autonomous coding agents through risky code execution and malicious code generation using real Docker-based execution environments, enabling comprehensive assessment of agent security and reliability.

---

## 9. Keywords

- RedCode
- Code Agents
- Agentic AI
- AI Coding Agents
- Code Execution
- Risk Assessment
- Software Security
- Benchmark
- Docker Sandbox
- Malware Generation
- Safe AI
- Autonomous Software Engineering

---

## My Notes

Importance for Dissertation:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Code Agent Evaluation
- Docker Sandbox
- Safety Benchmark
- Execution Monitoring
- Failure Detection
- Security Evaluation
- Risk Assessment
- Autonomous Code Execution

Why I Selected This Paper:

This paper provides one of the strongest evaluation benchmarks for autonomous coding agents. Although it focuses on security rather than failure recovery, it clearly demonstrates why reliable debugging, self-reflection, and automatic recovery mechanisms are essential for real-world AI coding systems. The benchmark can also serve as a valuable reference when discussing evaluation methods and future validation of my proposed failure recovery framework.