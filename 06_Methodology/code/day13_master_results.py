"""
DAY 13: Master Results Consolidation.
Builds the final, complete results table across the 20-task baseline and all
three recovery conditions (Blind Retry, Reflection-only, Diagnose+Revise),
using the VERIFIED, RETROFITTED results from Days 8-12. No API calls needed -
this is pure consolidation of results already collected and confirmed.
"""

import json

master_data = {
    "astropy__astropy-12907": {"baseline": "PASS"},
    "astropy__astropy-14365": {"baseline": "PASS"},
    "astropy__astropy-14995": {"baseline": "PASS"},
    "astropy__astropy-6938": {"baseline": "PASS"},
    "django__django-10914": {"baseline": "PASS"},
    "django__django-10924": {"baseline": "PASS"},
    "django__django-11001": {"baseline": "PASS"},
    "django__django-11049": {"baseline": "PASS"},
    "django__django-11099": {"baseline": "PASS"},
    "django__django-11133": {"baseline": "PASS"},
    "django__django-11179": {"baseline": "PASS"},
    "django__django-11422": {"baseline": "PASS"},

    "astropy__astropy-7746": {
        "baseline": "FAIL", "blind_retry": "FAIL",
        "reflection_only": "FAIL", "diagnose_revise": "FAIL"
    },
    "django__django-11019": {
        "baseline": "FAIL", "blind_retry": "FAIL",
        "reflection_only": "FAIL", "diagnose_revise": "FAIL"
    },
    "django__django-11283": {
        "baseline": "FAIL", "blind_retry": "FAIL",
        "reflection_only": "FAIL", "diagnose_revise": "FAIL"
    },
    "django__django-11564": {
        "baseline": "FAIL", "blind_retry": "FAIL",
        "reflection_only": "FAIL", "diagnose_revise": "FAIL"
    },

    "astropy__astropy-14182": {
        "baseline": "ERROR (malformed)", "blind_retry": "EXCLUDED (permanently blocked - RECITATION)",
        "reflection_only": "EXCLUDED (permanently blocked - RECITATION)",
        "diagnose_revise": "EXCLUDED (permanently blocked - RECITATION)"
    },
    "django__django-11039": {
        "baseline": "ERROR (malformed)", "blind_retry": "PASS (old tooling, not retrofitted)",
        "reflection_only": "NOT_TESTED (already resolved, skipped to save quota)",
        "diagnose_revise": "NOT_TESTED (already resolved, skipped to save quota)"
    },
    "django__django-11583": {
        "baseline": "ERROR (malformed)", "blind_retry": "PASS (old tooling, not retrofitted)",
        "reflection_only": "NOT_TESTED (already resolved, skipped to save quota)",
        "diagnose_revise": "NOT_TESTED (already resolved, skipped to save quota)"
    },
    "django__django-11620": {
        "baseline": "ERROR (malformed)", "blind_retry": "PASS (retrofitted, verified)",
        "reflection_only": "PASS (retrofitted, verified)",
        "diagnose_revise": "PASS (retrofitted, verified)"
    },
}

total_tasks = len(master_data)
baseline_pass = sum(1 for v in master_data.values() if v["baseline"] == "PASS")
baseline_fail = sum(1 for v in master_data.values() if v["baseline"] == "FAIL")
baseline_error = sum(1 for v in master_data.values() if v["baseline"].startswith("ERROR"))

genuine_fail_tasks = [k for k, v in master_data.items() if v["baseline"] == "FAIL"]
malformed_tasks = [k for k, v in master_data.items() if v["baseline"].startswith("ERROR")]

genuine_recovered = {
    cond: sum(1 for k in genuine_fail_tasks if master_data[k].get(cond, "").startswith("PASS"))
    for cond in ["blind_retry", "reflection_only", "diagnose_revise"]
}

print("=" * 70)
print("MASTER RESULTS SUMMARY")
print("=" * 70)
print(f"Total pilot tasks: {total_tasks}")
print(f"Baseline PASS (no recovery needed): {baseline_pass} ({baseline_pass/total_tasks:.0%})")
print(f"Baseline genuine logic FAIL: {baseline_fail} ({baseline_fail/total_tasks:.0%})")
print(f"Baseline malformed-patch ERROR: {baseline_error} ({baseline_error/total_tasks:.0%})")
print()
print(f"Genuine logic failures recovered (out of {len(genuine_fail_tasks)}):")
for cond, count in genuine_recovered.items():
    print(f"  {cond}: {count}/{len(genuine_fail_tasks)} ({count/len(genuine_fail_tasks):.0%})")
print()
print(f"Malformed-patch cases ({len(malformed_tasks)} total):")
print("  1 permanently excluded (safety-blocked, no valid data)")
print("  2 resolved under old tooling only (not independently reverified)")
print("  1 resolved and CONFIRMED under retrofitted, reliable tooling across all 3 conditions")

with open("master_results.json", "w", encoding="utf-8") as f:
    json.dump(master_data, f, indent=2)

with open("master_results_table.md", "w", encoding="utf-8") as f:
    f.write("| Task | Baseline | Blind Retry | Reflection-only | Diagnose+Revise |\n")
    f.write("|---|---|---|---|---|\n")
    for task_id, results in master_data.items():
        row = [
            task_id,
            results.get("baseline", "-"),
            results.get("blind_retry", "-"),
            results.get("reflection_only", "-"),
            results.get("diagnose_revise", "-"),
        ]
        f.write("| " + " | ".join(row) + " |\n")

print()
print("Saved master_results.json and master_results_table.md")
