# Data Dictionary

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor ID |
| amfi_code | TEXT | Fund identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount | REAL | Transaction amount |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund identifier |
| return_1y | REAL | 1 Year Return |
| return_3y | REAL | 3 Year Return |
| return_5y | REAL | 5 Year Return |
| expense_ratio | REAL | Expense Ratio |