import sqlite3
from google import genai
from dotenv import load_dotenv
import os
import re

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

question = input(
    "Ask question: "
)

schema = """
customer(
customer_id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
join_date TEXT
)

sales(
sale_id INTEGER PRIMARY KEY,
customer_id INTEGER,
product TEXT,
amount REAL,
sale_date TEXT
)
"""

prompt = f"""
Database Schema:

{schema}

Convert the user's question into SQLite SQL.

Question:

{question}

Rules:
1. Return ONLY SQL
2. No markdown
3. No explanation
4. Output must run in SQLite
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

sql = response.text.strip()

sql = re.sub(
    r"```sql|```",
    "",
    sql
).strip()

print(
    "\nGenerated SQL:\n"
)

print(sql)

conn = sqlite3.connect(
    "sql_extraction/sales.db"
)

cur = conn.cursor()

try:

    cur.execute(sql)

    rows = cur.fetchall()

    print(
        "\nQuery Result:\n"
    )

    if len(rows) == 0:

        print(
            "No results for the query."
        )

    else:

        for row in rows:

            print(row)

except Exception as e:

    print(
        "\nExecution Error:"
    )

    print(e)

finally:

    conn.close()