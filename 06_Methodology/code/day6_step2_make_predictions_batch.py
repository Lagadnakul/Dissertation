"""
DAY 6 - STEP 2: Combine all pilot-batch attempts into one predictions.json.
Reuses the auto-fix logic from Day 5 (a/ b/ prefixes, trailing newline).
"""

import json
import re
import os

from datasets import load_dataset

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
pilot_instance_ids = [dataset[i]["instance_id"] for i in range(5)]

predictions = []

for instance_id in pilot_instance_ids:
    attempt_file = f"attempts/{instance_id}_attempt1.txt"

    if not os.path.exists(attempt_file):
        print(f"Skipping {instance_id} - no attempt file found (generation may have failed).")
        continue

    with open(attempt_file, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"PATCH:\s*```(?:diff)?\s*(.*?)```", content, re.DOTALL)
    if not match:
        print(f"Skipping {instance_id} - no PATCH block found in attempt file.")
        continue

    patch_text = match.group(1).strip()

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

with open("predictions_batch1.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

print(f"Saved predictions_batch1.json with {len(predictions)} predictions.")
