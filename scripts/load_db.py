import pandas as pd
import sqlite3

conn = sqlite3.connect("test.db")

nav = pd.read_csv("Data/processed/nav_history_clean.csv")
txn = pd.read_csv("Data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("Data/processed/scheme_performance_clean.csv")

nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
txn.to_sql("fact_transactions", conn, if_exists="replace", index=False)
perf.to_sql("fact_performance", conn, if_exists="replace", index=False)

conn.close()

print("Database Loaded Successfully")