# 🤖 AI-Powered FAQ Chatbot using RAG

This chatbot uses Retrieval-Augmented Generation to answer user queries based on uploaded company FAQs in PDF format.

## 🔧 Features
- Upload PDF with FAQs
- Embed and index content with FAISS
- Answer queries using HuggingFace LLM

## 🚀 Setup
```bash
pip install -r requirements.txt
mkdir data models
streamlit run app.py
```

## 📂 Structure
```
rag-faq-chatbot/
├── app.py
├── chatbot/
│   └── rag_pipeline.py
├── docs/
│   └── embedding_utils.py
├── data/           # Upload PDFs here
├── models/         # FAISS vectorstore saved here
├── requirements.txt
└── README.md
```

## 🧪 Example PDF
You can use any company FAQ PDF. Or download a sample from:
https://github.com/microsoft/BotBuilder-Samples/blob/main/docs/sample-faq.pdf
