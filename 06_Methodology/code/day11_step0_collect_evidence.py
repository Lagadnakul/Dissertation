"""
DAY 11 - STEP 0: Collect REAL failure evidence from the Day 8 baseline logs.
For genuine test failures, pulls the actual pytest output. For malformed-patch
failures, pulls the actual patch-apply error text. This is the real ground
truth the Diagnose+Revise condition will use - not a guess, not a reflection.
"""

import os

TARGET_IDS = [
    "astropy__astropy-7746",
    "django__django-11019",
    "django__django-11283",
    "django__django-11564",
    "django__django-11620",
]

LOG_BASE = "logs/run_evaluation/day8_test/gemini-3.6-flash-blindretry-attempt1"
os.makedirs("attempts", exist_ok=True)

for instance_id in TARGET_IDS:
    test_output_path = os.path.join(LOG_BASE, instance_id, "test_output.txt")
    instance_log_path = os.path.join(LOG_BASE, instance_id, "run_instance.log")
    out_path = f"attempts/{instance_id}_realfailure_evidence.txt"

    print("=" * 60)
    print("Collecting evidence for:", instance_id)

    evidence = None

    if os.path.exists(test_output_path):
        with open(test_output_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if content.strip():
            evidence = "REAL TEST OUTPUT (from running the previous patch):\n" + content
            print("  Using real test_output.txt")

    if evidence is None and os.path.exists(instance_log_path):
        with open(instance_log_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if "Patch Apply Failed" in content:
            idx = content.find("Patch Apply Failed")
            snippet = content[idx: idx + 800]
            evidence = "REAL PATCH-APPLY ERROR (the previous patch could not even be applied):\n" + snippet
            print("  Using patch-apply error from run_instance.log")

    if evidence is None:
        print("  WARNING: no evidence file found - check the log path/run_id.")
        continue

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(evidence)
    print(f"  Saved: {out_path}")

print("=" * 60)
print("Evidence collection complete.")
