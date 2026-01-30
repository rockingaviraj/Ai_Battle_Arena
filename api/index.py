from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os, sys
import numpy as np
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pdf_reader import read_pdf
from text_splitter import split_text
from vector_store import build_index, get_embedder
from qa_logic import generate_answer

PDF_CACHE = {}

app = FastAPI()

class InputData(BaseModel):
    pdf_url: str
    questions: list

@app.post("/aibattle")
def aibattle(data: InputData):

    # 1️⃣ Empty questions
    if not data.questions:
        return {"answers": []}

    # 2️⃣ Download PDF
    try:
        response = requests.get(data.pdf_url, timeout=10)
        response.raise_for_status()
    except Exception:
        return {"answers": [""] * len(data.questions)}

    # 3️⃣ Save PDF (cross-platform)
    pdf_path = os.path.join(tempfile.gettempdir(), "doc.pdf")
    try:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
    except Exception:
        return {"answers": [""] * len(data.questions)}

    # 4️⃣ Read PDF (cached)
    try:
        if data.pdf_url in PDF_CACHE:
            text = PDF_CACHE[data.pdf_url]
        else:
            text = read_pdf(pdf_path)
            PDF_CACHE[data.pdf_url] = text
    except Exception:
        return {"answers": [""] * len(data.questions)}

    if not text.strip():
        return {"answers": [""] * len(data.questions)}

    # 5️⃣ Split text
    chunks = split_text(text)

    # 6️⃣ Build index
    try:
        index = build_index(chunks)
    except Exception:
        return {"answers": [""] * len(data.questions)}

    answers = []
    embedder = get_embedder()

    # 7️⃣ Answer questions
    for q in data.questions:
        try:
            q_vec = embedder.encode([q])
            q_vec = np.array(q_vec).astype("float32")
            _, ids = index.search(q_vec, 1)
            context = chunks[ids[0][0]]
            ans = generate_answer(q, context)
            answers.append(ans)
        except Exception:
            answers.append("")

    return {"answers": answers}
