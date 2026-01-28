import fitz

def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for i, page in enumerate(doc):
        if i == 0:
            continue   # 👈 first page skip
        text += page.get_text()

    return text