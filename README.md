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



## 🖼️ Application Preview
<img width="1914" height="1013" alt="Screenshot 2026-03-06 095851" src="https://github.com/user-attachments/assets/f4a59cfa-9fd4-43f6-be63-e1212229b363" />

<img width="1915" height="1016" alt="Screenshot 2026-03-06 095907" src="https://github.com/user-attachments/assets/850a3617-f3b5-4af6-a93c-92a171874e25" />

<img width="1919" height="1017" alt="Screenshot 2026-03-06 095919" src="https://github.com/user-attachments/assets/e1c5bf17-d9cf-434c-b752-adcea7e1df5d" />

<img width="1906" height="1023" alt="Screenshot 2026-03-06 095836" src="https://github.com/user-attachments/assets/4282c20b-134b-4d57-901f-8b6e880a0f2b" />


---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/Devik20/ai-research-assistant.git
cd ai-research-assistant
pip install -r requirements.txt
streamlit run app.py
