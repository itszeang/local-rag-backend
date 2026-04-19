from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path):
    print(f"[{pdf_path}] loading document...")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    print(f"Found a total of {len(pages)} pages.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks = text_splitter.split_documents(pages)
    print(f"Text divided into {len(chunks)} chunks.")
    
    return chunks

if __name__ == '__main__':
    print("PDF Processor Module Ready!")
