from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2" )

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query= "tell me about virat."

docs_embedding = embeddings.embed_documents(documents)
quer_embeding = embeddings.embed_documents(query)

scores = cosine_similarity([quer_embeding],docs_embedding)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x [1])[-1]

print(query)
print(documents[index])
print("similarity score:", score)
