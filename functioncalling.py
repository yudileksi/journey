import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#FIRST LLM CALL
def chat(user_message):
    def get_weather(city):
        weather_data = {"Malang": {"temp": 25, "condition": "cloudy"}, 
                        "Jakarta": {"temp": 30, "condition": "sunny"}, 
                        "Bali": {"temp": 20, "condition": "rain"}
    }
        return json.dumps(weather_data.get(city, {"error": "City not found"}))

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
    
    message = [{
        "role": "user", 
        "content": user_message    
}]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=message, 
        tools=tools, 
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    
#FUNCTION CALLING
    if response_message.tool_calls:
        tool_calls = response_message.tool_calls[0]
        function_name = tool_calls.function.name
        function_args = json.loads(tool_calls.function.arguments)
        
        if function_name == "get_weather":
            result = get_weather(**function_args)
            
            message.append(response_message)
            message.append({
                "role": "tool", 
                "tool_call_id": tool_calls.id, 
                "content": result
            })
            
        #SECOND LLM CALL
        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=message
        )
        
        print(final_response.choices[0].message.content)
        
    else:
        print(response_message.content)

while True:
    print("Type q to quit")
    user_input = input("You: ")
    if user_input.lower() == "q":
        print("Goodbye.")
        break
    response = chat(user_input)