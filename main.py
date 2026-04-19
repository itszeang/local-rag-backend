from pdf_islemleri import pdf_yukle_ve_parcala
from vektor_veritabani import veritabani_olustur_ve_kaydet
import os

def veritabanini_kur():
    # İşleyeceğimiz PDF'in yolu
    pdf_yolu = "ISAD/2-scrum.pdf"
    
    if not os.path.exists(pdf_yolu):
        print(f"HATA: {pdf_yolu} dosyası bulunamadı!")
        return
        
    print(f"--- RAG SÜRECİ BAŞLIYOR: {pdf_yolu} ---")
    
    # 1. Aşama: Oku ve Parçala
    parcalar = pdf_yukle_ve_parcala(pdf_yolu)
    
    # 2. Aşama: Vektörleştir ve Veritabanına Kaydet
    veritabani_olustur_ve_kaydet(parcalar)
    
    print("\n--- İŞLEM TAMAMLANDI! ---")
    print("Artık projemizde metinlerimizin koordinatlarını tutan 'chroma_db' adında bir klasörümüz var.")

if __name__ == '__main__':
    veritabanini_kur()
