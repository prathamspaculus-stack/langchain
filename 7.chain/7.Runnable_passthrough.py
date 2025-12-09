from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

passthrough = RunnablePassthrough()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="explain the following joke- {topic}",
    input_variables=['topic']
)

chain1 = RunnableSequence(prompt1, model, parser)

chain2 =RunnableParallel({
    'pass' : passthrough,
    'explain':RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(chain1,chain2)

result = chain.invoke({'topic':'AI'})

print(result)