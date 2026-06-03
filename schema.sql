CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code TEXT,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code TEXT,
    transaction_date DATE,
    transaction_type TEXT,
    amount REAL
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code TEXT,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL
);