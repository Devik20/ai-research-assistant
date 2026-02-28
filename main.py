from transformers import pipeline

def load_llm():
    generator = pipeline(
        task="text2text-generation",
        model="google/flan-t5-base"
    )
    return generator

def ask_llm(generator, question):
    prompt = f"Answer the following question clearly and simply:\n\n{question}"

    response = generator(
        prompt,
        max_new_tokens=150,
        temperature=0.7
    )

    return response[0]["generated_text"]

if __name__ == "__main__":
    print("Loading model... (first time may take a minute)")
    llm = load_llm()

    while True:
        question = input("\nAsk something (type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer = ask_llm(llm, question)
        print("\nAnswer:\n", answer)