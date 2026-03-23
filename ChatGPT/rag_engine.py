import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("all-MiniLM-L6-v2")
# model = SentenceTransformer("models/all-MiniLM-L6-v2")
model = SentenceTransformer("/app/models/all-MiniLM-L6-v2")

index = faiss.read_index("ChatGPT/vector_db/index.faiss")

with open("ChatGPT/vector_db/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k
    )

    results = [chunks[i] for i in indices[0]]

    return "\n".join(results)


# import numpy as np
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# model = SentenceTransformer("all-MiniLM-L6-v2")

# documents = [...]  # your document chunks
# doc_embeddings = model.encode(documents)

# SIMILARITY_THRESHOLD = 0.45


# def retrieve_context(question):

#     query_embedding = model.encode([question])

#     scores = cosine_similarity(query_embedding, doc_embeddings)[0]

#     best_index = np.argmax(scores)
#     best_score = scores[best_index]

#     if best_score < SIMILARITY_THRESHOLD:
#         return ""   # no relevant context

#     return documents[best_index]