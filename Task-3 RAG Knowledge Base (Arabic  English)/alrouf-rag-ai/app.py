import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# 1. Immediate Load
load_dotenv()

# Page Config
st.set_page_config(page_title="Alrouf AI", page_icon="⚡", layout="centered")
st.title("⚡ Alrouf Speed-Optimized AI")

# 2. POWER MOVE: Cache Resources (Only loads once per session)
@st.cache_resource
def get_ai_engines():
    # Load local embeddings once
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    # Load Vector DB once
    db = FAISS.load_local("faiss_alrouf", embeddings, allow_dangerous_deserialization=True)
    # Connect to high-speed Groq Llama 3.1
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
    return db.as_retriever(search_kwargs={"k": 2}), llm

retriever, llm = get_ai_engines()

# 3. Static Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant for Alrouf Lighting. 
Answer ONLY based on context. If unknown, say you don't know.
Context: {context}
Question: {question}
""")

# 4. Faster UI Logic
query = st.text_input("How can I help you today?", placeholder="e.g., What is the warranty?")

if query:
    # Use a container for immediate feedback
    with st.chat_message("assistant"):
        # Step A: Instant Local Retrieval
        docs = retriever.invoke(query)
        context_text = "\n\n".join([doc.page_content for doc in docs])
        
        # Step B: Fast Generation
        chain = prompt | llm | StrOutputParser()
        
        # We use st.write_stream or just st.write for rapid delivery
        response = chain.invoke({"context": context_text, "question": query})
        st.write(response)
        
        # Citations at the bottom
        sources = [os.path.basename(doc.metadata.get('source', 'Unknown')) for doc in docs]
        st.caption(f"Sources: {', '.join(set(sources))}")