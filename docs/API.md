# Internal API Documentation

*(This document will be automatically populated as the Orchestrator API solidifies).*

## Backend Orchestrator

The `Orchestrator` class is the primary interface for the frontend.

### `ingest_file(file_path: Path) -> bool`
- **Description**: Determines file type, routes to appropriate parser, chunks the text, and stores embeddings in the vector database.
- **Returns**: `True` on success, `False` on failure.

### `ask_question(query: str, session_id: str) -> str`
- **Description**: Retrieves semantic context from the vector database, formats the prompt, and queries the local LLM.
- **Returns**: The generated answer string.
