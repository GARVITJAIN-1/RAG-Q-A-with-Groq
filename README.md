# RAG-Q-A-with-Groq

> Retrieval-Augmented Generation question answering over research papers using LangChain and Groq.

![GitHub stars](https://img.shields.io/github/stars/GARVITJAIN-1/RAG-Q-A-with-Groq?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/GARVITJAIN-1/RAG-Q-A-with-Groq?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/GARVITJAIN-1/RAG-Q-A-with-Groq?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/GARVITJAIN-1/RAG-Q-A-with-Groq?style=for-the-badge&logo=github) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📑 Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Key Dependencies](#key-dependencies)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Contributing](#contributing)

## 📝 Description

RAG-Q-A-with-Groq is a Python-based Retrieval-Augmented Generation (RAG) application designed to facilitate automated question answering over scientific and academic documents. By pairing the orchestrational strength of LangChain with high-speed inference, this project enables users to extract insights directly from technical papers without manual searching.

## ✨ Key Features

- **📄 Research Paper Ingestion** — Processes and indexes PDF or text-based academic publications from a dedicated local research papers directory.
- **🔗 LangChain Orchestration** — Coordinates document retrieval, splitting, embedding generation, and prompt construction using the LangChain library.
- **⚡ Groq-Powered LLM Inference** — Leverages the Groq API to deliver low-latency responses based on the retrieved context from your documents.

## 🎯 Use Cases

- Querying a collection of academic papers to extract specific methodologies, formulas, or conclusions.
- Developing and testing localized Retrieval-Augmented Generation workflows utilizing LangChain and Groq inference.

## 🛠️ Tech Stack

- 🐍 **Python**

**Notable libraries:** LangChain

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/GARVITJAIN-1/RAG-Q-A-with-Groq.git

# 2. Create & activate a virtualenv
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 📦 Key Dependencies

```
langchain: latest
langchain-core: latest
langchain-community: latest
langchain-openai: latest
langchain-ollama: latest
langchain-groq: latest
langchain-text-splitters: latest
python-dotenv: latest
streamlit: latest
faiss-cpu: latest
pypdf: latest
chromadb: latest
langchain_huggingface: latest
langchain_chroma: latest
sentence-transformers: latest
```

## 📁 Project Structure

```
.
├── app2.py
├── requirements.txt
└── research_papers
    ├── Attention.pdf
    └── LLM.pdf
```

## 🛠️ Development Setup

### Python
1. Install Python (v3.10+ recommended)
2. `python -m venv venv && source venv/bin/activate`  (Windows: `venv\Scripts\activate`)
3. `pip install -r requirements.txt`

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/GARVITJAIN-1/RAG-Q-A-with-Groq.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a pull request

Please follow the existing code style and include tests for new behavior where applicable.

---
*This README was generated with ❤️ by [ReadmeBuddy](https://readmebuddy.com)*
