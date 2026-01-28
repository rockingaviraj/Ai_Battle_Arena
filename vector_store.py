from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# embedding model (global, ek hi baar load)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(chunks):
    # text → vectors
    vectors = embedder.encode(chunks)
    vectors = np.array(vectors).astype("float32")  # 👈 VERY IMPORTANT

    # FAISS index
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    return index