from groq import Groq
from dotenv import load_dotenv
import os
import warnings

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

warnings.filterwarnings("ignore")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PDF_PATH = "AI_Engineering_Guidebook.pdf"
PERSIST_DIR = "chroma_db"   #Customize folder name for saved vectors

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"       # STANDARD embedding model
)

if os.path.exists(PERSIST_DIR):
    print("Loading existing vectorstore...")
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedding_model
    )
else:
    print("Creating new vectorstore...")
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50            # Both CUSTOMIZE - overlap 10% of size
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

def ask(question):
    # Retrieve relevant chunks
    relevant_chunks = retriever.invoke(question)

    # Format chunks into context string
    context = "\n\n".join([
        f"Page {chunk.metadata['page']}:\n{chunk.page_content}"
        for chunk in relevant_chunks
    ])

    # Build prompt
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

    # Send to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer

# STANDARD FORMULA - Conversation Loop
print("\n=== Chat with your PDF ===")
print("Type 'quit to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("GoodBye.")
        break

    answer = ask(user_input)
    print(f"\nAssistant: {answer}\n")