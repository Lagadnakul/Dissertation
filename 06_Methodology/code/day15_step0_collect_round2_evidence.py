"""
DAY 15 - STEP 0: Collect Round 2 evidence - the REAL test failures from
evaluating Round 1's Diagnose+Revise attempts (Day 11b), for the 4 tasks
that still failed. This is fresh evidence, different from Round 1's evidence.
"""

import os

TARGET_IDS = [
    "astropy__astropy-7746",
    "django__django-11019",
    "django__django-11283",
    "django__django-11564",
]

LOG_BASE = "logs/run_evaluation/day11b_tes/gemini-3.6-flash-diagnoserevise-v2-searchreplace"
os.makedirs("attempts", exist_ok=True)

for instance_id in TARGET_IDS:
    test_output_path = os.path.join(LOG_BASE, instance_id, "test_output.txt")
    instance_log_path = os.path.join(LOG_BASE, instance_id, "run_instance.log")
    out_path = f"attempts/{instance_id}_round2_evidence.txt"

    print("=" * 60)
    print("Collecting Round 2 evidence for:", instance_id)

    evidence = None

    if os.path.exists(test_output_path):
        with open(test_output_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if content.strip():
            evidence = "REAL TEST OUTPUT from Round 1's revised patch:\n" + content
            print("  Using real test_output.txt")

    if evidence is None and os.path.exists(instance_log_path):
        with open(instance_log_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if "Patch Apply Failed" in content:
            idx = content.find("Patch Apply Failed")
            evidence = "REAL PATCH-APPLY ERROR from Round 1's revised patch:\n" + content[idx: idx + 800]
            print("  Using patch-apply error from run_instance.log")

    if evidence is None:
        print("  WARNING: no evidence found - check the log path.")
        continue

    if len(evidence) > 3000:
        evidence = "...[earlier output trimmed]...\n" + evidence[-3000:]

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(evidence)
    print(f"  Saved: {out_path}")

print("=" * 60)
print("Round 2 evidence collection complete.")
