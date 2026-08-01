# Architecture

Colog utilizes a decoupled, layered architecture to ensure maintainability, testability, and scalability.

## Core Layers

1. **User Interface (UI) Layer**
   - Implemented via Streamlit.
   - Strictly responsible for presentation and capturing user input. Contains no business logic.

2. **Orchestration Layer**
   - Acts as the Facade between the UI and the Business Logic.
   - Routes requests (e.g., "Ingest PDF", "Answer Question").

3. **Business Logic Layer (Domain)**
   - **Ingestion**: Parsers for PDF, Markdown, Audio, and Video.
   - **Embeddings**: Text chunking and vector generation.
   - **LLM/RAG**: Prompt construction and generation chains.

4. **Data Access Layer (Repository Pattern)**
   - Abstracts underlying storage mechanisms.
   - `ChromaRepository` handles vector DB interactions.
   - `SQLiteRepository` handles conversational memory and metadata state.

## Dependency Injection
Modules are injected with their dependencies (e.g., the Chunker receives an instantiated Splitter, the Orchestrator receives instantiated Repositories). This prevents tight coupling and allows for easy mocking during testing.
