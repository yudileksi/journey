import os
from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# PROMPT
@tool
def get_weather(city):
    """Get the current weather for a city"""
    weather_data = {
        "Malang": {"temp": 28, "condition": "rainy"},
        "Bali": {"temp": 32, "condition": "sunny"},
        "Jakarta": {"temp": 30, "condition": "cloudy"}
    }
    return json.dumps(weather_data.get(city, {"error": "city not found"}))

@tool
def get_population(city):
    """Get the current population for a city"""
    population_data = {
        "Malang": 10000,
        "Bali": 20000,
        "Jakarta": 50000
    }
    return json.dumps(population_data.get(city, {"error": "city not found"}))

# TOOLS
tools = [get_weather, get_population]

# Add Memory
memory = MemorySaver()

# AGENT
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a bad and rude assistant but give factual data with memory of our conversation.",
    checkpointer=memory
)

# Formula for conversation loop with memory
config = {"configurable": {"thread_id": "1"}}

print("=== Agent with Memory ===")
print("Type 'quit' to exit\n")

# INVOKE
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye")
        break

    result = agent.invoke(
        {"messages": [("user", user_input)]},
        config=config
    )

    print(f"Agent: {result['messages'][-1].content}\n") # means "Give me the content of the last message [-1]"