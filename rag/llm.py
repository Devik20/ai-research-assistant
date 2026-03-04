from groq import Groq
import os

class LocalLLM:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, prompt):
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150,
            )

            return completion.choices[0].message.content

        except Exception as e:
            return f"Error: {repr(e)}"