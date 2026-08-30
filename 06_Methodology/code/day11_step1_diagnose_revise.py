"""
DAY 11 - STEP 1: Diagnose + Revise condition.
Shows the model the REAL failure evidence (actual test output or actual
patch-apply error), asks it to diagnose the specific root cause based on
that real evidence, then provide a revised patch. This is the condition
that actually tests the paper's core research question.
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

TARGET_IDS = [
    "astropy__astropy-7746",
    "django__django-11019",
    "django__django-11283",
    "django__django-11564",
    "django__django-11620",
]

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

for instance_id in TARGET_IDS:
    task = task_lookup.get(instance_id)
    original_attempt_path = f"attempts/{instance_id}_attempt1.txt"
    evidence_path = f"attempts/{instance_id}_realfailure_evidence.txt"
    output_path = f"attempts/{instance_id}_diagnoserevise_attempt4.txt"

    print("=" * 60)
    print("Diagnose+Revise:", instance_id)

    if not os.path.exists(original_attempt_path) or not os.path.exists(evidence_path):
        print("  Missing original attempt or evidence file, skipping.")
        continue

    with open(original_attempt_path, "r", encoding="utf-8") as f:
        previous_attempt_content = f.read()
    with open(evidence_path, "r", encoding="utf-8") as f:
        real_evidence = f.read()

    target_files = extract_target_files(task["patch"])
    if not target_files:
        print("  No target file found, skipping.")
        continue

    file_path = target_files[0]
    real_content = fetch_file(task["repo"], task["base_commit"], file_path)
    if real_content is None:
        print("  Could not fetch file, skipping.")
        continue

    prompt = f"""You are an expert software engineer. You previously attempted to fix a bug in the open-source repository "{task['repo']}", but your fix did NOT resolve the issue.

Here is the original bug report:
---
{task['problem_statement']}
---

Here is the ACTUAL, CURRENT content of the file "{file_path}":
--- START OF FILE: {file_path} ---
{real_content}
--- END OF FILE ---

Here was your PREVIOUS ATTEMPT:
---
{previous_attempt_content}
---

Here is the REAL, ACTUAL result of running your previous patch against the real test suite (this is ground truth, not a guess):
---
{real_evidence}
---

Based on this REAL evidence (not speculation), diagnose the SPECIFIC root cause of why your previous attempt failed, then provide a revised fix. Respond in this exact format:

DIAGNOSIS:
<2-4 sentences identifying the specific root cause, grounded in the real evidence shown above>

EXPLANATION:
<1-3 sentences explaining your revised fix>

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
print("Diagnose+Revise generation complete.")
