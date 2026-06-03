import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS test(
    id INTEGER,
    name TEXT
)
""")

conn.commit()
conn.close()

print("SQLite Working")