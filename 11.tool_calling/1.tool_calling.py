from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")


# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# print(multiply.invoke({'a':3, 'b':4}))
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

model.invoke('hi')

llm_with_tools = model.bind_tools([multiply])

# result = llm_with_tools.invoke("hi how are you")
# print(result)

query = HumanMessage('can you multiply 3 with 1000')

messages = [query]

result = llm_with_tools.invoke(messages)
# print(result.tool_calls[0])

result2 = multiply.invoke(result.tool_calls[0])
print(result2)

