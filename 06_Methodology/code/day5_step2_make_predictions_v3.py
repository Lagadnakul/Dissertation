"""
DAY 5 - STEP 2 (predictions v3): Convert saved attempt into predictions.json.
Now auto-fixes two common LLM diff mistakes:
1. Guarantees exactly one trailing newline.
2. Adds missing "a/" and "b/" prefixes on --- / +++ lines (required for patch to
   correctly locate files - without this, the tool can strip the wrong folder name).
"""

import json
import re

instance_id = "astropy__astropy-12907"
attempt_file = f"attempts/{instance_id}_attempt2.txt"

with open(attempt_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"PATCH:\s*```(?:diff)?\s*(.*?)```", content, re.DOTALL)

if not match:
    raise ValueError(
        "Could not find a PATCH block in the attempt file. "
        "Check that the file contains 'PATCH:' followed by a ```diff ... ``` block."
    )

patch_text = match.group(1).strip()

# --- Auto-fix 1: add missing a/ b/ prefixes ---
fixed_lines = []
for line in patch_text.split("\n"):
    if line.startswith("--- ") and not line.startswith("--- a/") and "/dev/null" not in line:
        line = "--- a/" + line[len("--- "):]
    elif line.startswith("+++ ") and not line.startswith("+++ b/") and "/dev/null" not in line:
        line = "+++ b/" + line[len("+++ "):]
    fixed_lines.append(line)
patch_text = "\n".join(fixed_lines)

# --- Auto-fix 2: guarantee exactly one trailing newline ---
if not patch_text.endswith("\n"):
    patch_text += "\n"

prediction = {
    "instance_id": instance_id,
    "model_patch": patch_text,
    "model_name_or_path": "gemini-3.6-flash-attempt2"
}

with open("predictions.json", "w", encoding="utf-8") as f:
    json.dump([prediction], f, indent=2)

print("=" * 60)
print("Final patch (after auto-fixes):")
print(patch_text)
print("=" * 60)
print("Saved predictions.json - ready for the evaluation harness.")