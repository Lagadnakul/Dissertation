"""
DAY 14: Generate publication-ready charts from the master results.
Produces two PNG figures: (1) baseline outcome breakdown, (2) recovery
condition comparison on genuine logic failures. No API calls needed.
"""

import json
import matplotlib.pyplot as plt

with open("master_results.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

baseline_pass = sum(1 for v in master_data.values() if v["baseline"] == "PASS")
baseline_fail = sum(1 for v in master_data.values() if v["baseline"] == "FAIL")
baseline_error = sum(1 for v in master_data.values() if v["baseline"].startswith("ERROR"))

fig1, ax1 = plt.subplots(figsize=(6, 5))
categories = ["PASS\n(first attempt)", "FAIL\n(genuine logic)", "ERROR\n(malformed patch)"]
values = [baseline_pass, baseline_fail, baseline_error]
colors = ["#4CAF50", "#F44336", "#FF9800"]
bars = ax1.bar(categories, values, color=colors)
for bar, val in zip(bars, values):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2,
              str(val), ha="center", fontweight="bold")
ax1.set_ylabel("Number of tasks (out of 20)")
ax1.set_title("Baseline Outcome Breakdown (20-task pilot)")
ax1.set_ylim(0, 14)
plt.tight_layout()
plt.savefig("figure1_baseline_breakdown.png", dpi=200)
print("Saved figure1_baseline_breakdown.png")
plt.close()

genuine_fail_tasks = [k for k, v in master_data.items() if v["baseline"] == "FAIL"]
conditions = ["blind_retry", "reflection_only", "diagnose_revise"]
condition_labels = ["Blind Retry", "Reflection-only", "Diagnose+Revise"]

recovered_counts = [
    sum(1 for k in genuine_fail_tasks if master_data[k].get(cond, "").startswith("PASS"))
    for cond in conditions
]
not_recovered_counts = [len(genuine_fail_tasks) - c for c in recovered_counts]

fig2, ax2 = plt.subplots(figsize=(7, 5))
x = range(len(conditions))
ax2.bar(x, recovered_counts, label="Recovered", color="#4CAF50")
ax2.bar(x, not_recovered_counts, bottom=recovered_counts, label="Still Failed", color="#F44336")
ax2.set_xticks(list(x))
ax2.set_xticklabels(condition_labels)
ax2.set_ylabel(f"Genuine logic failures (out of {len(genuine_fail_tasks)})")
ax2.set_title("Recovery Strategy Comparison\n(genuine logic failures only)")
ax2.legend()
plt.tight_layout()
plt.savefig("figure2_recovery_comparison.png", dpi=200)
print("Saved figure2_recovery_comparison.png")
plt.close()

print("\nBoth figures saved in the current folder - ready to include in your paper.")
