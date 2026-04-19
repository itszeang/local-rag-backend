from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def pdf_yukle_ve_parcala(pdf_yolu):
    # 1. Adım: PDF'i Yükleme
    print(f"[{pdf_yolu}] dosyası yükleniyor...")
    loader = PyPDFLoader(pdf_yolu)
    sayfalar = loader.load()
    print(f"Toplam {len(sayfalar)} sayfa bulundu.")

    # 2. Adım: Metni Parçalama (Chunking)
    # chunk_size: Her bir parçanın maksimum karakter sayısı
    # chunk_overlap: Cümlelerin/anlamın ortadan kesilmemesi için önceki parçadan alınan kopyalama payı
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    parcalar = text_splitter.split_documents(sayfalar)
    print(f"Metin toplam {len(parcalar)} parçaya (chunk) bölündü.")
    
    return parcalar

if __name__ == '__main__':
    print("PDF İşlemleri Modülü Hazır! Dışarıdan kullanılmayı bekliyor.")
