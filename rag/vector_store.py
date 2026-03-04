import faiss
import numpy as np
import pickle
import os


class VectorStore:
    def __init__(self, embedding_dim, storage_path="storage"):
        self.embedding_dim = embedding_dim
        self.storage_path = storage_path

        os.makedirs(self.storage_path, exist_ok=True)

        self.index_path = os.path.join(self.storage_path, "index.faiss")
        self.meta_path = os.path.join(self.storage_path, "metadata.pkl")

        self.index = None
        self.texts = []

    def create_index(self):
        self.index = faiss.IndexFlatL2(self.embedding_dim)

    def add(self, embeddings, texts):
        if self.index is None:
            self.create_index()

        self.index.add(np.array(embeddings))
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(
            np.array(query_embedding).reshape(1, -1), top_k
        )

        results = []

        for i, idx in enumerate(indices[0]):
           if idx < len(self.texts):
               results.append({
                   "text": self.texts[idx],
                   "distance": float(distances[0][i])
               })

        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.texts, f)

    def load(self):
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, "rb") as f:
                self.texts = pickle.load(f)
            return True
        return False