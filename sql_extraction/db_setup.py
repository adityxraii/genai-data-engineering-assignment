import sqlite3

conn = sqlite3.connect(
    "sql_extraction/sales.db"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS customer(
customer_id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
join_date TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sales(
sale_id INTEGER PRIMARY KEY,
customer_id INTEGER,
product TEXT,
amount REAL,
sale_date TEXT,

FOREIGN KEY(customer_id)
REFERENCES customer(customer_id)
)
""")

cur.execute("""
INSERT INTO customer
VALUES(
1,
'Aditya',
'aditya@test.com',
'2026-01-01'
)
""")

cur.execute("""
INSERT INTO sales
VALUES(
1,
1,
'Laptop',
50000,
'2026-05-20'
)
""")

conn.commit()

conn.close()

print(
"Database created"
)