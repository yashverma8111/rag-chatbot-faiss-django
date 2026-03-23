# 🚀 RAG-Based Chatbot (Django + FAISS)

A Retrieval-Augmented Generation (RAG) chatbot that answers queries using a custom knowledge base. Built with Django, FAISS, and Sentence Transformers, and containerized with Docker.

---

## 📌 Features
- RAG-based contextual responses  
- PDF knowledge base ingestion  
- Fast similarity search (FAISS)  
- Semantic embeddings (MiniLM)  
- Dockerized deployment  

---

## 🏗️ Tech Stack
- Django (Backend)  
- FAISS (Vector DB)  
- Sentence Transformers  
- Groq API  
- HTML, CSS, JS  
- Docker  

---

## 🧠 How It Works
1. Split document into chunks  
2. Convert chunks → embeddings  
3. Store in FAISS  
4. Query → embedding  
5. Retrieve top-k chunks  
6. Send context to LLM  
7. Generate grounded response  

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/rag-chatbot-faiss-django.git
cd rag-chatbot-faiss-django

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create .env:
GROQ_API_KEY=your_api_key_here

Run:
python manage.py runserver

Docker:
docker build -t rag-chatbot .
docker run -p 8000:8000 --env-file .env rag-chatbot

Access:
http://localhost:8000
```
---
## Note!
Knowledge base PDF is not included
Add your own in ChatGPT/documents/

---

## Use Cases
- Research Q&A
- Internal knowledge assistant
- Domain-specific chatbot

---

##👨‍💻 Author
Yash Verma
