import json
import re
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_metadata(first_pages_text):
    prompt = f"""
You are an academic metadata extraction assistant.

Extract:
- Journal or Conference Name
- Publisher Name
- Authors
- Year of Publication
- DOI (if available)

Return ONLY valid JSON. No explanations.

TEXT:
{first_pages_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()

    # Extract JSON using regex
    json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)

    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            return {"error": "Invalid JSON returned", "raw_output": raw_output}
    else:
        return {"error": "No JSON found", "raw_output": raw_output}