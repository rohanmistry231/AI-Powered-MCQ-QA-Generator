import fitz
import time
import requests

def extract_text_from_pdf_in_chunks(pdf_path, chunk_size=5000):
    doc = fitz.open(pdf_path)
    text_chunks = []
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
        if len(text.split()) >= chunk_size:
            text_chunks.append(text)
            text = ""

    if text:
        text_chunks.append(text)

    return text_chunks

import os  
from dotenv import load_dotenv  
import requests  

# Load environment variables from .env file  
load_dotenv()  

def generate_mcqs(text_chunk, num_questions):  
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"  
    
    # Get the API key from environment variables  
    huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")  
    
    if not huggingface_api_key:  
        return "Error: HUGGINGFACE_API_KEY not found in environment variables."  
        
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}  
    
    prompt = (  
        f"Create {num_questions} multiple-choice questions based on the following text:\n\n"  
        f"{text_chunk}\n\n"  
        "Each question should have one correct answer and three incorrect answers."  
    )  
    
    payload = {"inputs": prompt}  
    response = requests.post(API_URL, headers=headers, json=payload)  
    
    if response.status_code == 200:  
        # Assuming the response structure is as you described  
        return response.json()[0]['generated_text']  
    else:  
        return f"Error generating MCQs: {response.text}"

def main(pdf_path, num_questions, chunk_size=5000):
    text_chunks = extract_text_from_pdf_in_chunks(pdf_path, chunk_size)
    print(f"Extracted {len(text_chunks)} chunks of text from PDF.")

    for i, text_chunk in enumerate(text_chunks):
        try:
            print(f"Processing chunk {i+1}/{len(text_chunks)}")
            mcqs = generate_mcqs(text_chunk, num_questions)
            print(f"Generated MCQs for chunk {i+1}:\n{mcqs}\n")
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred while processing chunk {i+1}: {e}")

if __name__ == "__main__":
    pdf_path = "aws.pdf"
    num_questions = int(input("Enter the number of questions to be generated: "))
    chunk_size = 500

    main(pdf_path, num_questions, chunk_size)
