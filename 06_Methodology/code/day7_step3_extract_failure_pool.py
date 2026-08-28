"""
DAY 7 - STEP 3: Build the "failure pool" - the list of tasks that did NOT
succeed on the first attempt. THIS is the dataset the recovery-method
comparison (Blind Retry vs Reflection-only vs Diagnose+Revise) will run on,
since there's nothing to recover from on tasks that already passed.
"""

import json
import sys

report_file = sys.argv[1]

with open(report_file, "r", encoding="utf-8") as f:
    report = json.load(f)

resolved = set(report.get("resolved_ids", []))
unresolved = set(report.get("unresolved_ids", []))
errored = set(report.get("error_ids", []))

with open("skipped_pilot20.json", "r", encoding="utf-8") as f:
    skipped = json.load(f)
blocked_ids = {s["instance_id"] for s in skipped}

failure_pool = sorted(unresolved | errored | blocked_ids)

print("=" * 50)
print(f"{'TASK ID':<35} {'RESULT'}")
print("-" * 50)
for instance_id in sorted(resolved):
    print(f"{instance_id:<35} PASS")
for instance_id in sorted(unresolved):
    print(f"{instance_id:<35} FAIL")
for instance_id in sorted(errored):
    print(f"{instance_id:<35} ERROR")
for s in skipped:
    print(f"{s['instance_id']:<35} BLOCKED ({s['reason']})")
print("=" * 50)
print(f"Passed on attempt 1: {len(resolved)}")
print(f"Failed / blocked (the FAILURE POOL for recovery experiments): {len(failure_pool)}")

with open("failure_pool.json", "w", encoding="utf-8") as f:
    json.dump(failure_pool, f, indent=2)

print("\nSaved failure_pool.json - this is what Day 8 builds the recovery comparison on.")
