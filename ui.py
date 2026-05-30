import gradio as gr
from app import qa

def ask(question, history):
    result = qa.invoke({"query": question})
    return result["result"]

gr.ChatInterface(
    fn=ask,
    title="📄 RAG Assistant",
    description="Ask questions about your PDF document",
    examples=["Summarize the document", "What are the key points?"],
).launch(inbrowser=True)