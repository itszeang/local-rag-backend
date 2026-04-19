from vektor_veritabani import mevcut_veritabanini_yukle
import ollama
import json

def soru_sor(soru):
    print(f"\n[SİSTEM] Soru: '{soru}'")
    print("[SİSTEM] Veritabaninda araniyor (Vektorel Uzayda)...")
    
    # 1. RETRIEVAL (Geri Getirme)
    db = mevcut_veritabanini_yukle()
    # Sadece metni degil, metnin soruya olan uzakligini (skorunu) da getiriyoruz
    sonuclar_ve_puanlar = db.similarity_search_with_score(soru, k=3)
    
    # Chunk'lari birlestir
    context = "\n\n".join([
        f"[Chunk {i+1}]: {doc.page_content}"
        for i, (doc, score) in enumerate(sonuclar_ve_puanlar)
    ])
    
    print("[SİSTEM] Bulunan metinler Ollama'ya gonderiliyor...\n")
    
    # 2. GENERATION (Uretim)
    prompt = f'''Based on the following context from documents, answer the question concisely.

Context:
{context}

Question: {soru}

Answer (be concise and specific):'''

    try:
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = response['message']['content']
        
        # 3. FORMAT RESPONSE (Attigin koddaki gibi iyilestirilmis format)
        response_data = {
            "query": soru,
            "answer": answer,
            "sources": [
                {
                    "chunk_id": i+1,
                    "text": doc.page_content[:200] + "...",
                    "relevance_score": round(score, 3)
                }
                for i, (doc, score) in enumerate(sonuclar_ve_puanlar)
            ],
            "metadata": {
                "model": "llama3.2",
                "chunks_retrieved": len(sonuclar_ve_puanlar),
                "chunks_used": 3
            }
        }
        
        # Ciktiyi guzel gozuken bir JSON formatinda ekrana basiyoruz
        print(json.dumps(response_data, indent=4, ensure_ascii=False))
        
    except Exception as e:
        print("\n[HATA]: Ollama'ya baglanilamadi.")
        print(f"Hata Detayi: {e}")

if __name__ == '__main__':
    sorum = "What is the purpose of Daily Scrum?"
    soru_sor(sorum)
