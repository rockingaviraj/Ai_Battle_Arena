import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Lightweight embedding model (CPU safe)
embedder = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

def build_index(chunks):
    vectors = embedder.encode(chunks)
    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    return index, vectors

def search(index_vectors, chunks, query, top_k=3):
    index, vectors = index_vectors

    q_vec = embedder.encode([query])
    q_vec = np.array(q_vec).astype("float32")

    _, ids = index.search(q_vec, top_k)
    return [chunks[i] for i in ids[0]]
