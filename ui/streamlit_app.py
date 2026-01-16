import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📄 Document Q&A (RAG System)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file}
    res = requests.post(f"{API_URL}/upload", files=files)
    st.success(res.json()["message"])

question = st.text_input("Ask a question from the document")

if st.button("Get Answer"):
    res = requests.post(
        f"{API_URL}/query",
        params={"question": question}
    )
    data = res.json()
    st.write("### Answer")
    st.write(data["answer"])
