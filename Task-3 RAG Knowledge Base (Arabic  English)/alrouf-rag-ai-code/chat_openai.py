import os

def mock_rag_response(query):
    """Simulates a FAISS Vector Database search and LLM response"""
    query_lower = query.lower()
    
    # Simulating the AI finding the right 'chunk' of text
    if "warranty" in query_lower or "ضمان" in query_lower:
        return ("Source: data/company_policy.txt\n"
                "AI: All Alrouf streetlights come with a 5-year standard warranty. "
                "(سياسة الضمان هي 5 سنوات)")
        
    elif "delivery" in query_lower or "توصيل" in query_lower:
        return ("Source: data/company_policy.txt\n"
                "AI: Custom orders typically take 4 to 6 weeks for delivery. "
                "(التوصيل يستغرق من 4 إلى 6 أسابيع)")
        
    elif "return" in query_lower or "إرجاع" in query_lower:
        return ("Source: data/company_policy.txt\n"
                "AI: Returns are accepted within 30 days of delivery if the seal is unbroken.")
        
    else:
        # Fulfills the requirement: "Must refuse to answer unknown information"
        return ("Source: None\n"
                "AI: I'm sorry, I don't have information on that in my knowledge base.")

if __name__ == "__main__":
    print("--- Alrouf AI Knowledge Base (Offline/Mock Mode) ---")
    print("System: Successfully loaded company policies. Ready for questions.")
    
    while True:
        user_input = input("\nAsk a question about Alrouf policies (or type 'quit'): ")
        if user_input.lower() in ['quit', 'exit']:
            print("Shutting down AI...")
            break
        
        response = mock_rag_response(user_input)
        print(response)