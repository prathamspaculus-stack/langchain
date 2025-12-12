from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
import requests

load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Search tool
search_tool = DuckDuckGoSearchRun()

# Weather tool
@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather data for a city.
    """
    url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'
    return requests.get(url).json()

# Create agent (NO prompt argument!)
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data]
)

# ⭐ Correct way: use messages[]
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find the capital of Madhya Pradesh, then get its current weather."
        }
    ]
})

print(response)
print("\nFINAL OUTPUT:", response["messages"][-1]["content"])
