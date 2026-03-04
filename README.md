# 🧠 AI Research Paper Reviewer (RAG-Based System)

A Retrieval-Augmented Generation (RAG) based AI system that evaluates research papers using semantic search and LLM reasoning.

---

## 🚀 Live Demo
👉 https://ai-research-assistant-mk4skak4eqy9so3pqfeukr.streamlit.app/ 

## 💻 GitHub Repository
👉 https://github.com/Devik20/ai-research-assistant

---

## 📌 Features

- 📄 Research paper evaluation
- 🔍 Semantic search using FAISS
- 🧠 LLM-powered reasoning via Groq
- 📊 Structured scoring system
- 🗂 Metadata extraction
- 🌐 Public deployment using Streamlit Cloud

---

## 🏗️ Architecture Overview

User Input  
⬇  
Text Processing  
⬇  
Sentence Embeddings (Sentence Transformers)  
⬇  
Vector Storage (FAISS)  
⬇  
Retriever  
⬇  
Groq LLM  
⬇  
Evaluation + Scoring Output  

---

## ⚙️ Tech Stack

- Python
- Streamlit
- FAISS
- LangChain
- Sentence Transformers
- Groq API
- PyPDF
- NumPy
- Torch

---

## 🧠 How It Works (RAG Explained)

This project uses a Retrieval-Augmented Generation (RAG) pipeline:

1. The research paper text is converted into embeddings.
2. Embeddings are stored in FAISS vector database.
3. Relevant context is retrieved.
4. The retrieved content is passed to a Large Language Model (LLM).
5. The model generates structured evaluation and scoring.

This improves contextual accuracy compared to direct prompting.

---

## 🖼️ Application Preview

(Add screenshot here)

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/Devik20/ai-research-assistant.git
cd ai-research-assistant
pip install -r requirements.txt
streamlit run app.py
