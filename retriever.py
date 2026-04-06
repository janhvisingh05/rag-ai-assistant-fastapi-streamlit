from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHROMA_DB_PATH, EMBEDDING_MODEL


# -----------------------------
# INIT VECTOR DB
# -----------------------------
def get_db():
    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding
    )

    return db


# -----------------------------
# RETRIEVE (🔥 FIXED)
# -----------------------------
def retrieve_context(query):
    db = get_db()

    # ✅ USE MMR (VERY IMPORTANT)
    docs = db.max_marginal_relevance_search(
        query,
        k=6,              # more candidates
        fetch_k=20        # deeper search
    )

    print(f"\n[DEBUG] Retrieved docs: {len(docs)}")

    context = "\n\n".join([doc.page_content for doc in docs])

    return context