from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from config import GEMINI_API_KEY

# -----------------------------
# INIT GEMINI
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3   # slightly increased for better reasoning
)

# -----------------------------
# FIXED PROMPT (IMPORTANT)
# -----------------------------
prompt = PromptTemplate(
    input_variables=["context", "question", "history"],
    template="""
You are a helpful AI assistant answering questions based on a document.

RULES:
- Use the provided context to answer the question
- If the answer is clearly present → answer directly
- If the answer is partially present → infer and explain clearly
- If the answer is indirectly mentioned → still answer using context
- ONLY say "Answer not found in provided documents" if completely unrelated
- Keep answer concise and clear
- Use simple language

---------------------
Context:
{context}

---------------------
Chat History:
{history}

---------------------
Question:
{question}

---------------------
Answer:
"""
)

# -----------------------------
# CHAIN
# -----------------------------
chain = prompt | llm


# -----------------------------
# GENERATE RESPONSE
# -----------------------------
def generate_response(context, question, history):
    response = chain.invoke({
        "context": context,
        "question": question,
        "history": history
    })
    return response.content