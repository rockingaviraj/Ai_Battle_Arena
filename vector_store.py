from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

def build_index(chunks):
    vectors = vectorizer.fit_transform(chunks)
    return vectors

def search(vectors, chunks, query, top_k=2):
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, vectors)[0]
    top_ids = np.argsort(scores)[-top_k:][::-1]
    return [chunks[i] for i in top_ids]
