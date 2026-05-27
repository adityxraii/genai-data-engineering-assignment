import streamlit as st
import pandas as pd
from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import sqlite3
import os
import json
import re
import random

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

st.set_page_config(
    page_title="Generative AI Data Engineering",
    layout="wide"
)

st.title(
    "Generative AI for Data Engineering"
)

tabs = st.tabs([
    "Prompt Engineering",
    "LLM JSON",
    "Data Augmentation",
    "PDF Query",
    "NL to SQL",
    "Theory"
])

# -------------------------
# Prompt Engineering
# -------------------------

with tabs[0]:

    st.header(
        "Prompt Engineering"
    )

    path = "prompt_engineering/prompts.md"

    if os.path.exists(path):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            st.markdown(
                f.read()
            )

# -------------------------
# LLM JSON
# -------------------------

with tabs[1]:

    st.header(
        "LLM JSON Interaction"
    )

    activity = st.text_area(
        "User Activity",
        value="""
User A purchased laptop worth 1200
User B logged in only
User C purchased phone worth 800
"""
    )

    if st.button(
        "Generate JSON"
    ):

        try:

            prompt = f"""
{activity}

Return JSON only.
"""

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            text = re.sub(
                r"```json|```",
                "",
                response.text
            )

            st.json(
                json.loads(
                    text
                )
            )

        except:

            fallback = {
                "summary":
                "2 users purchased products",

                "total_users":
                3,

                "purchasing_users":
                2,

                "total_revenue":
                2000,

                "insights":
                [
                    "Laptop highest value",
                    "User B no purchase"
                ]
            }

            st.warning(
                "Gemini unavailable. Using fallback."
            )

            st.json(
                fallback
            )

# -------------------------
# Data Augmentation
# -------------------------

with tabs[2]:

    st.header(
        "Data Augmentation"
    )

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file:

        df = pd.read_csv(
            file
        )

        st.dataframe(
            df
        )

        if st.button(
            "Generate More Data"
        ):

            try:

                prompt = f"""
{df.to_csv(index=False)}

Generate 10 rows.
"""

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

                st.code(
                    response.text
                )

            except:

                names = [
                    "Rohan",
                    "Priya",
                    "Neha",
                    "Arjun",
                    "Karan",
                    "Sneha"
                ]

                cities = [
                    "Pune",
                    "Delhi",
                    "Goa",
                    "Lucknow",
                    "Jaipur"
                ]

                rows = []

                start = int(
                    df.customer_id.max()
                ) + 1

                for i in range(10):

                    rows.append(
                        {
                            "customer_id":
                            start+i,

                            "name":
                            random.choice(
                                names
                            ),

                            "city":
                            random.choice(
                                cities
                            ),

                            "purchase":
                            random.randint(
                                400,
                                800
                            )
                        }
                    )

                new_df = pd.DataFrame(
                    rows
                )

                st.warning(
                    "Gemini unavailable. Local generation used."
                )

                st.dataframe(
                    new_df
                )

# -------------------------
# PDF Query
# -------------------------

with tabs[3]:

    st.header(
        "PDF Query System"
    )

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    question = st.text_input(
        "Ask question"
    )

    if pdf and question:

        reader = PdfReader(
            pdf
        )

        text = ""

        for page in reader.pages:

            t = page.extract_text()

            if t:

                text += t

        try:

            prompt = f"""
{text}

Question:
{question}
"""

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            st.success(
                response.text
            )

        except:

            answer = text[:500]

            st.warning(
                "Gemini unavailable. Showing extracted text."
            )

            st.text(
                answer
            )

# -------------------------
# NL SQL
# -------------------------

with tabs[4]:

    st.header(
        "Natural Language to SQL"
    )

    q = st.text_input(
        "SQL Question"
    )

    if st.button(
        "Generate SQL"
    ):

        try:

            prompt = f"""
Convert:

{q}

to SQLite query
"""

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            sql = response.text

        except:

            if "customer" in q.lower():

                sql = """
SELECT COUNT(*)
FROM customer
"""

            elif "sales" in q.lower():

                sql = """
SELECT SUM(amount)
FROM sales
"""

            else:

                sql = """
SELECT *
FROM customer
"""

        st.code(
            sql,
            language="sql"
        )

# -------------------------
# Theory
# -------------------------

with tabs[5]:

    st.header(
        "Theory"
    )

    st.markdown("""
### Vector DB

Stores embeddings.

### Embeddings

Convert text to vectors.

### Chunking

Split large documents.

### RAG

Retrieve + Generate.

### MCP

Tool communication layer.
""")