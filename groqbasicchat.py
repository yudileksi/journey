from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_hisory = [{
    "role": "system", 
    "content": "You are a helpful assistant"
}]

def chat(user_messsage):
    conversation_hisory.append({
        "role": "user", 
        "content": user_messsage
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=conversation_hisory, 
        max_tokens=100
    )
    
    ai_response = response.choices[0].message.content
    
    conversation_hisory.append({
        "role": "assistant", 
        "content": ai_response
    })
    
    return ai_response

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye.")
        break
    response = chat(user_input)
    print(f"AI: {response}\n")