import os
import re

from config import UPLOAD_DIR, CHROMA_DB_PATH, EMBEDDING_MODEL

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


# -----------------------------
# CLEAN TEXT (IMPROVED)
# -----------------------------
def clean_text(text):
    # remove headers
    text = re.sub(r'ANDROID QUICK START GUIDE.*?\n', '', text)

    # remove page junk like "6 Accessibility 56"
    text = re.sub(r'\d+\sAccessibility.*?\n', '', text)

    # remove page numbers
    text = re.sub(r'\n?\d+\n', '\n', text)

    # remove broken words (hyphen line breaks)
    text = re.sub(r'-\s+', '', text)

    # normalize spacing
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# -----------------------------
# LOAD PDFs
# -----------------------------
def load_pdfs():
    texts = []

    for file in os.listdir(UPLOAD_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(UPLOAD_DIR, file)
            print(f"[INGEST] Loading: {file}")

            reader = PdfReader(path)
            raw_text = ""

            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    raw_text += extracted + "\n"

            cleaned = clean_text(raw_text)
            texts.append(cleaned)

    return texts


# -----------------------------
# MAIN
# -----------------------------
def main():
    print("\n[INGEST] Starting ingestion...\n")

    documents = load_pdfs()
    full_text = "\n".join(documents)

    print(f"[DEBUG] Text length: {len(full_text)}")

    # ✅ MUCH BETTER CHUNKING
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,        # 🔥 smaller = better retrieval
        chunk_overlap=120,     # 🔥 preserves context
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_text(full_text)

    print(f"[DEBUG] Chunks: {len(chunks)}")

    # embeddings
    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # ✅ add metadata (improves retrieval)
    metadatas = [{"source": f"chunk_{i}"} for i in range(len(chunks))]

    # vector DB
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        metadatas=metadatas,
        persist_directory=CHROMA_DB_PATH
    )

    print("\n[INGEST] ✅ DONE\n")


if __name__ == "__main__":
    main()