from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from typing import TypedDict

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

class review(TypedDict):

    summary: str
    sentimate: str

structured_model = model.with_structured_output(review)

result = structured_model.invoke(""" 
the hardware is greate, but the software feels bloted. there are so many pre-install appps that i cant remove. also, the UI looks outdated compared to another brand. Hoping software updated to fix this.
                      """)

print(result)


# this is use for openai model.