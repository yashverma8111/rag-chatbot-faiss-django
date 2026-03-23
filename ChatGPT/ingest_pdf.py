import faiss
import pickle
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import os

os.makedirs("ChatGPT/vector_db", exist_ok=True)

pdf_path = "ChatGPT/documents/knowledge.pdf"

reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    text += page.extract_text()

# Chunking
chunks = []
chunk_size = 500

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(index, "ChatGPT/vector_db/index.faiss")

with open("ChatGPT/vector_db/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("PDF ingestion completed")