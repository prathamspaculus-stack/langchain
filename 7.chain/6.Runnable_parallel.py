from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

template1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Generate a linkid post {topic}',
    input_variables=['topic']
)

chain = RunnableParallel({
    'Tweet': RunnableSequence(template1,model,parser),
    'post':RunnableSequence(template2,model,parser)
})

result = chain.invoke({'topic':'Ai'})

print(result)