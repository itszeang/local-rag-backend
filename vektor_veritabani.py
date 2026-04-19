from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Veritabanının kaydedileceği fiziksel klasör adı
VERITABANI_KLASORU = "./chroma_db"

def veritabani_olustur_ve_kaydet(parcalar):
    print("Vektörleştirme (Embedding) modeli yükleniyor...")
    # Ücretsiz, hızlı ve yerel çalışan güçlü bir model seçiyoruz
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print(f"Toplam {len(parcalar)} parça koordinatlara çevrilip veritabanına kaydediliyor (İlk seferde model ineceği için biraz sürebilir)...")
    
    # ChromaDB'ye kaydediyoruz
    db = Chroma.from_documents(
        documents=parcalar, 
        embedding=embeddings, 
        persist_directory=VERITABANI_KLASORU
    )
    
    print("Harika! Tüm metinler vektörlere çevrildi ve veritabanı başarıyla diske kaydedildi.")
    return db

def mevcut_veritabanini_yukle():
    # Zaten var olan veritabanını kullanmak istediğimizde çağıracağımız fonksiyon
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=VERITABANI_KLASORU, embedding_function=embeddings)
    return db
