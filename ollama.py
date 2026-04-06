import ollama

def generate_response(context, question, history):

    prompt = f"""
You are a strict RAG-based assistant.

RULES:
- Answer ONLY from the given context
- If answer is not in context → say "Answer not found in provided documents"
- Do NOT hallucinate
- Keep answer concise
- Answer in same language as user

Context:
{context}

Chat History:
{history}

Question:
{question}
"""

    response = ollama.chat(
        model="gemma2:2b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2,
            "num_predict": 300
        }
    )

    return response["message"]["content"]