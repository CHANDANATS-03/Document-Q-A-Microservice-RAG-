import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
DIM = 384

INDEX_PATH = "data/faiss_index/index.faiss"
META_PATH = "data/faiss_index/meta.pkl"

os.makedirs("data/faiss_index", exist_ok=True)

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    metadata = pickle.load(open(META_PATH, "rb"))
else:
    index = faiss.IndexFlatL2(DIM)
    metadata = []

def add_embeddings(text_chunks):
    embeddings = EMBEDDING_MODEL.encode(text_chunks)
    index.add(embeddings)
    metadata.extend(text_chunks)

    faiss.write_index(index, INDEX_PATH)
    pickle.dump(metadata, open(META_PATH, "wb"))

def search(query, top_k=3):
    query_emb = EMBEDDING_MODEL.encode([query])
    distances, indices = index.search(query_emb, top_k)
    return [metadata[i] for i in indices[0]]
