"""
DAY 4 - STEP 1 (v2): Convert saved attempt into predictions.json
Now guarantees the patch ends with exactly one trailing newline (patch/git apply requires this).
"""

import json
import re

instance_id = "astropy__astropy-12907"
attempt_file = f"attempts/{instance_id}_attempt1.txt"

with open(attempt_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"PATCH:\s*```(?:diff)?\s*(.*?)```", content, re.DOTALL)

if not match:
    raise ValueError(
        "Could not find a PATCH block in the attempt file. "
        "Check that the file contains 'PATCH:' followed by a ```diff ... ``` block."
    )

patch_text = match.group(1).strip()

# Guarantee exactly one trailing newline - required by git apply / patch
if not patch_text.endswith("\n"):
    patch_text += "\n"

prediction = {
    "instance_id": instance_id,
    "model_patch": patch_text,
    "model_name_or_path": "gemini-3.6-flash-attempt1"
}

with open("predictions.json", "w", encoding="utf-8") as f:
    json.dump([prediction], f, indent=2)

print("=" * 60)
print("Extracted patch:")
print(repr(patch_text))
print("=" * 60)
print("Saved predictions.json - ready for the evaluation harness.")