# 📚 Vector DB Project

A minimal **local vector database system** that lets you search your **PDF** and **TXT** files using semantic meaning rather than just keywords.  
Perfect for building **local RAG (Retrieval-Augmented Generation)** prototypes and understanding how modern search works.

---

## 📌 Features
- 📂 Load and process **multiple PDFs/TXTs** from the `input/` folder.
- ✂️ **Automatic text chunking** for better search accuracy.
- 🤖 Use **Sentence Transformers** to generate semantic embeddings.
- ⚡ **FAISS** for fast similarity search on vectors.
- 🔍 Search for text **by meaning**, not exact word match.
- 🖥 Works **offline** — no external APIs required.

---

## 📂 Folder Structure
vector-db-project/

│

├── main.py # Runs the app: loads data, builds index, handles queries

├── file_loader.py # Reads PDFs/TXTs and splits into text chunks

├── vector_db.py # Builds vector database & performs similarity search

│

├── input/ # Place your PDF/TXT files here

│ ├── example.pdf

│ ├── notes.txt

│

├── requirements.txt # List of Python dependencies

└── README.md # Project documentation


---

## ⚙️ Setup Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/shameem3e/Vector-DB-Project.git
cd Vector-DB-Project

```
### **2️⃣ Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```
### **3️⃣ Install Requirements**
```bash
pip install -r requirements.txt

```
### **4️⃣ Add files**
Place your `PDF` or `TXT` files in the `input/` folder.

Example:
```bash
input/
 ├── example1.pdf
 ├── example2.txt

```
### **5️⃣ Run the project**
```bash
python main.py

```
### **6️⃣ Example run**
User input:
```bash
Enter your search query (or 'exit' to quit): what is machine learning

```
Output:
```bash
Top matches:
[machine_learning_notes.pdf] Machine learning is a subset of AI that focuses on algorithms learning patterns... (score: 0.4231)
[research_summary.txt] ML models are trained using data to predict future outcomes... (score: 0.4512)

```
## 📜 Code Overview
This project uses three main Python files:

### 1. `file_loader.py`
* PyMuPDF (`fitz`) → Extracts text from PDF files.
* Chunking function → Splits long text into smaller segments (~300 words) for better search results.

### 2. `vector_db.py`
* Sentence Transformers ([all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)) → Turns text into numerical vectors (embeddings) that represent meaning.
* FAISS → Stores these vectors and allows fast nearest neighbor searches to find similar chunks.

### 3. `main.py`
* Loads documents from `input/`.
* Builds a FAISS index.
* Runs a query loop so you can search your files in real time.

## ❓ FAQ
Q: Why do we need chunking?

A: Without it, a query might match an entire page of irrelevant content. Smaller chunks increase relevance.

Q: Does this work without internet?

A: Yes! All models and tools run locally once installed.

Q: Can I add DOCX or HTML files?

A: Yes — just extend file_loader.py to handle new formats.

Q: Is this production-ready?

A: It’s a prototype for learning. For production, add persistence, error handling, and scaling features.

## 🛠 Tech Stack
* Python – Main programming language.
* Sentence Transformers – Generates semantic embeddings from text.
* FAISS – Facebook AI Similarity Search for fast vector lookup.
* PyMuPDF – Efficient PDF text extraction.
* NumPy – Vector/matrix operations for embeddings.

## 🚀 Future Improvements
* 💾 Persistence → Save/load FAISS index to avoid rebuilding.
* 📄 More file types → DOCX, HTML, CSV.
* 🧠 Integrate with LLMs for Retrieval-Augmented Generation (RAG).
* 🌐 Web interface using Flask or FastAPI.
* 🔍 Advanced ranking using cosine similarity instead of L2 distance.

## 👨‍💻 Author
[MD. Shameem Ahammed](https://sites.google.com/view/shameem3e)

Graduate Student | AI & ML Enthusiast

---

