"""
DAY 5 - STEP 1: Fetch the REAL file content (at the exact commit) and generate
a patch attempt based on actual code, not guessed code.
"""

from google import genai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import os
import requests

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=API_KEY)

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
task = dataset[0]

problem_statement = task["problem_statement"]
repo = task["repo"]
base_commit = task["base_commit"]
instance_id = task["instance_id"]

file_path = "astropy/modeling/separable.py"

raw_url = f"https://raw.githubusercontent.com/{repo}/{base_commit}/{file_path}"
print("Fetching real file from:", raw_url)

file_response = requests.get(raw_url)
if file_response.status_code != 200:
    raise ValueError(f"Could not fetch file (status {file_response.status_code}). Check the URL/path.")

real_file_content = file_response.text
print(f"Fetched {len(real_file_content)} characters of REAL file content.")

prompt = f"""You are an expert software engineer fixing a real bug in the open-source repository "{repo}".

Here is the bug report:
---
{problem_statement}
---

Here is the ACTUAL, CURRENT content of the file "{file_path}" that likely needs to change.
Use this EXACT content as the basis for your diff - do not guess or assume different code:

--- START OF FILE: {file_path} ---
{real_file_content}
--- END OF FILE ---

Propose a code fix for this bug. Respond in this exact format:

EXPLANATION:
<1-3 sentences explaining what you think is wrong and how you'll fix it>

PATCH:
<a valid unified diff (git diff format), based on the EXACT file content shown above>

CRITICAL RULES for the PATCH:
1. Base the diff ONLY on the exact file content shown above - every context line
   you keep or remove must appear EXACTLY as shown.
2. Each hunk header "@@ -A,B +C,D @@" must have B and D EXACTLY matching the number
   of lines that follow.
3. Include at least 3 unchanged context lines immediately before and after every change.
4. End the patch with a newline character after the last line.
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
output_path = f"attempts/{instance_id}_attempt2.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print("\nSaved to:", output_path)