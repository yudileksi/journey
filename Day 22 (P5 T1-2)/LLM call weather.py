import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define the actual function
def get_weather(city):
    weather_data = {
        "Malang": {"temp": 28, "condition": "rainy"},
        "Bali": {"temp": 32, "condition": "sunny"},
        "Jakarta": {"temp": 30, "condition": "cloudy"}
    }
    return json.dumps(weather_data.get(city, {"error": "city not found"}))

# Describe the tool to LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# First LLM call
messages = [{"role": "user", "content": "Should i bring an umbrella to Jakarta tomorrow?"}]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

response_message = response.choices[0].message

# Handle tool call
if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    if function_name == "get_weather":
        result = get_weather(**function_args)

        messages.append(response_message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

    #Second LLM call
    final_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
    )

    print(final_response.choices[0].message.content)

else:
    print(response_message.content)