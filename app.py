import streamlit as st
from chatbot.rag_pipeline import load_vectorstore, run_query
from docs.embedding_utils import ingest_docs

st.set_page_config(page_title="AI FAQ Chatbot", layout="wide")
st.title("🤖 AI-Powered FAQ Chatbot")

uploaded_file = st.file_uploader("Upload a PDF with company FAQs", type=["pdf"])

if uploaded_file:
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    st.success("PDF uploaded successfully!")
    ingest_docs(f"data/{uploaded_file.name}")
    st.success("Document ingested and vectorstore created.")

query = st.text_input("Ask a question based on your FAQ:")

if query:
    vs = load_vectorstore()
    response = run_query(query, vs)
    st.markdown(f"**Answer:** {response}")
