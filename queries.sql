-- Top 5 funds by NAV
SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code
ORDER BY MAX(nav) DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transaction count
SELECT COUNT(*)
FROM fact_transactions;

-- Total transaction amount
SELECT SUM(amount)
FROM fact_transactions;

-- Transaction type distribution
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Expense ratio below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Top 10 by 5Y return
SELECT *
FROM fact_performance
ORDER BY return_5y DESC
LIMIT 10;

-- Average 1Y return
SELECT AVG(return_1y)
FROM fact_performance;

-- Average 3Y return
SELECT AVG(return_3y)
FROM fact_performance;

-- Average 5Y return
SELECT AVG(return_5y)
FROM fact_performance;