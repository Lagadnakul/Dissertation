"""
DAY 9 - STEP 2: Build predictions.json from the blind retry attempts.
"""

import json
import re
import os

with open("failure_pool.json", "r", encoding="utf-8") as f:
    failure_pool = json.load(f)


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

for instance_id in failure_pool:
    attempt_file = f"attempts/{instance_id}_blindretry_attempt2.txt"

    if not os.path.exists(attempt_file):
        print(f"Skipping {instance_id} - no blind retry attempt found.")
        continue

    with open(attempt_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print(f"Skipping {instance_id} - empty response.")
        continue

    patch_text = extract_patch(content)
    if not patch_text:
        print(f"Skipping {instance_id} - no PATCH content extracted.")
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
        "model_name_or_path": "gemini-3.6-flash-blindretry-attempt2"
    })

with open("predictions_blindretry.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

print(f"Saved predictions_blindretry.json with {len(predictions)} predictions.")
