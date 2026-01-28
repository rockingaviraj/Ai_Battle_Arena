# AI PDF Question Answering System

This project implements a lightweight Question Answering (QA) system that accepts a PDF document and a list of questions, processes the document, and returns answers in a structured JSON format.

The system is designed with simplicity, stability, and performance in mind, focusing on document understanding rather than conversational AI.

---

## 🚀 Features

- Accepts a **PDF URL** as input
- Supports **multiple questions** in a single request
- Extracts and processes text directly from PDFs
- 
- Uses vector-based similarity search to find relevant content
- Returns **clean JSON responses**
- Handles errors gracefully (no crashes)
- Optimized for speed and low memory usage

---

## 🧠 How It Works (High Level)

1. The PDF is downloaded from the provided URL
2. Text is extracted from the document (first page skipped for relevance)
3. Text is split into smaller chunks
4. Chunks are converted into vector representations
5. For each question, the most relevant chunk is selected
6. Answers are generated from the selected context
7. Results are returned as a JSON response

---

## 📥 API Endpoint

### `POST /aibattle`

#### Request Body
```json
{
  "pdf_url": "https://example.com/sample.pdf",
  "questions": [
    "What is this document about?",
    "What is the main contribution?"
  ]
}
Response Body
{
  "answers": [
    "Answer to question 1...",
    "Answer to question 2..."
  ]
}
