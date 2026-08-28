"""
DAY 7 - STEP 1: Generate first-attempt fixes for a larger pilot batch (20 tasks).
Goal: find out how many tasks genuinely fail on attempt 1, since those are the
ones needed for the actual recovery-method comparison (Blind Retry vs
Reflection-only vs Diagnose+Revise).
"""

from google import genai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import os
import re
import requests
import time

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")

# Larger pilot: first 20 tasks (buffer room in case some get skipped/blocked)
pilot_tasks = [dataset[i] for i in range(20)]

os.makedirs("attempts", exist_ok=True)


def extract_target_files(gold_patch):
    paths = re.findall(r"^--- a/(.+)$", gold_patch, re.MULTILINE)
    return [p for p in paths if "test" not in p.lower()]


def fetch_file(repo, commit, path):
    url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    return resp.text


for task in pilot_tasks:
    instance_id = task["instance_id"]
    output_path = f"attempts/{instance_id}_attempt1.txt"

    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        print(f"Skipping {instance_id} - already have a non-empty attempt.")
        continue

    print("=" * 60)
    print("Processing:", instance_id)

    target_files = extract_target_files(task["patch"])
    if not target_files:
        print(f"  Skipping {instance_id} - could not identify a target file.")
        continue

    file_path = target_files[0]
    real_content = fetch_file(task["repo"], task["base_commit"], file_path)

    if real_content is None:
        print(f"  Skipping {instance_id} - could not fetch {file_path}.")
        continue

    prompt = f"""You are an expert software engineer fixing a real bug in the open-source repository "{task['repo']}".

Here is the bug report:
---
{task['problem_statement']}
---

Here is the ACTUAL, CURRENT content of the file "{file_path}" that likely needs to change.
Use this EXACT content as the basis for your diff - do not guess or assume different code:

--- START OF FILE: {file_path} ---
{real_content}
--- END OF FILE ---

Propose a code fix for this bug. Respond in this exact format:

EXPLANATION:
<1-3 sentences explaining what you think is wrong and how you'll fix it>

PATCH:
<a valid unified diff (git diff format), based on the EXACT file content shown above>

CRITICAL RULES for the PATCH:
1. Base the diff ONLY on the exact file content shown above.
2. Each hunk header "@@ -A,B +C,D @@" must have B and D EXACTLY matching the number
   of lines that follow.
3. Include at least 3 unchanged context lines immediately before and after every change.
4. End the patch with a newline character after the last line.
5. Always wrap the diff inside a code block using ```diff and ``` on their own lines.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        try:
            reason = response.candidates[0].finish_reason
        except Exception:
            reason = "unknown"

        text = response.text or ""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"  finish_reason: {reason} | length: {len(text)} chars | Saved: {output_path}")
    except Exception as e:
        print(f"  ERROR generating fix for {instance_id}: {e}")

    time.sleep(3)

print("=" * 60)
print("Full pilot batch generation complete.")
