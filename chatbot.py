
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader, JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

llm = ChatOpenAI(temperature=0.2)
embeddings = OpenAIEmbeddings()

def load_data():
    docs = []
    loader = TextLoader("store_data/about_us.md")
    docs += loader.load()
    loader = JSONLoader("store_data/products.json", jq_schema=".products", text_content=False)
    docs += loader.load()
    return docs

def build_vectorstore():
    docs = load_data()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    return FAISS.from_documents(splits, embeddings)

db = build_vectorstore()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

def ask_bot(question):
    return qa.run(question)