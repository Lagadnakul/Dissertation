# Paper 27

## File Name

Paper_27_API_Bank_A_Comprehensive_Benchmark_for_Tool_Augmented_LLMs.md

## Category

Category 6 – Tool-Augmented LLM Benchmarks

## Paper Title

API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs

## Authors

Minghao Li,
Yingxiu Zhao,
Bowen Yu,
Feifan Song,
Hangyu Li,
Haiyang Yu,
Zhoujun Li,
Fei Huang,
Yongbin Li

Alibaba Group,
Hong Kong University of Science and Technology,
Peking University

## Year

2023 (EMNLP)

---

## 1. Problem Statement

Large Language Models (LLMs) are increasingly being integrated with external tools such as APIs, search engines, calculators, and software services. However, there is no standardized benchmark to evaluate whether LLMs can effectively select, retrieve, plan, and correctly invoke APIs. Existing benchmarks focus mainly on code generation or tool invocation but fail to comprehensively assess real-world tool usage capabilities.

---

## 2. Methodology

The authors introduce **API-Bank**, the first comprehensive benchmark for evaluating tool-augmented LLMs.

The benchmark evaluates three core abilities:

### 1. API Call

The model is given the correct API and must generate the appropriate API call using the correct parameters.

### 2. Retrieve + Call

The model must first identify the correct API from a large API pool and then execute it correctly.

### 3. Plan + Retrieve + Call

The most difficult setting where the model:

- Understands user intent
- Plans multiple steps
- Retrieves appropriate APIs
- Executes several API calls
- Produces the final response

The benchmark also introduces a runnable execution environment that verifies whether the generated API calls actually work.

---

## 3. Dataset / Benchmark

Benchmark:

API-Bank

Evaluation System:

- 73 executable APIs
- 314 manually annotated dialogues
- 753 API calls

Training Dataset:

- 2,138 APIs
- 1,888 dialogues
- 1,000 different domains
- 4,149 API calls

Generated using:

- Multi-Agent Data Generation Framework

Compared Models:

- GPT-3
- GPT-3.5
- GPT-4
- Alpaca-7B
- ChatGLM-6B
- Lynx-7B

Evaluation Metrics:

- API Call Accuracy
- ROUGE-L
- Planning Accuracy
- Retrieval Accuracy

---

## 4. Results

Main findings:

- GPT-4 achieved the best planning performance.
- GPT-3.5 performed well in API retrieval and calling.
- GPT-3 showed very poor API usage capability.
- Fine-tuned Lynx significantly outperformed Alpaca.
- API planning remains the most difficult capability.
- Current LLMs still struggle with multi-step tool reasoning.

---

## 5. Strengths

- First comprehensive benchmark for tool-augmented LLMs.
- Introduces three levels of tool usage evaluation.
- Uses executable APIs instead of simulated evaluation.
- Covers over 2,000 APIs across 1,000 domains.
- Includes planning, retrieval, and execution together.
- High-quality manually annotated evaluation set.

---

## 6. Limitations

- Focuses on API usage rather than autonomous coding agents.
- Does not include self-reflection mechanisms.
- Does not evaluate failure recovery.
- Limited to predefined APIs.
- Mainly measures tool usage ability rather than software engineering performance.

---

## 7. Relation to My Research

This paper is highly relevant because autonomous coding agents depend heavily on external tools for software engineering tasks.

My dissertation focuses on self-reflection-based failure recovery for AI coding systems.

Before an agent can recover from failures, it must first correctly select, retrieve, and execute external tools. API-Bank provides a strong benchmark for evaluating these capabilities and highlights current limitations in planning and tool utilization. These findings support the motivation for developing more reliable and intelligent coding agents.

---

## 8. Key Contribution

The paper introduces API-Bank, the first comprehensive benchmark for evaluating planning, API retrieval, and API execution capabilities of tool-augmented LLMs using real executable APIs and large-scale multi-domain datasets.

---

## 9. Keywords

- API-Bank
- Tool-Augmented LLM
- API Retrieval
- API Calling
- Tool Planning
- LLM Agents
- Tool Use
- API Benchmark
- Autonomous Agents
- Large Language Models

---

## My Notes

Importance for Dissertation:

⭐⭐⭐⭐⭐ (5/5)

Useful Ideas:

- Tool Selection
- API Retrieval
- Multi-Step Planning
- API Execution
- Tool Benchmark
- Agent Evaluation
- Planning Capability

Why I Selected This Paper:

This paper provides one of the most comprehensive benchmarks for evaluating tool usage in LLM agents. Since modern AI coding agents rely heavily on APIs and external tools for code execution, testing, and debugging, API-Bank offers valuable evaluation methods and highlights current limitations that motivate the need for improved failure recovery and self-reflection mechanisms.