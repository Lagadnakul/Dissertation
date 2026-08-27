"""
DAY 6 - STEP 2 (v2): Combine all pilot-batch attempts into predictions.json.
Now tolerates patches that aren't wrapped in ```diff fences (fixes the
astropy-6938 case where the model skipped the code fence entirely).
"""

import json
import re
import os

from datasets import load_dataset

dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
pilot_instance_ids = [dataset[i]["instance_id"] for i in range(5)]


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

for instance_id in pilot_instance_ids:
    attempt_file = f"attempts/{instance_id}_attempt1.txt"

    if not os.path.exists(attempt_file):
        print(f"Skipping {instance_id} - no attempt file found.")
        continue

    with open(attempt_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print(f"Skipping {instance_id} - attempt file is empty (regenerate this one).")
        continue

    patch_text = extract_patch(content)
    if not patch_text:
        print(f"Skipping {instance_id} - no PATCH content could be extracted.")
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

with open("predictions_batch1.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

print(f"Saved predictions_batch1.json with {len(predictions)} predictions.")