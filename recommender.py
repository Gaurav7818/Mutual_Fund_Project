import pandas as pd

# Load scheme performance data
performance = pd.read_csv("Data/processed/scheme_performance_clean.csv")

print("Available Risk Levels:")
print(performance["risk_grade"].unique())

# Take user input
risk = input("\nEnter Risk Appetite (Low / Moderate / High): ").strip()

# Filter by risk grade
filtered = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
recommended = filtered.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")

print(
    recommended[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)