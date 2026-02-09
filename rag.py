import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

class SchemaRAG:
    def __init__(self, documents):
        self.documents = documents
        self.embeddings = model.encode(documents)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, k=2):
        query_embedding = model.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding), k
        )
        return [self.documents[i] for i in indices[0]]