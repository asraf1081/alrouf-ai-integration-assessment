import os
import sys
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

def create_knowledge_base():
    print("--- Starting RAG Ingestion (Free Local Embeddings) ---")
    
    # 1. Load the 3 text files you created
    loader = DirectoryLoader('./data', glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    documents = loader.load()
    
    if len(documents) == 0:
        print("ERROR: No .txt files found in './data'")
        sys.exit(1)
        
    print(f"Success: Found {len(documents)} document(s).")
    
    # 2. Chunking
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    print(f"Split documents into {len(docs)} chunk(s).")
    
    # 3. Embed & Index (Using a Free Multilingual Model)
    print("Downloading/Loading Local AI Model (this takes a moment the first time)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    
    db = FAISS.from_documents(docs, embeddings)
    
    # 4. Save
    db.save_local("faiss_alrouf")
    print("Success: Knowledge base 'faiss_alrouf' created locally for $0.00!")

if __name__ == "__main__":
    create_knowledge_base()