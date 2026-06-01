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
def get_weather(city: str) -> str:      # str = type hints (just a label), tells that city must be string
    """Get the current weather for a city"""
    weather_data = {
        "Malang": {"temp": 28, "condition": "rainy"},
        "Bali": {"temp": 32, "condition": "sunny"},
        "Jakarta": {"temp": 30, "condition": "cloudy"}
    }
    return json.dumps(weather_data.get(city, {"error": "city not found"}))

@tool
def get_population(city: str) -> str:   # -> str = tells that "this function will return a string"
    """Get the current population for a city"""
    population_data = {
        "Malang": 10000,
        "Bali": 20000,
        "Jakarta": 50000
    }
    return json.dumps(population_data.get(city, {"error": "city not found"}))

@tool
def get_travel_time(origin: str, destination: str) -> str:
    """Get the travel time"""
    travel_time_data = {
        ("Malang", "Bali"): "9 h, 16 m",
        ("Malang", "Jakarta"): "10 h, 42 m",
        ("Bali", "Malang"): "9 h, 16 m",
        ("Bali", "Jakarta"): "18 h, 24 m",
        ("Jakarta", "Malang"): "10 h, 42 m",
        ("Jakarta", "Bali"): "18 h, 24 m"
    }
    return json.dumps(travel_time_data.get((origin, destination), {"error": "city not found"}))

@tool
def get_hotel_price(city: str) -> str:
    """Get the current hotel price for a city"""
    hotel_price_data = {
        "Malang": "Rp 300.000",
        "Bali": "Rp 1.000.000",
        "Jakarta": "Rp 500.000"
    }
    return json.dumps(hotel_price_data.get(city, {"error": "city not found"}))

# TOOLS
tools = [get_weather, get_population, get_travel_time, get_hotel_price]

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
config = {"configurable": {"thread_id": "2"}}

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