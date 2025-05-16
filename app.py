import streamlit as st
import os
import PyPDF2
from dotenv import load_dotenv, find_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Load Hugging Face Model for Text Generation (lighter model for 4GB GPU)
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", device=0)  # device=0 → use GPU if available

# Extract text from PDF
def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return ""

# Generate MCQs using Hugging Face Model
def generate_mcqs(text_chunk, num_questions):
    prompt = (
        f"Create {num_questions} multiple-choice questions based on the following text:\n\n"
        f"{text_chunk}\n\nEach question should have one correct answer and three incorrect answers."
    )
    try:
        response = generator(prompt, max_length=500, do_sample=True, temperature=0.7)
        return response[0]["generated_text"].strip()
    except Exception as e:
        return f"Error generating MCQs: {e}"

# Generate MCQs for the entire document
def generate_mcqs_main(file, num_questions):
    text = extract_text_from_pdf(file)
    if not text:
        return "Error: Could not extract text from the file."
    
    st.write("✅ Extracted text from PDF.")
    with st.spinner("Generating MCQs..."):
        mcqs = generate_mcqs(text, num_questions)
    
    if mcqs.startswith("Error"):
        st.error(mcqs)
    else:
        st.write("✅ Generated MCQs:")
        st.write(mcqs)

# Main function for Q&A
def qa_main(file):
    text = extract_text_from_pdf(file)
    if not text:
        st.error("Error: Could not extract text from the file.")
        return
    
    st.write('✅ Loaded document successfully.')
    question = st.text_input("Ask anything about the content of your file:")

    if st.button("Get Answer") and question:
        prompt = f"Answer the following question based on the text:\n\n{text}\n\nQuestion: {question}"
        with st.spinner("Fetching answer..."):
            try:
                response = generator(prompt, max_length=300, do_sample=True, temperature=0.7)
                st.write(f'✅ Answer: {response[0]["generated_text"].strip()}')
            except Exception as e:
                st.error(f"Error generating answer: {e}")

# Streamlit UI
st.title("📄 AI-Powered Content Processor")
file = st.file_uploader("📂 Upload a PDF file", type="pdf")
action = st.selectbox("🔍 What would you like to do?", ["Select", "Generate MCQs", "Ask Questions"])

if file and action != "Select":
    if action == "Generate MCQs":
        num_questions = st.number_input("📝 Enter the number of MCQs:", min_value=1, step=1)
        if st.button("Generate MCQs"):
            generate_mcqs_main(file, num_questions)
    
    elif action == "Ask Questions":
        qa_main(file)
