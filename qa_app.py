import os
import requests
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

# Load environment variables
load_dotenv(find_dotenv(), override=True)
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face Inference API URL
HF_API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"

def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    return response.json()

# Function to load documents
def load_document(file):
    name, extension = os.path.splitext(file)
    if extension == ".pdf":
        loader = PyPDFLoader(file)
    elif extension == ".docx":
        loader = Docx2txtLoader(file)
    elif extension == ".txt":
        loader = TextLoader(file)
    else:
        print("Unsupported document format.")
        return None
    return loader.load()

# Function to chunk data
def chunk_data(data, chunk_size=256, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(data)

# Function to create embeddings (Stubbed, using Chroma without real embeddings)
def create_embedding(chunks):
    vector_store = Chroma.from_documents(chunks, embedding_function=lambda x: x)  # Placeholder function
    return vector_store

# Function to ask questions and get answers
def ask_and_get_answer(text, question):
    prompt = f"Answer the question based on the following document:\n\n{text}\n\nQuestion: {question}"
    response = query_huggingface_api(prompt)
    return response["generated_text"] if response else "No answer generated."

if __name__ == "__main__":
    file_path = input("Enter the path of the file to process: ")
    data = load_document(file_path)
    
    if data:
        chunks = chunk_data(data)
        print(f"Chunk size: {len(chunks)}")
        
        vector_store = create_embedding(chunks)
        
        # Concatenate text from chunks for Hugging Face Processing
        full_text = "\n".join([chunk.page_content for chunk in chunks])

        while True:
            question = input("\nAsk anything about the content of your file (type 'exit' to quit): ")
            if question.lower() == "exit":
                break
            answer = ask_and_get_answer(full_text, question)
            print(f"Answer: {answer}")
