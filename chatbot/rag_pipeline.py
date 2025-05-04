import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

qa_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
llm = HuggingFacePipeline(pipeline=qa_pipeline)

def load_vectorstore():
    return FAISS.load_local("models/vectorstore", embeddings=embedding)

def run_query(query, vectorstore):
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa.run(query)

