from vektor_veritabani import mevcut_veritabanini_yukle

def soru_sor(soru):
    print(f"\nSoru: '{soru}'")
    print("Veritabaninda araniyor (Vektorel Uzayda)...\n")
    
    # Diskteki chroma_db klasorunu yukluyoruz
    db = mevcut_veritabanini_yukle()
    
    # Soruyla anlamsal olarak en cok eslesen (k=3) parcayi getir
    sonuclar = db.similarity_search(soru, k=3)
    
    print("--- BULUNAN EN ALAKALI 3 PARCA ---")
    for i, sonuc in enumerate(sonuclar):
        print(f"\n[{i+1}. Parca]:")
        print(sonuc.page_content)
        print("-" * 50)

if __name__ == '__main__':
    # PDF icinde arayacagimiz soru
    sorum = "What is the purpose of Daily Scrum?"
    soru_sor(sorum)
