from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    user_question = input("Ask something: ")
    answer = ask_llm(user_question)
    print("\nAnswer:\n")
    print(answer)