import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. Load the Local Embeddings and FAISS DB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
db = FAISS.load_local("faiss_alrouf", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 2})

# 2. Setup the Free Groq LLM
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# 3. Create the Strict AI Prompt
template = """You are a helpful assistant for Alrouf Lighting.
Use ONLY the following pieces of retrieved context to answer the question.
If the answer is not in the context, exactly say: 'I'm sorry, I don't have information on that in my knowledge base.'
Do not make up any information. Answer in the same language as the user's question.

Context: {context}

Question: {question}"""
prompt = ChatPromptTemplate.from_template(template)

def ask_question(query):
    print("\nSearching knowledge base...")
    try:
        # Step A: Retrieve the documents manually (bypassing the broken chains module)
        docs = retriever.invoke(query)
        context_text = "\n\n".join([doc.page_content for doc in docs])
        
        # Step B: Ask the AI
        chain = prompt | llm | StrOutputParser()
        answer = chain.invoke({"context": context_text, "question": query})
        
        print(f"\nAI: {answer}")
        
        # Step C: Print the Citations
        sources = set([doc.metadata.get('source', 'Unknown') for doc in docs])
        if sources:
            print(f"Sources Cited: {', '.join(sources)}")
            
    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure your GROQ_API_KEY is in your .env file!")

if __name__ == "__main__":
    print("--- Alrouf AI Knowledge Base (Modern LCEL Pipeline) ---")
    while True:
        q = input("\nAsk a question (or type 'quit'): ")
        if q.lower() in ['quit', 'exit']: break
        ask_question(q)