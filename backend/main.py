from fastapi import FastAPI, UploadFile, File
import os
import shutil

from backend.pdf_utils import extract_text_from_pdf
from backend.vector_store import add_embeddings, search
from backend.database import SessionLocal, DocumentChunk
from backend.rag import generate_answer
from backend.text_utils import chunk_text
# from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("data/uploads", exist_ok=True)
    file_path = f"data/uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)

    add_embeddings(chunks)

    db = SessionLocal()
    for i in range(len(chunks)):
        db.add(DocumentChunk(filename=file.filename, chunk_id=i))
    db.commit()
    db.close()

    return {"message": "File uploaded and indexed"}

@app.post("/query")
def query_doc(question: str):
    context = search(question)
    answer = generate_answer(question, context)
    return {
        "question": question,
        "answer": answer,
        "context": context
    }
