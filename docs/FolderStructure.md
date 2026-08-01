# Folder Structure

```text
Colog/
├── backend/                # Core Python backend
│   ├── config.py           # Configuration management
│   ├── database/           # SQLite and ChromaDB repositories
│   ├── embeddings/         # Chunking and Vector generation
│   ├── ingestion/          # Parsers (PDF, MD, Audio, YT)
│   ├── llm/                # LangChain chains and prompts
│   └── orchestrator.py     # Application facade
├── docs/                   # System documentation
├── frontend/               # Streamlit application
│   ├── app.py              # Entry point
│   ├── components/         # UI Widgets
│   └── state.py            # Session management
├── models/                 # Local model storage (ignored by git)
├── tests/                  # Pytest suite mirroring backend structure
├── uploads/                # Temporary file staging
├── .env.example            # Environment template
├── .gitignore              # Ignored files
├── README.md               # Main entry point
└── requirements.txt        # Python dependencies
```
