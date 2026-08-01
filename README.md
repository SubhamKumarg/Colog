# Colog - AI Personal Knowledge Assistant

Colog is a production-quality offline AI Personal Knowledge Assistant. It is capable of ingesting PDFs, Markdown vaults, local audio files, and YouTube videos, indexing them with semantic embeddings inside a local vector database, and answering questions using Retrieval-Augmented Generation (RAG).

**Crucially, the system runs completely locally without relying on cloud APIs.**

## Features
- **Offline First**: All LLM and embedding models run locally on your hardware.
- **Multi-Modal Ingestion**: Support for Text, PDFs, Markdown, Local Audio, and YouTube Audio.
- **Advanced RAG**: Context-aware answers utilizing LangChain and ChromaDB.
- **Modular Architecture**: Built adhering strictly to SOLID principles and Clean Architecture.

## Documentation
Detailed documentation can be found in the `docs/` directory:
- [Architecture](docs/Architecture.md)
- [Installation](docs/Installation.md)
- [Roadmap](docs/Roadmap.md)
- [Development Log](docs/DevelopmentLog.md)
- [Folder Structure](docs/FolderStructure.md)
- [API](docs/API.md)

## Tech Stack
- **Language**: Python 3.12
- **Frontend**: Streamlit
- **LLM**: Gemma or Qwen (via Ollama/llama.cpp)
- **Embeddings**: BAAI/bge-small-en-v1.5
- **Vector DB**: ChromaDB
- **Transcription**: Faster Whisper

## License
MIT License
