from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

passed = RunnablePassthrough()

prompt1 =PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

chain1 = RunnableSequence(prompt1, model, parser)

chain2 = RunnableBranch(
    (lambda x: len(x.split())>200 ,RunnableSequence(prompt2,model, parser)),
    passed
)

chain = RunnableSequence(chain1, chain2)

result = chain.invoke({'topic':'Russia vs Ukrain'})

print(result)