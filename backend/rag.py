import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
