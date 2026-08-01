"""
Text Chunking Engine.
Breaks down large parsed documents into smaller, semantically meaningful chunks.
"""
import logging
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownTextSplitter

from backend.ingestion.document import Document

logger = logging.getLogger(__name__)

class TextChunker:
    """
    Engine for splitting Document objects into smaller chunks suitable for LLM context windows.
    Implements a dual-strategy approach:
    - MarkdownTextSplitter for .md files
    - RecursiveCharacterTextSplitter for everything else (PDFs, raw text)
    """

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Primary Splitter (PDFs, Text)
        self.default_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Secondary Splitter (Markdown)
        self.markdown_splitter = MarkdownTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """
        Takes a list of Documents (e.g., from PDF parser) and returns a flattened
        list of chunked Documents.
        """
        chunked_docs = []
        
        for doc in documents:
            # Determine strategy based on source filename
            is_markdown = doc.metadata.source.lower().endswith(".md")
            splitter = self.markdown_splitter if is_markdown else self.default_splitter
            
            # Use LangChain to split the raw text
            text_chunks = splitter.split_text(doc.text)
            
            # Map back to our standard Document model
            for i, chunk_text in enumerate(text_chunks):
                # Copy existing metadata so we don't lose source or page_number
                new_metadata = doc.metadata.model_copy()
                # Add chunk index for traceability
                new_metadata.extra["chunk_index"] = i
                
                chunked_docs.append(Document(
                    text=chunk_text,
                    metadata=new_metadata
                ))
                
        logger.info(f"Chunked {len(documents)} original docs into {len(chunked_docs)} chunks.")
        return chunked_docs
