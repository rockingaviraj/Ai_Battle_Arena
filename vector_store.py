from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Lazy-loaded embedder (IMPORTANT for Railway build timeout)
_embedder = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )
    return _embedder

def build_index(chunks):
    embedder = get_embedder()

    vectors = embedder.encode(chunks)
    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    return index
