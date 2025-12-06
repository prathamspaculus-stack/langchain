from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

llm= ChatGroq(model = "llama-3.1-8b-instant")
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

Documents = [
    "delhi is a capital of india",
    "kolkata is a capital of westbangal",
    "paris is a capital of france"
]

vectors = embeddings.embed_documents(Documents)
print(vectors)