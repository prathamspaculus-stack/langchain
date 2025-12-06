from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

llm= ChatGroq(model = "llama-3.1-8b-instant")
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# result = llm.invoke("suggest me 5 indian batsman name")
# print(result.content)
query_vector = embeddings.embed_query("suggest me 5 indian batsman name")
print(query_vector)



