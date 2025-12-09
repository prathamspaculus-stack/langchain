from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

template1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="explain the following joke- {text}",
    input_variables=['text']
)

chain = RunnableSequence(template1, model, parser, template2, model, parser)

result = chain.invoke({'topic':'AI'})

print(result)