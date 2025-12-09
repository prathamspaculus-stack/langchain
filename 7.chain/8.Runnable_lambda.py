from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

passed = RunnablePassthrough()

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())

chain1 = RunnableSequence(prompt,model, parser)

chain2 = RunnableParallel({
    'pass':RunnablePassthrough(),
    'lambda': RunnableLambda(word_count)
})

chain = RunnableSequence(chain1, chain2)

result = chain.invoke({'topic':'AI'})

print(result)