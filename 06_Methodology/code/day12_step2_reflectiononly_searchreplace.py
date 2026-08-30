"""
DAY 12 - STEP 2: Reflection-only, retrofitted with SEARCH/REPLACE format.
Only re-tests tasks that failed due to malformed patches under the old
diff format. Same reflection logic as Day 10 - shows the model its own
original attempt1 and asks for self-critique + revision, still with no
external test evidence.
"""

from google import genai
from datasets import load_dataset
from dotenv import load_dotenv, find_dotenv
import os
import re
import requests
import time
import json
import difflib

load_dotenv(find_dotenv())
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

TARGET_IDS = [
    "django__django-11019",
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


def build_diff(original_content, new_content, file_path):
    original_lines = original_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    diff = difflib.unified_diff(
        original_lines, new_lines,
        fromfile=f"a/{file_path}", tofile=f"b/{file_path}"
    )
    diff_text = "".join(diff)
    if not diff_text.endswith("\n"):
        diff_text += "\n"
    return diff_text


os.makedirs("attempts", exist_ok=True)
predictions = []
apply_log = []

for instance_id in TARGET_IDS:
    task = task_lookup.get(instance_id)
    original_attempt_path = f"attempts/{instance_id}_attempt1.txt"
    raw_output_path = f"attempts/{instance_id}_reflectiononly_v2_raw.txt"

    print("=" * 60)
    print("Reflection-only v2 (search/replace):", instance_id)

    with open(original_attempt_path, "r", encoding="utf-8") as f:
        previous_attempt_content = f.read()

    target_files = extract_target_files(task["patch"])
    file_path = target_files[0]
    real_content = fetch_file(task["repo"], task["base_commit"], file_path)

    prompt = f"""You are an expert software engineer. You previously attempted to fix a bug in the open-source repository "{task['repo']}", but your fix did NOT resolve the issue.

Here is the original bug report:
---
{task['problem_statement']}
---

Here is the ACTUAL, CURRENT content of the file "{file_path}":
--- START OF FILE: {file_path} ---
{real_content}
--- END OF FILE ---

Here was your PREVIOUS ATTEMPT, which did not successfully fix the bug:
---
{previous_attempt_content}
---

Reflect critically on what might be wrong with your previous reasoning, then provide a revised fix using SEARCH/REPLACE blocks - NOT a diff, NO line numbers.

Respond in this exact format:

REFLECTION:
<2-4 sentences critically reflecting on what might have been wrong with your previous attempt>

EXPLANATION:
<1-3 sentences explaining your revised fix>

EDITS:
<<<<<<< SEARCH
<exact original code, copied character-for-character from the file above - include enough surrounding lines to make this snippet unique in the file>
=======
<the new code that should replace it>
>>>>>>> REPLACE

(You may include multiple SEARCH/REPLACE blocks if separate parts of the file need to change. Each SEARCH block must match the file content EXACTLY.)
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        text = response.text or ""
        with open(raw_output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  Raw response saved ({len(text)} chars)")
    except Exception as e:
        print(f"  ERROR generating: {e}")
        apply_log.append({"instance_id": instance_id, "status": "generation_error", "detail": str(e)})
        time.sleep(60)
        continue

    blocks = re.findall(
        r"<<<<<<< SEARCH\n(.*?)\n=======\n(.*?)\n>>>>>>> REPLACE",
        text, re.DOTALL
    )

    if not blocks:
        print("  No SEARCH/REPLACE blocks found.")
        apply_log.append({"instance_id": instance_id, "status": "no_blocks_found"})
        time.sleep(60)
        continue

    working_content = real_content
    all_applied = True
    for search_text, replace_text in blocks:
        count = working_content.count(search_text)
        if count == 1:
            working_content = working_content.replace(search_text, replace_text, 1)
        elif count == 0:
            print("  SEARCH block not found (0 matches).")
            apply_log.append({"instance_id": instance_id, "status": "search_not_found"})
            all_applied = False
            break
        else:
            print(f"  SEARCH block ambiguous ({count} matches).")
            apply_log.append({"instance_id": instance_id, "status": "search_ambiguous", "matches": count})
            all_applied = False
            break

    if all_applied:
        diff_text = build_diff(real_content, working_content, file_path)
        predictions.append({
            "instance_id": instance_id,
            "model_patch": diff_text,
            "model_name_or_path": "gemini-3.6-flash-reflectiononly-v2-searchreplace"
        })
        print("  Applied successfully.")
        apply_log.append({"instance_id": instance_id, "status": "applied_ok"})

    time.sleep(60)

with open("predictions_reflectiononly_v2.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

print("=" * 60)
print(f"Saved predictions_reflectiononly_v2.json with {len(predictions)} predictions.")
