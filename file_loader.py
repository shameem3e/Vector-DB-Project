# file_loader.py
import fitz  # PyMuPDF
import os

def load_documents(input_folder="input", chunk_size=300):
    """Read all PDF and TXT files from the input folder and split into chunks."""
    documents = []

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)

        if file.lower().endswith(".pdf"):
            text = read_pdf(file_path)
            chunks = chunk_text(text, chunk_size)
        elif file.lower().endswith(".txt"):
            text = read_txt(file_path)
            chunks = chunk_text(text, chunk_size)
        else:
            continue

        for chunk in chunks:
            documents.append((file, chunk))  # Store filename + chunk

    return documents


def read_pdf(file_path):
    """Extract text from PDF."""
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        if text.strip():
            full_text += " " + text.strip()
    return full_text


def read_txt(file_path):
    """Read text from TXT file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=300):
    """Split text into chunks of about `chunk_size` words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks
