"""
DAY 7 - STEP 2: Build predictions.json from all 20 pilot attempts.
Same tolerant extraction logic as Day 6 (handles fenced and unfenced patches).
"""

import json
import re
import os

from datasets import load_dataset

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
pilot_instance_ids = [dataset[i]["instance_id"] for i in range(20)]


def extract_patch(content):
    match = re.search(r"PATCH:\s*```(?:diff)?\s*(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1).strip()

    match = re.search(r"PATCH:\s*\n(.*)", content, re.DOTALL)
    if match:
        text = match.group(1).strip()
        text = re.sub(r"^```(?:diff)?\s*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
        return text.strip()

    return None


predictions = []
skipped = []

for instance_id in pilot_instance_ids:
    attempt_file = f"attempts/{instance_id}_attempt1.txt"

    if not os.path.exists(attempt_file):
        print(f"Skipping {instance_id} - no attempt file found.")
        skipped.append({"instance_id": instance_id, "reason": "no_attempt_file"})
        continue

    with open(attempt_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print(f"Skipping {instance_id} - empty attempt (likely blocked by safety filter).")
        skipped.append({"instance_id": instance_id, "reason": "empty_response_blocked"})
        continue

    patch_text = extract_patch(content)
    if not patch_text:
        print(f"Skipping {instance_id} - no PATCH content could be extracted.")
        skipped.append({"instance_id": instance_id, "reason": "no_patch_extracted"})
        continue

    fixed_lines = []
    for line in patch_text.split("\n"):
        if line.startswith("--- ") and not line.startswith("--- a/") and "/dev/null" not in line:
            line = "--- a/" + line[len("--- "):]
        elif line.startswith("+++ ") and not line.startswith("+++ b/") and "/dev/null" not in line:
            line = "+++ b/" + line[len("+++ "):]
        fixed_lines.append(line)
    patch_text = "\n".join(fixed_lines)

    if not patch_text.endswith("\n"):
        patch_text += "\n"

    predictions.append({
        "instance_id": instance_id,
        "model_patch": patch_text,
        "model_name_or_path": "gemini-3.6-flash-blindretry-attempt1"
    })

with open("predictions_pilot20.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

with open("skipped_pilot20.json", "w", encoding="utf-8") as f:
    json.dump(skipped, f, indent=2)

print(f"\nSaved predictions_pilot20.json with {len(predictions)} predictions.")
print(f"Saved skipped_pilot20.json with {len(skipped)} skipped tasks (see reasons inside).")
