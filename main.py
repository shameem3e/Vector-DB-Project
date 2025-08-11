# main.py
from vector_db import VectorDatabase
from file_loader import load_documents

def main():
    # Step 1: Load documents from 'input/' folder
    documents = load_documents("input")
    if not documents:
        print("No documents found in 'input/' folder.")
        return

    # Step 2: Initialize and build vector DB
    vdb = VectorDatabase()
    vdb.build_index(documents)

    # Step 3: Search loop
    while True:
        query = input("\nEnter your search query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        results = vdb.search(query, k=3)
        print("\nTop matches:")
        for filename, text, score in results:
            print(f"[{filename}] {text[:100]}... (score: {score:.4f})")

if __name__ == "__main__":
    main()
