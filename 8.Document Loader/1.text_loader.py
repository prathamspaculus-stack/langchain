from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

loader = TextLoader("cricket.txt", encoding = 'utf-8')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

docs = loader.load()

# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})

print(result)