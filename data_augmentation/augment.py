import pandas as pd
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

df = pd.read_csv(
    "data_augmentation/sample.csv"
)

prompt = f"""
Dataset:

{df.to_string(index=False)}

Generate 10 more similar rows.

Rules:
1. Keep same columns
2. Generate realistic Indian names and cities
3. Keep purchase values similar
4. Return ONLY CSV
5. No explanation

Existing data:

{df.to_csv(index=False)}
"""

try:

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    print(
        "\nGenerated Data:\n"
    )

    print(
        response.text
    )

except Exception as e:

    msg = str(e)

    if "RESOURCE_EXHAUSTED" in msg:

        print(
"""
Gemini quota exhausted.

Options:

1. Wait and retry

2. Create another Gemini API key

3. Reduce testing frequency
"""
        )

    else:

        print(
            msg
        )