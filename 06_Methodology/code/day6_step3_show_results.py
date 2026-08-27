"""
DAY 6 - STEP 4: Print a clean, simple results table from the harness's report JSON.
"""

import json
import sys

report_file = sys.argv[1] if len(sys.argv) > 1 else "gemini-3.6-flash-blindretry-attempt1.day6_test.json"

with open(report_file, "r", encoding="utf-8") as f:
    report = json.load(f)

resolved = set(report.get("resolved_ids", []))
unresolved = set(report.get("unresolved_ids", []))
errored = set(report.get("error_ids", []))

all_ids = resolved | unresolved | errored

print("=" * 50)
print(f"{'TASK ID':<35} {'RESULT'}")
print("-" * 50)
for instance_id in sorted(all_ids):
    if instance_id in resolved:
        result = "PASS"
    elif instance_id in errored:
        result = "ERROR"
    else:
        result = "FAIL"
    print(f"{instance_id:<35} {result}")
print("=" * 50)
print(f"Total: {len(all_ids)} | Passed: {len(resolved)} | Failed: {len(unresolved)} | Errors: {len(errored)}")
