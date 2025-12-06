from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm= ChatGroq(model = "llama-3.1-8b-instant", temperature=1.5, max_tokens=50)

result = llm.invoke("suggest me 5 indian batsman name")

print(result.content)