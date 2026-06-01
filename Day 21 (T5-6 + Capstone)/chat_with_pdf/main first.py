import os
from groq import Groq
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#LOAD PDF
PDF_PATH = "AI_Engineering_Guidebook.pdf"

loader = PyPDFLoader(PDF_PATH)
pages = loader.load()

#SPLIT into CHUNKS
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50            # Both CUSTOMIZE - overlap 10% of size
)
chunks = splitter.split_documents(pages)

#print(f"Total chunks: {len(chunks)}")
#print(f"\nFirst chunk: {chunks[0].page_content}")
#print(f"\nMetadata: {chunks[0].metadata}")

#EMBED & STORE in Chroma
PERSIST_DIR = "chroma_db"   #Customize folder name for saved vectors

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"       # STANDARD embedding model
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=PERSIST_DIR
)

print(f"Vectorstore created. Total vectors: {vectorstore._collection.count()}")