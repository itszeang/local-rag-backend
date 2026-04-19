# Local RAG Backend (API'siz Çevrimdışı Vektör Arama & Ollama LLM) 🚀

Bu proje, **RAG (Retrieval-Augmented Generation)** mimarisinin arka planını uçtan uca anlamak amacıyla geliştirilmiş eğitim odaklı bir projedir. 

Projenin en büyük özelliği, metinleri anlamlandırmak ve yapay zeka cevapları üretmek için **hiçbir ücretli API'ye (OpenAI vb.) ihtiyaç duymamasıdır.** Tamamen yerel (local) çalışan HuggingFace tabanlı ll-MiniLM-L6-v2 embedding modeli ve **Ollama (Llama 3.2)** kullanılmıştır.

## 🛠️ Kullanılan Teknolojiler
- **LangChain:** Tüm RAG akışının orkestrasyonu.
- **PyPDF:** PDF belgelerini okuyup işlemek.
- **Sentence-Transformers (HuggingFace):** Metinleri yerel işlemci (CPU) gücüyle anlamsal uzayda vektörlere dönüştürmek.
- **ChromaDB:** Vektörleri saklamak ve mesafe/benzerlik araması yapmak için vektör veritabanı.
- **Ollama:** Vektörel aramadan dönen sonuçları okuyup, insan dilinde anlamlı ve net cevaplar üreten yerel Büyük Dil Modeli (LLM).

## ⚙️ Kurulum ve Çalıştırma

1. Repoyu bilgisayarınıza klonlayın.
2. Bir sanal ortam (venv) oluşturup aktif edin.
3. Gerekli kütüphaneleri yükleyin:
   `ash
   pip install -r requirements.txt
   `
4. Sisteminize [Ollama](https://ollama.com/) kurun ve Llama 3.2 modelini indirin:
   `ash
   ollama run llama3.2
   `
5. Veritabanını oluşturmak ve PDF'leri vektörlere çevirmek için:
   `ash
   python main.py
   `
6. Sisteme soru sormak ve LLM'den cevap almak için:
   `ash
   python soru_sor.py
   `

## 🧠 Nasıl Çalışıyor? (Özellikler)
- **Vektörel Parçalama:** PDF yüklenir ve RecursiveCharacterTextSplitter ile küçük parçalara bölünür.
- **Benzerlik Araması:** Kullanıcı soru sorduğunda, vektörel uzayda soruya en yakın 3 metin parçası (Chunk) bulunur.
- **Yapılandırılmış JSON Çıktısı:** Proje artık ham metin yerine profesyonel bir backend API gibi **JSON** formatında yanıt döndürür. Çıktı şunları içerir:
  - Kullanıcının sorusu (\query\)
  - Ollama'nın ürettiği net LLM cevabı (\nswer\)
  - Kullanılan kaynak metinler ve **Benzerlik Skorları** (\elevance_score\)
  - Kullanılan model detayları (\metadata\).
