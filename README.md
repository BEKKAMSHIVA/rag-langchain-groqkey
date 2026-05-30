# 📄 RAG Chatbot — LangChain + Groq + FAISS

A simple RAG chatbot that answers questions from your PDF using LangChain, Groq LLM, and FAISS.

---

## 🛠️ Installation

1. Clone the repo
   git clone https://github.com/BEKKAMSHIVA/rag-langchain-groqkey.git
   cd rag-langchain-groqkey

2. Create virtual environment
   python -m venv venv
   .\venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

---

## 🔑 Setup .env file

Create a .env file in the project folder and add:

   GROQ_API_KEY=your_groq_api_key_here

To get your Groq API key:
- Go to https://console.groq.com
- Sign up and click API Keys → Create API Key
- Paste it in your .env file

⚠️ Never push your .env file to GitHub!

---

## ▶️ Run

Chat UI:
   python ui.py

Command Line:
   python app.py

---

## 📦 Tech Stack

- LangChain — RAG pipeline
- Groq — Fast LLM (LLaMA)
- FAISS — Vector store
- HuggingFace — Text embeddings
- Gradio — Chat UI
- PyPDF — PDF loader



## 🎨 Gradio UI

This project uses **Gradio** to provide a simple and clean chat interface in the browser.

### What is Gradio?
- Gradio is a Python library that lets you build web UIs with just a few lines of code
- No HTML, CSS, or JavaScript knowledge needed
- Automatically opens in your browser at http://localhost:7860

### How it works here?
- You type your question in the chat box
- It sends the question to the RAG chain (app.py)
- The answer is fetched from your PDF and displayed in the chat
- You can ask multiple questions in the same session

### Why Gradio?
- Super simple to set up
- Built-in chat interface with history
- No frontend coding required
- Perfect for AI and ML projects
