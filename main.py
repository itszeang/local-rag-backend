from pdf_processor import load_and_split_pdf
from vector_database import create_and_save_database
import os

def setup_database():
    pdf_path = "ISAD/2-scrum.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"ERROR: File {pdf_path} not found!")
        return
        
    print(f"--- RAG PROCESS STARTING: {pdf_path} ---")
    
    # Step 1: Load and Split
    chunks = load_and_split_pdf(pdf_path)
    
    # Step 2: Vectorize and Save to Database
    create_and_save_database(chunks)
    
    print("\n--- PROCESS COMPLETED! ---")
    print("We now have a 'chroma_db' folder holding the coordinates of our texts.")

if __name__ == '__main__':
    setup_database()
