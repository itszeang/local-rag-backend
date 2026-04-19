from vector_database import load_existing_database
import ollama
import json

def ask_question(query):
    print(f"\n[SYSTEM] Query: '{query}'")
    print("[SYSTEM] Searching in the vector database...")
    
    # 1. RETRIEVAL
    db = load_existing_database()
    results_and_scores = db.similarity_search_with_score(query, k=3)
    
    context = "\n\n".join([
        f"[Chunk {i+1}]: {doc.page_content}"
        for i, (doc, score) in enumerate(results_and_scores)
    ])
    
    print("[SYSTEM] Sending retrieved chunks to Ollama...\n")
    
    # 2. GENERATION
    prompt = f'''Based on the following context from documents, answer the question concisely.

Context:
{context}

Question: {query}

Answer (be concise and specific):'''

    try:
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = response['message']['content']
        
        # 3. FORMAT RESPONSE
        response_data = {
            "query": query,
            "answer": answer,
            "sources": [
                {
                    "chunk_id": i+1,
                    "text": doc.page_content[:200] + "...",
                    "relevance_score": round(score, 3)
                }
                for i, (doc, score) in enumerate(results_and_scores)
            ],
            "metadata": {
                "model": "llama3.2",
                "chunks_retrieved": len(results_and_scores),
                "chunks_used": 3
            }
        }
        
        print(json.dumps(response_data, indent=4, ensure_ascii=False))
        
    except Exception as e:
        print("\n[ERROR]: Failed to connect to Ollama.")
        print(f"Error Details: {e}")

if __name__ == '__main__':
    my_query = "What is the purpose of Daily Scrum?"
    ask_question(my_query)
