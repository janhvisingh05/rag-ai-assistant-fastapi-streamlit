from fastapi import FastAPI
from pydantic import BaseModel

# ✅ correct imports
from rag.retriever import retrieve_context
from llm.langchain_gemini import generate_response

app = FastAPI()


class QueryRequest(BaseModel):
    question: str
    history: str = ""


@app.post("/chat")
def chat(request: QueryRequest):
    context = retrieve_context(request.question)

    answer = generate_response(
        context=context,
        question=request.question,
        history=request.history
    )

    return {"answer": answer}