"""
DAY 3 - STEP 1 (v2): First bug-fix attempt - stricter prompt to reduce malformed diffs.
"""

from google import genai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=API_KEY)

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
task = dataset[0]

problem_statement = task["problem_statement"]
repo = task["repo"]
instance_id = task["instance_id"]

prompt = f"""You are an expert software engineer fixing a real bug in the open-source repository "{repo}".

Here is the bug report:
---
{problem_statement}
---

Propose a code fix for this bug. Respond in this exact format:

EXPLANATION:
<1-3 sentences explaining what you think is wrong and how you'll fix it>

PATCH:
<a valid unified diff (git diff format)>

CRITICAL RULES for the PATCH (a broken diff cannot be applied at all):
1. Each hunk header "@@ -A,B +C,D @@" must have B and D EXACTLY matching the number
   of lines that follow (context lines + removed lines = B, context lines + added lines = D).
   Count carefully before writing the header.
2. Include at least 3 unchanged context lines immediately before and after every change.
3. Every line in the hunk must start with a space (unchanged), a "-" (removed), or a
   "+" (added) - no exceptions.
4. End the patch with a newline character after the last line.
5. Do not omit or truncate any part of the diff.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("=" * 60)
print("TASK:", instance_id)
print("=" * 60)
print(response.text)

os.makedirs("attempts", exist_ok=True)
output_path = f"attempts/{instance_id}_attempt1.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print("\nSaved to:", output_path)
