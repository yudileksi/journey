# Chat with any Website
# User provides a URL
# Your app scrapes the webpage content
# Builds a RAG pipeline from that content
# User can ask questions about that webpage
# Streamlit interface

from bs4 import BeautifulSoup
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import requests

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
api_key = os.getenv("API_KEY")

st.set_page_config(
    page_title="Webpage Chatbot",
    page_icon="🌐"
)
st.title("Chat with any Website")
url = st.text_input("Enter a URL to chat with: ")
if url:
    response = requests.get(url)
    web_strach = BeautifulSoup(response.text, 'html.parser')
    
    text = web_strach.get_text()

    PERSIST_DIR = "chroma_db"

    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    if os.path.exists(PERSIST_DIR):
        print("Loading existing vectorstore...")
        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embedding_model
        )
    else:
        print("Creating new vectorstore...")
        loader = PyPDFLoader(text)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(pages)

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=PERSIST_DIR
        )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
else:
    st.warning("Please enter a valid URL.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def ask(question):
    relevant_chunks = retriever.invoke(question)

    context = "\n\n".join([
        f"Page {chunk.metadata['page']}:\n{chunk.page_content}"
        for chunk in relevant_chunks
    ])
    
    messages = [
        {
            "role": "system",
            'content': """You are a helpful assistant. 
            Answer ONLY based on the context provided by the user. 
            If the answer is not in the context, say I don't know."""
        },
        {
            "role": "user",
            "content": f"""Context:
{context}

Question:
{question}"""
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer

question = st.text_input("Ask a question about this webpage:", key="question_input")
if st.button("Send") and question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Be patient you frick"):
        answer = ask(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)
        
