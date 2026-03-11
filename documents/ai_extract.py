import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def extract_invoice_data(text):

    prompt = f"""
    Extract the following fields from this invoice text:

    invoice_number
    vendor
    total_amount

    Return ONLY JSON.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"raw_output": content}