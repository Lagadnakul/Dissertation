"""
DAY 15 - STEP 1: Round 2 generation for all three conditions, on the 4
still-failing genuine logic bugs. Uses SEARCH/REPLACE + programmatic diff
throughout (no diff-format risk this time). Produces 3 predictions files.
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
    "astropy__astropy-7746",
    "django__django-11019",
    "django__django-11283",
    "django__django-11564",
]

REFLECTION_ROUND1_FILE = {
    "astropy__astropy-7746": "attempts/astropy__astropy-7746_reflectiononly_attempt3.txt",
    "django__django-11019": "attempts/django__django-11019_reflectiononly_v2_raw.txt",
    "django__django-11283": "attempts/django__django-11283_reflectiononly_attempt3.txt",
    "django__django-11564": "attempts/django__django-11564_reflectiononly_attempt3.txt",
}

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
task_lookup = {t["instance_id"]: t for t in dataset}


def extract_target_files(gold_patch):
    paths = re.findall(r"^--- a/(.+)$", gold_patch, re.MULTILINE)
    return [p for p in paths if "test" not in p.lower()]


def fetch_file(repo, commit, path):
    resp = requests.get(f"https://raw.githubusercontent.com/{repo}/{commit}/{path}")
    return resp.text if resp.status_code == 200 else None


def build_diff(original_content, new_content, file_path):
    diff = difflib.unified_diff(
        original_content.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=f"a/{file_path}", tofile=f"b/{file_path}"
    )
    diff_text = "".join(diff)
    return diff_text if diff_text.endswith("\n") or not diff_text else diff_text + "\n"


def apply_search_replace(text, real_content):
    blocks = re.findall(r"<<<<<<< SEARCH\n(.*?)\n=======\n(.*?)\n>>>>>>> REPLACE", text, re.DOTALL)
    if not blocks:
        return None, "no_blocks_found"
    working = real_content
    for search_text, replace_text in blocks:
        count = working.count(search_text)
        if count == 1:
            working = working.replace(search_text, replace_text, 1)
        elif count == 0:
            return None, "search_not_found"
        else:
            return None, "search_ambiguous"
    return working, "ok"


EDIT_INSTRUCTIONS = """Respond in this exact format:

{header}:
<your reasoning>

EXPLANATION:
<1-3 sentences explaining your revised fix>

EDITS:
<<<<<<< SEARCH
<exact original code, copied character-for-character - include enough context to be unique>
=======
<the new code that should replace it>
>>>>>>> REPLACE

(Multiple SEARCH/REPLACE blocks allowed. Each SEARCH block must match EXACTLY.)
"""

os.makedirs("attempts", exist_ok=True)
all_predictions = {"blind_retry_round2": [], "reflection_round2": [], "diagnose_revise_round2": []}

for instance_id in TARGET_IDS:
    task = task_lookup[instance_id]
    target_files = extract_target_files(task["patch"])
    file_path = target_files[0]
    real_content = fetch_file(task["repo"], task["base_commit"], file_path)

    print("=" * 60)
    print("Blind Retry Round 2:", instance_id)
    prompt = f"""You are an expert software engineer fixing a real bug in "{task['repo']}".

Bug report:
---
{task['problem_statement']}
---

Current file "{file_path}":
--- START OF FILE ---
{real_content}
--- END OF FILE ---

{EDIT_INSTRUCTIONS.format(header="EXPLANATION")}"""
    resp = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
    working, status = apply_search_replace(resp.text or "", real_content)
    if status == "ok":
        all_predictions["blind_retry_round2"].append({
            "instance_id": instance_id, "model_patch": build_diff(real_content, working, file_path),
            "model_name_or_path": "gemini-3.6-flash-blindretry-round2"
        })
        print("  Applied OK")
    else:
        print("  Not applied:", status)
    time.sleep(60)

    print("Reflection Round 2:", instance_id)
    with open(REFLECTION_ROUND1_FILE[instance_id], "r", encoding="utf-8") as f:
        round1_reflection = f.read()
    prompt = f"""You are an expert software engineer. Your last TWO attempts to fix a bug in "{task['repo']}" both failed.

Bug report:
---
{task['problem_statement']}
---

Current file "{file_path}":
--- START OF FILE ---
{real_content}
--- END OF FILE ---

Your most recent attempt (which also failed):
---
{round1_reflection}
---

{EDIT_INSTRUCTIONS.format(header="REFLECTION")}"""
    resp = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
    working, status = apply_search_replace(resp.text or "", real_content)
    if status == "ok":
        all_predictions["reflection_round2"].append({
            "instance_id": instance_id, "model_patch": build_diff(real_content, working, file_path),
            "model_name_or_path": "gemini-3.6-flash-reflection-round2"
        })
        print("  Applied OK")
    else:
        print("  Not applied:", status)
    time.sleep(60)

    print("Diagnose+Revise Round 2:", instance_id)
    with open(f"attempts/{instance_id}_diagnoserevise_v2_raw.txt", "r", encoding="utf-8") as f:
        round1_diagnose = f.read()
    with open(f"attempts/{instance_id}_round2_evidence.txt", "r", encoding="utf-8") as f:
        round2_evidence = f.read()
    prompt = f"""You are an expert software engineer. Your last attempt to fix a bug in "{task['repo']}" was based on a diagnosis, but it STILL did not resolve the issue.

Bug report:
---
{task['problem_statement']}
---

Current file "{file_path}":
--- START OF FILE ---
{real_content}
--- END OF FILE ---

Your previous diagnosis and revised attempt:
---
{round1_diagnose}
---

Here is the REAL, FRESH result of running that revised patch (ground truth):
---
{round2_evidence}
---

Diagnose again, based on this NEW evidence, then revise. {EDIT_INSTRUCTIONS.format(header="DIAGNOSIS")}"""
    resp = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)
    working, status = apply_search_replace(resp.text or "", real_content)
    if status == "ok":
        all_predictions["diagnose_revise_round2"].append({
            "instance_id": instance_id, "model_patch": build_diff(real_content, working, file_path),
            "model_name_or_path": "gemini-3.6-flash-diagnoserevise-round2"
        })
        print("  Applied OK")
    else:
        print("  Not applied:", status)
    time.sleep(60)

for cond, preds in all_predictions.items():
    with open(f"predictions_{cond}.json", "w", encoding="utf-8") as f:
        json.dump(preds, f, indent=2)
    print(f"Saved predictions_{cond}.json with {len(preds)} predictions.")
