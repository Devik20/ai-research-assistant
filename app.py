import streamlit as st
import os
from pypdf import PdfReader
from evaluator import run_full_evaluation
from rag.llm import LocalLLM
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

st.set_page_config(page_title="AI Research Reviewer Pro", layout="wide")

st.title("📚 AI Research Paper Reviewer (RAG + Scoring Engine)")

# ==============================
# SESSION STATE
# ==============================

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

@st.cache_resource
def load_embedder():
    return EmbeddingModel()

@st.cache_resource
def load_llm():
    return LocalLLM()

if "embedder" not in st.session_state:
    st.session_state.embedder = load_embedder()

if "llm" not in st.session_state:
    st.session_state.llm = load_llm()

# ==============================
# PDF UPLOAD
# ==============================

uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type="pdf")

if uploaded_file:

    reader = PdfReader(uploaded_file)
    full_text = ""
    first_pages_text = ""

    for i, page in enumerate(reader.pages):
        extracted = page.extract_text()
        if extracted:
            full_text += extracted + "\n"
            if i < 2:
                first_pages_text += extracted + "\n"

    st.success("PDF Loaded Successfully ✅")

    # ==============================
    # METADATA + SCORING
    # ==============================

    with st.spinner("Evaluating Research Paper..."):
        evaluation = run_full_evaluation(full_text, first_pages_text)

    # -------- Metadata --------
    st.subheader("📊 Metadata Extraction")
    st.json(evaluation["metadata"])

    # -------- Scoring --------
    st.subheader("📈 Research Quality Scoring")

    scoring = evaluation["scoring"]

    if isinstance(scoring, dict):

        total = scoring.get("Total Score") or scoring.get("total_score")

        if total is not None:
       
            total = float(total)

            st.markdown(f"## ⭐ Final Research Quality Score: {total} / 10")

        # Visual Score Bar
            st.progress(min(total / 10, 1.0))

        # Interpretation
            if total <= 3:
               st.error("Weak Research Design – Major Improvements Required")
            elif total <= 6:
               st.warning("Moderate Quality – Significant Improvements Recommended")
            elif total <= 8:
               st.info("Strong Academic Quality")
            else:
               st.success("Publication-Ready Research Quality 🔥")

            st.divider()

        st.json(scoring)

    # ==============================
    # BUILD RAG INDEX
    # ==============================

    def chunk_text(text, chunk_size=800, overlap=150):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            if len(chunk) > 100:
                chunks.append(chunk)
            start += chunk_size - overlap
        return chunks

    chunks = chunk_text(full_text)
    chunks = [f"[SOURCE: uploaded_paper]\n{chunk}" for chunk in chunks]

    embeddings = st.session_state.embedder.encode(chunks)

    vector_store = VectorStore(embedding_dim=len(embeddings[0]))
    vector_store.add(embeddings, chunks)

    st.session_state.vector_store = vector_store

    st.success("RAG Index Built Successfully 🔥")

# ==============================
# QUESTION ANSWERING
# ==============================

if st.session_state.vector_store:

    st.subheader("💬 Ask Questions About the Paper")

    user_query = st.text_input("Enter your question")

    if user_query:

        query_embedding = st.session_state.embedder.encode([user_query])[0]

        results = st.session_state.vector_store.search(query_embedding, top_k=5)

        context_chunks = []

        for item in results:
            similarity = 1 / (1 + item["distance"])
            if similarity > 0.30:
                context_chunks.append(item["text"])

        context = "\n\n".join(context_chunks[:4])

        if not context:
            st.warning("Not enough context found.")
        else:
            prompt = f"""
You are a Professional AI Research Reviewer.

STRICT RULES:
- Use ONLY the provided context.
- If something is missing, explicitly say it is not present.

Context:
{context}

Question:
{user_query}

Provide structured, professional answer.
"""

            response = st.session_state.llm.generate(prompt)

            st.subheader("🧠 AI Review Response")
            st.write(response)