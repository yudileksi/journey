# streamlit run chatwithweb.py
import requests
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Streamlit interface
st.set_page_config(
    page_title="Webpage Chatbot",
    page_icon="🌐"
)

st.title("Chat with any Website")

# Vectorstore setup - same as PDF example but with webpage text instead of PDF text
if "messages" not in st.session_state:
    st.session_state.messages = []

url = st.text_input("Enter a URL to chat with:")

# Get URL input from user
if url:
    try:
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
    except requests.RequestException as e:
        st.error(f"Error fetching webpage: {e}")
        st.stop()

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()      

    # persist_dir = "chroma_db"
    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # We need to split the text into chunks for better embedding and retrieval
    with st.spinner("Processing webpage..."):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_text(text)

        # Create vectorstore from chunks
        vectorstore = Chroma.from_texts(
            texts=chunks,
            embedding=embedding_model,
        )

    # Create retriever to get relevant chunks based on user query
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    def ask(question):
        # Retrieve relevant chunks
        relevant_chunks = retriever.invoke(question)

        # Format chunks into context string
        context = "\n\n".join([doc.page_content for doc in relevant_chunks])

        # Build prompt for Groq
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        
        # Get answer from Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
                    {"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        return answer
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask a question about the webpage...")
if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    with st.chat_message("user"):
        st.write(user_input)
        
    with st.spinner("Getting answer..."):
        answer = ask(user_input)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
    with st.chat_message("assistant"):
        st.write(answer)





