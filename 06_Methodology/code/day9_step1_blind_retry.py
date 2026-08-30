"""
DAY 9 - STEP 1: Blind Retry condition.
For each task in the failure pool, retry the EXACT same prompt again -
no diagnosis, no reflection, no new information. Tests whether pure
random variation in generation ever fixes a failure on its own.
"""

from google import genai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import os
import re
import requests
import time
import json

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

with open("failure_pool.json", "r", encoding="utf-8") as f:
    failure_pool = json.load(f)

print(f"Failure pool has {len(failure_pool)} tasks: {failure_pool}")

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
task_lookup = {t["instance_id"]: t for t in dataset}


def extract_target_files(gold_patch):
    paths = re.findall(r"^--- a/(.+)$", gold_patch, re.MULTILINE)
    return [p for p in paths if "test" not in p.lower()]


def fetch_file(repo, commit, path):
    url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    return resp.text


os.makedirs("attempts", exist_ok=True)

for instance_id in failure_pool:
    task = task_lookup.get(instance_id)
    if task is None:
        print(f"  Could not find {instance_id} in dataset, skipping.")
        continue

    output_path = f"attempts/{instance_id}_blindretry_attempt2.txt"
    print("=" * 60)
    print("Blind retry:", instance_id)

    target_files = extract_target_files(task["patch"])
    if not target_files:
        print("  No target file found, skipping.")
        continue

    file_path = target_files[0]
    real_content = fetch_file(task["repo"], task["base_commit"], file_path)
    if real_content is None:
        print("  Could not fetch file, skipping.")
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
        text = response.text or ""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  Saved: {output_path} ({len(text)} chars)")
    except Exception as e:
        print(f"  ERROR: {e}")

    time.sleep(3)

print("=" * 60)
print("Blind retry generation complete.")
