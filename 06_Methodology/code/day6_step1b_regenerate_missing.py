"""
DAY 6 - STEP 1b: Regenerate the one task that came back empty, with debug info
to understand WHY (e.g. safety block, empty generation, etc.)
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

TARGET_IDS = ["astropy__astropy-14182"]


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

for task in dataset:
    if task["instance_id"] not in TARGET_IDS:
        continue

    instance_id = task["instance_id"]
    print("=" * 60)
    print("Regenerating:", instance_id)

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

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    try:
        print("  finish_reason:", response.candidates[0].finish_reason)
    except Exception as e:
        print("  (could not read finish_reason:", e, ")")

    text = response.text or ""
    print("  Response length:", len(text), "characters")

    output_path = f"attempts/{instance_id}_attempt1.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("  Saved:", output_path)

    time.sleep(3)

print("=" * 60)
print("Regeneration complete.")