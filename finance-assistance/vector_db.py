from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load Sentence Transformer for Embeddings
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Sample Financial Knowledge Base
financial_docs = [
    "The S&P 500 rose by 2% amid economic recovery.",
    "Bitcoin reached an all-time high of $68,000.",
    "Federal Reserve plans to increase interest rates in 2024.",
]

# Convert Docs to Embeddings
embeddings = embed_model.encode(financial_docs)
embedding_dim = embeddings.shape[1]

# Initialize FAISS Index
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(embeddings))

# Function to Retrieve Context for Chatbot
def retrieve_context(query: str):
    query_embedding = embed_model.encode([query])
    _, indices = index.search(query_embedding, k=1)
    return financial_docs[indices[0][0]]

# Example Usage
query = "What's happening with Bitcoin?"
context = retrieve_context(query)
print("Retrieved Context:", context)
