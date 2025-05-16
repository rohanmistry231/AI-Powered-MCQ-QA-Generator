# 🧠 AI-Powered MCQ and Q&A Generator

Welcome to the **AI-Powered MCQ and Q&A Generator**, a cutting-edge tool designed to transform your documents into interactive learning resources! This project leverages advanced natural language processing (NLP) models to generate multiple-choice questions (MCQs) and provide answers to custom questions based on uploaded documents. Whether you're a student, educator, or professional, this tool simplifies studying and content exploration with an intuitive interface and robust functionality.

## 🌟 Features

- **MCQ Generation**: Automatically create multiple-choice questions from PDF documents with one correct answer and three distractors.
- **Question Answering**: Ask any question about the content of your document and receive accurate, context-based answers.
- **Multi-Format Support**: Process PDFs, DOCX, and TXT files (with primary focus on PDFs).
- **Streamlit Web Interface**: A user-friendly UI powered by Streamlit for seamless interaction.
- **Chunked Text Processing**: Efficiently handle large documents by splitting them into manageable chunks.
- **Hugging Face Integration**: Utilize powerful NLP models like `EleutherAI/gpt-neo-1.3B` and `mistralai/Mistral-7B-Instruct-v0.1` for text generation.
- **GPU Acceleration**: Optimized for GPU usage to speed up processing (configurable for lighter models).
- **Vector Store (Chroma)**: Experimental support for document embeddings to enhance question answering (placeholder implementation).

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A Hugging Face API key (set up in a `.env` file)
- GPU (optional, for faster processing)
- Required libraries (listed in `requirements.txt`)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rohanmistry231/AI-Powered-MCQ-QA-Generator.git
   cd AI-Powered-MCQ-QA-Generator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your Hugging Face API key:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

### Running the Application
- **Streamlit App** (`app.py`):
  Launch the web interface:
  ```bash
  streamlit run app.py
  ```
  Open your browser to `http://localhost:8501` and upload a PDF to start generating MCQs or asking questions.

- **Command-Line MCQ Generator** (`mcq_app.py` or `model.py`):
  Run the script to generate MCQs from a PDF:
  ```bash
  python mcq_app.py
  ```
  Enter the path to your PDF and the number of questions when prompted.

- **Command-Line Q&A Tool** (`qa_app.py`):
  Run the script to ask questions about a document:
  ```bash
  python qa_app.py
  ```
  Provide the file path and ask questions interactively.

## 📂 Project Structure
```
ai-mcq-qa-generator/
├── app.py               # Streamlit web app for MCQ and Q&A
├── mcq_app.py           # Command-line MCQ generator
├── qa_app.py            # Command-line Q&A tool
├── model.py             # Core logic for MCQ generation (shared with mcq_app.py)
├── .env                 # Environment variables (API keys)
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🛠️ How It Works
1. **Document Loading**: Upload a PDF (or other supported formats) via the Streamlit UI or command-line scripts.
2. **Text Extraction**: Extract text using `PyPDF2` or `fitz` (PyMuPDF) for PDFs, with support for chunking large documents.
3. **MCQ Generation**:
   - Text is processed in chunks to handle large documents.
   - Hugging Face models generate MCQs with one correct answer and three incorrect options.
4. **Question Answering**:
   - Text is chunked and optionally stored in a Chroma vector store (placeholder embedding).
   - Custom questions are answered using context-aware prompts sent to Hugging Face models.
5. **Output**: Results are displayed in the Streamlit UI or printed to the console.

## 💡 Use Cases
- **Education**: Generate practice quizzes for students from textbooks or lecture notes.
- **Training**: Create assessments for corporate training materials.
- **Self-Study**: Explore and understand complex documents by asking targeted questions.
- **Content Review**: Quickly generate questions to test comprehension of reports or articles.

## 🧪 Future Improvements
- Add support for more document formats (e.g., Markdown, HTML).
- Implement real embeddings for Chroma vector store to improve Q&A accuracy.
- Enhance MCQ formatting for export to formats like JSON or CSV.
- Optimize chunking and model parameters for faster processing.
- Add user authentication and session management for the Streamlit app.

## 🤝 Contributing
We welcome contributions! To get started:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 🙏 Acknowledgments
- [Hugging Face](https://huggingface.co/) for providing powerful NLP models.
- [Streamlit](https://streamlit.io/) for the intuitive web interface framework.
- [PyMuPDF](https://pymupdf.readthedocs.io/) and [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing.
- [LangChain](https://langchain.com/) for document chunking and vector store utilities.

---

**Ready to transform your documents into interactive learning tools?** Dive in and start generating MCQs and answers today! 🚀