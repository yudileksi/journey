from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

@app.get("/")
def home():
    return {"message": "AI API is running"}

@app.post("/ask")
def ask_ai(request: Question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": request.question}
        ]
    )
    answer = response.choices[0].message.content
    return Answer(answer=answer)