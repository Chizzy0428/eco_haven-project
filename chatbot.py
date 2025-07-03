import streamlit as st
import json
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter




openai_api_key = st.secrets["openai_api_key"]
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.2)



def load_data():
    docs = []

    loader = TextLoader("store_data/about_us.md")
    docs += loader.load()

    with open("store_data/products.json", "r") as f:
        data = json.load(f)
        for item in data["products"]:
            content = f"{item['name']}: {item['description']} - Price: {item['price']}"
            docs.append(Document(page_content=content))

    return docs

def build_vectorstore():
    docs = load_data()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    return FAISS.from_documents(splits, embeddings)

db = build_vectorstore()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

def ask_bot(question):
    return qa.run(question)
