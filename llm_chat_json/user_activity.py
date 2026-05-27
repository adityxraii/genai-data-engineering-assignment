from google import genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

prompt = """
User activity:

- User A logged in and purchased laptop worth $1200
- User B logged in but did not purchase
- User C purchased phone worth $800

Return ONLY JSON:

{
"summary":"",
"total_users":3,
"purchasing_users":2,
"total_revenue":2000,
"insights":[]
}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

text = response.text.strip()

text = re.sub(
    r"```json|```",
    "",
    text
).strip()

print(
    "\nRaw Output:\n"
)

print(text)

try:

    parsed = json.loads(text)

    print(
        "\nFormatted JSON:\n"
    )

    print(
        json.dumps(
            parsed,
            indent=4
        )
    )

except Exception as e:

    print(
        "\nJSON Error:"
    )

    print(e)