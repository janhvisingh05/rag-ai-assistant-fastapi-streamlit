from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

# Load multilingual model
model = SentenceTransformer(EMBEDDING_MODEL)

def get_embeddings(texts):
    return model.encode(texts, normalize_embeddings=True).tolist()