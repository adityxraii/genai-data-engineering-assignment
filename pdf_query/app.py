from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

reader = PdfReader(
    "pdf_query/sample.pdf"
)

text = ""

for page in reader.pages:

    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"

question = input(
    "Ask question: "
)

prompt = f"""
Document:

{text}

Question:

{question}

Instructions:
1. Answer ONLY from the document
2. Do not hallucinate
3. If answer unavailable return:

Information not found.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(
    "\nAnswer:\n"
)

print(
    response.text
)