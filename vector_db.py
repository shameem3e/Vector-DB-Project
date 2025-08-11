# vector_db.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorDatabase:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.documents = []  # Stores (filename, chunk)
        self.index = None
        self.dimension = None

    def build_index(self, docs):
        """Convert docs to vectors and store them in FAISS index."""
        self.documents = docs
        text_chunks = [chunk for _, chunk in docs]  # Only chunks for embedding
        embeddings = self.model.encode(text_chunks)

        self.dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(np.array(embeddings, dtype=np.float32))

    def search(self, query, k=3):
        """Search for most similar docs to the query."""
        if self.index is None:
            raise ValueError("Index not built yet! Call build_index first.")

        query_vector = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_vector, dtype=np.float32), k
        )

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            filename, chunk = self.documents[idx]
            results.append((filename, chunk, dist))
        return results
