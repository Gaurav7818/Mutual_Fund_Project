import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT
)
""")

conn.commit()
conn.close()

print("Tables created successfully")