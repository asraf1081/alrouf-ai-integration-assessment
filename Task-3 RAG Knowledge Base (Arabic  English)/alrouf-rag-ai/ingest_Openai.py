import os
import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

def create_knowledge_base():
    print("--- Starting AI Knowledge Ingestion ---")
    
    # 1. Load the data (ADDED UTF-8 ENCODING HERE!)
    loader = DirectoryLoader(
        './data', 
        glob="**/*.txt", 
        loader_cls=TextLoader, 
        loader_kwargs={'encoding': 'utf-8'}
    )
    documents = loader.load()
    
    # Safety Check: Did we actually find any files?
    if len(documents) == 0:
        print("ERROR: No .txt files found in the './data' folder!")
        print("Please make sure 'company_policy.txt' is inside the 'data' folder.")
        sys.exit(1)
        
    print(f"Success: Found {len(documents)} document(s).")
    
    # 2. Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    print(f"Split documents into {len(docs)} chunk(s).")
    
    # 3. Create the Vector Store
    print("Connecting to OpenAI to generate embeddings...")
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    
    # 4. Save it locally
    db.save_local("faiss_alrouf")
    print("Success: Knowledge base 'faiss_alrouf' created!")

if __name__ == "__main__":
    create_knowledge_base()