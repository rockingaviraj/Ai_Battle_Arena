from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os, sys
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pdf_reader import read_pdf
from text_splitter import split_text
from vector_store import build_index, search
from qa_logic import generate_answer

app = FastAPI()

class InputData(BaseModel):
    pdf_url: str
    questions: list

@app.post("/aibattle")
def aibattle(data: InputData):

    if not data.questions:
        return {"answers": []}

    # Download PDF
    try:
        response = requests.get(data.pdf_url, timeout=10)
        response.raise_for_status()
    except Exception:
        return {"answers": [""] * len(data.questions)}

    # Save PDF
    pdf_path = os.path.join(tempfile.gettempdir(), "doc.pdf")
    try:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
    except Exception:
        return {"answers": [""] * len(data.questions)}

    # Read PDF
    try:
        text = read_pdf(pdf_path)
    except Exception:
        return {"answers": [""] * len(data.questions)}

    if not text.strip():
        return {"answers": [""] * len(data.questions)}

    # Split text
    chunks = split_text(text)

    # Build index
    vectors = build_index(chunks)

    answers = []

    for q in data.questions:
        try:
            context_chunks = search(vectors, chunks, q, top_k=2)
            context = " ".join(context_chunks)
            ans = generate_answer(q, context)
            answers.append(ans)
        except Exception:
            answers.append("")

    return {"answers": answers}
