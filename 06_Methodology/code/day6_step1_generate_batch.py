"""
DAY 6 - STEP 1: Generate attempts for a small pilot batch of 5 tasks.
Uses "oracle file localization": we extract WHICH file needs editing from the
task's own gold patch metadata (filenames only, never the actual fix content),
then fetch that file's real pre-fix content and ask the model to propose a fix.
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

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=API_KEY)

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")

# ---- Pilot batch: first 5 tasks only ----
pilot_tasks = [dataset[i] for i in range(5)]

os.makedirs("attempts", exist_ok=True)


def extract_target_files(gold_patch):
    """Pull out non-test source file paths that the gold patch touches."""
    paths = re.findall(r"^--- a/(.+)$", gold_patch, re.MULTILINE)
    # Skip test files - we only want to know which SOURCE file to look at
    return [p for p in paths if "test" not in p.lower()]


def fetch_file(repo, commit, path):
    url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    return resp.text


for task in pilot_tasks:
    instance_id = task["instance_id"]
    print("=" * 60)
    print("Processing:", instance_id)

    target_files = extract_target_files(task["patch"])
    if not target_files:
        print(f"  Skipping {instance_id} - could not identify a target file.")
        continue

    file_path = target_files[0]  # keep it simple: just the first file for now
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
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        output_path = f"attempts/{instance_id}_attempt1.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"  Saved: {output_path}")
    except Exception as e:
        print(f"  ERROR generating fix for {instance_id}: {e}")

    time.sleep(3)  # be polite to the free-tier rate limit

print("=" * 60)
print("Pilot batch generation complete.")
