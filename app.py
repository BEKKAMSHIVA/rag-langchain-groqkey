import os    # Access environment variables like API keys
from langchain_community.document_loaders import PyPDFLoader # Load and read PDF file page by page
from langchain_text_splitters import RecursiveCharacterTextSplitter # Split PDF text into smaller chunks
from langchain_huggingface import HuggingFaceEmbeddings  # Convert text chunks into vector embeddings
from langchain_groq import ChatGroq  # Use Groq's fast LLM to generate answers
from langchain_community.vectorstores import FAISS  # Store and search embeddings locally
from langchain_core.prompts import ChatPromptTemplate # Create custom prompt template for LLM
from langchain_core.runnables import RunnablePassthrough  # Pass user query through chain as-is
from langchain_classic.chains import RetrievalQA  # Combine retriever + LLM into one QA chain
from dotenv import load_dotenv  # Load GROQ_API_KEY from .env file

load_dotenv()  # Load environment variables from .env file, including GROQ_API_KEY

# 1. Load the document
loader = PyPDFLoader('mydocument.pdf')  # Fixed: PyPDFLoader for PDF files
documents = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# 3. Convert to embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Store in vector database
vector_db = FAISS.from_documents(chunks, embeddings)

# 5. Create retriever
retriever = vector_db.as_retriever()        

# 6. Create the LLM
llm = ChatGroq(temperature=0, model_name='llama-3.3-70b-versatile')  # Fixed: 'temperatue' → 'temperature'

# 7. RAG Chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 8. Ask a question
if __name__ == "__main__":
    while True:
        query = input("Ask something (type 'exit' to quit): ")
        if query == "exit":
            break

        print("\nChecking Retrieved context ...\n")
        docs = retriever.invoke(query)

        for i, doc in enumerate(docs):
            print(f"\nContext {i+1}:\n", doc.page_content)

        print("\nFinal Answer:")
        response = qa.invoke({'query': query})
        print(response["result"])













