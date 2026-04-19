# Local RAG Backend (API'siz Çevrimdışı Vektör Arama) 🚀

Bu proje, **RAG (Retrieval-Augmented Generation)** mimarisinin arka planını (veri okuma, parçalama, vektörel veritabanı oluşturma ve arama) uçtan uca anlamak amacıyla geliştirilmiş eğitim odaklı bir projedir. 

Projenin en büyük özelliği, metinleri anlamlandırmak ve vektörlere çevirmek için **hiçbir ücretli API'ye (OpenAI vb.) ihtiyaç duymamasıdır.** Tamamen açık kaynaklı, yerel olarak (local) çalışan HuggingFace tabanlı ll-MiniLM-L6-v2 modeli kullanılmıştır.

## 🛠️ Kullanılan Teknolojiler
- **LangChain:** Tüm RAG akışının orkestrasyonu.
- **PyPDF:** PDF belgelerini okuyup işlemek.
- **Sentence-Transformers (HuggingFace):** Metinleri yerel işlemci (CPU) gücüyle anlamsal uzayda matematiksel vektörlere (embedding) dönüştürmek.
- **ChromaDB:** Vektörleri saklamak ve mesafe/benzerlik araması yapmak için vektör veritabanı.

## ⚙️ Kurulum ve Çalıştırma

1. Repoyu bilgisayarınıza klonlayın.
2. Bir sanal ortam (venv) oluşturup aktif edin.
3. Gerekli kütüphaneleri yükleyin:
   `ash
   pip install -r requirements.txt
   `
4. Veritabanını oluşturmak ve PDF'leri vektörlere çevirmek için:
   `ash
   python main.py
   `
   *(Bu işlem ilk çalıştırmada 90MB boyutundaki açık kaynaklı dil modelini indirecektir).*
5. Sisteme soru sormak ve en alakalı metinleri PDF'ten çekmek için:
   `ash
   python soru_sor.py
   `

## 🧠 Nasıl Çalışıyor?
1. PDF yüklenir ve RecursiveCharacterTextSplitter ile anlamlı küçük parçalara (chunk) bölünür.
2. Bu parçalar MiniLM modeli ile çok boyutlu uzayda koordinatlara (vektörlere) çevrilir ve chroma_db isimli klasöre diske kaydedilir.
3. Kullanıcı bir soru sorduğunda, soru da aynı modele girer ve vektörel uzayda soruya **anlamsal olarak en yakın** olan 3 metin parçası matematiksel olarak hesaplanıp saniyeler içinde ekrana basılır.
