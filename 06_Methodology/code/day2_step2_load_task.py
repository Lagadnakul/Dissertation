"""
DAY 2 - STEP 2
Purpose: Pull ONE real coding task from SWE-bench Lite and look at it.
"""

from datasets import load_dataset

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")

task = dataset[0]

print("=" * 60)
print("TASK ID:", task["instance_id"])
print("REPO:", task["repo"])
print("-" * 60)
print("PROBLEM STATEMENT (the bug report):")
print(task["problem_statement"][:1000], "...")
print("=" * 60)
print("Total tasks available:", len(dataset))