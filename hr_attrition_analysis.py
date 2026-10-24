
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create a synthetic HR dataset for demonstration.
# This is not real employee data.
data = {
    "EmployeeID": range(1001, 1011),
    "Department": [
        "Sales", "IT", "HR", "Sales", "IT",
        "Finance", "Sales", "HR", "IT", "Finance"
    ],
    "YearsAtCompany": [1, 5, 2, 1, 7, 4, 2, 8, 1, 6],
    "MonthlyIncome": [
        2800, 5200, 3500, 3000, 6100,
        4800, 3200, 4300, 2900, 5000
    ],
    "Overtime": [
        "Yes", "No", "No", "Yes", "No",
        "No", "Yes", "No", "Yes", "No"
    ],
    "Attrition": [
        "Yes", "No", "No", "Yes", "No",
        "No", "Yes", "No", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Calculate overall attrition rate.
attrition_rate = (df["Attrition"] == "Yes").mean() * 100

print("HR ATTRITION ANALYSIS")
print("-" * 30)
print(f"Employees analysed: {len(df)}")
print(f"Employees who left: {(df['Attrition'] == 'Yes').sum()}")
print(f"Overall attrition rate: {attrition_rate:.1f}%")

# Calculate attrition by department.
department_attrition = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\nAttrition rate by department (%):")
print(department_attrition.round(1))

# Save the dataset and department summary.
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "synthetic_hr_data.csv", index=False)
department_attrition.rename("AttritionRatePercent").to_csv(
    output_dir / "department_attrition.csv"
)

# Create a chart.
sns.set_theme(style="whitegrid")
ax = department_attrition.plot(kind="bar", figsize=(8, 5))
ax.set_title("Employee Attrition Rate by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Attrition rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "department_attrition.png", dpi=150)
plt.show()

print("\nFiles saved in the outputs folder.")
