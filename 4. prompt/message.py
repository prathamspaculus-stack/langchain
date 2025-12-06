from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

messages = [
    SystemMessage(content="you are helpful assistant"),
    HumanMessage(content='tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(result.content))

print(messages)