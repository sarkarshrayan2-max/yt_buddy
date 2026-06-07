# 🎥 YT Buddy

AI-Powered YouTube Learning Assistant

YT Buddy is an end-to-end AI application that transforms YouTube videos into interactive learning experiences. Users can generate intelligent summaries, chat with video content using RAG (Retrieval-Augmented Generation), translate summaries into multiple languages, and export results as PDFs. [https://ytbuddy-learnaccordingtoyou.streamlit.app/](https://ytbuddy-learnaccordingtoyou.streamlit.app/)

---

## 🚀 Features

### 📜 Transcript Extraction

* Extracts transcripts directly from YouTube videos.
* Handles long-form educational videos and podcasts.

### 🧠 Intelligent Summarization

* Direct summarization for short videos.
* Map-Reduce summarization for long videos.
* Generates:

  * Short Summary
  * Detailed Explanation
  * Key Takeaways
  * Important Concepts
  * Actionable Insights

### ✂️ Smart Chunking

* Automatically detects transcript length.
* Switches between:

  * Direct Processing
  * Chunk-Based Processing
* Uses overlapping chunks to preserve context.

### 💬 Chat With Video (RAG)

* Ask questions about video content.
* Uses:

  * Sentence Transformers
  * FAISS Vector Database
  * Groq LLM
* Retrieves relevant transcript chunks before generating answers.

### 🌍 Translation Support

Translate summaries and answers into:

* English
* Hindi
* Bengali
* French
* Spanish

### 📄 PDF Export

Export:

* Video Summary
* Key Concepts
* Chat History

### 🎥 Video Metadata

Displays:

* Video Title
* Channel Name
* Publish Date
* Duration
* Thumbnail

### ☁️ Cloud Deployment

* Streamlit Cloud Deployment
* GitHub Actions CI/CD Pipeline

---

## 🏗️ Architecture

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Smart Chunking Engine
      ↓

Short Video?
      ↓
Direct Summary

Long Video?
      ↓
Chunking
      ↓
Map-Reduce Summarization

      ↓

FAISS Vector Store
      ↓
Question Answering (RAG)
      ↓
Groq LLM
      ↓
Answer Generation
```

---

## 🧠 RAG Pipeline

```text
Transcript
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS
      ↓
Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
Groq LLM
      ↓
Answer
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Groq
* Llama 3.1 8B Instant

### NLP

* Sentence Transformers
* LangChain

### Vector Database

* FAISS

### Data Processing

* YouTube Transcript API
* PyTube

### PDF Generation

* FPDF2

### Deployment

* Streamlit Community Cloud
* GitHub Actions

---

## 📂 Project Structure

```text
yt_buddy/
│
├── app.py
│
├── src/
│   ├── config.py
│   ├── transcript.py
│   ├── chunker.py
│   ├── summarizer.py
│   ├── rag.py
│   ├── translator.py
│   ├── video_metadata.py
│   ├── pdf_generator.py
│   └── prompts.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── main.yml
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sarkarshrayan2-max/yt_buddy.git
cd yt_buddy
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

Add screenshot here.

### Summary Generation

Add screenshot here.

### Chat With Video

Add screenshot here.

### PDF Export

Add screenshot here.

---

## 🎯 Future Enhancements

* Playlist Summarization
* Timestamp-Based Citations
* Multi-Video Knowledge Base
* Audio Upload Support
* User Authentication
* Persistent Chat Memory
* Advanced PDF Formatting
* Support for More Languages

---

## 👨‍💻 Author

Shrayan Sarkar

B.Tech – Electronics & Computer Science Engineering

Machine Learning & AI Enthusiast

GitHub: https://github.com/sarkarshrayan2-max

LinkedIn: Add your LinkedIn profile here

---

## ⭐ If you found this project useful, consider giving it a star!
