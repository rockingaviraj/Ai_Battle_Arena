from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def build_index(chunks):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(chunks)
    return (vectorizer, vectors)

def search(index, chunks, query, top_k=2):
    vectorizer, vectors = index
    q_vec = vectorizer.transform([query])
    scores = (vectors @ q_vec.T).toarray().ravel()
    top_ids = scores.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_ids]
