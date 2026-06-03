import pandas as pd

# NAV DATA
print("Loading NAV data...")

nav = pd.read_csv("Data/raw/02_nav_history.csv")

nav = nav.drop_duplicates()

nav.to_csv(
    "Data/processed/nav_history_clean.csv",
    index=False
)

print("NAV file cleaned")


# INVESTOR TRANSACTIONS
print("Loading Investor Transactions...")

txn = pd.read_csv(
    "Data/raw/08_investor_transactions.csv"
)

txn = txn.drop_duplicates()

txn.to_csv(
    "Data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions cleaned")


# SCHEME PERFORMANCE
print("Loading Scheme Performance...")

perf = pd.read_csv(
    "Data/raw/07_scheme_performance.csv"
)

perf = perf.drop_duplicates()

perf.to_csv(
    "Data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned")

print("All files cleaned successfully")