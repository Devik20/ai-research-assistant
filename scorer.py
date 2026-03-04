import json
import re
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def evaluate_paper(full_text):
    prompt = f"""
You are an expert academic reviewer.

Evaluate using this rubric:

Problem Clarity (0–2)
Methodology Strength (0–2)
Experimental Design (0–2)
Statistical Rigor (0–1)
Reproducibility (0–1)
Novelty (0–1)
Ethics (0–1)

Return ONLY valid JSON including:
- individual scores
- total score
- major strengths
- major weaknesses
- improvement suggestions

PAPER TEXT:
{full_text[:12000]}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()

    json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)

    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            return {"error": "Invalid JSON returned", "raw_output": raw_output}
    else:
        return {"error": "No JSON found", "raw_output": raw_output}