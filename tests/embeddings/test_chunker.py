"""
Unit tests for the Text Chunking Engine.
"""
from backend.embeddings.chunker import TextChunker
from backend.ingestion.document import Document, DocumentMetadata

def test_recursive_chunking():
    """Test that a large standard text is chunked recursively."""
    chunker = TextChunker(chunk_size=50, chunk_overlap=10)
    
    large_text = "This is a very long sentence. It is designed to be broken into smaller pieces.\n\nHere is a second paragraph that should be kept together if possible."
    
    doc = Document(
        text=large_text,
        metadata=DocumentMetadata(source="test.pdf", page_number=1)
    )
    
    chunks = chunker.chunk_documents([doc])
    
    assert len(chunks) > 1
    # Check that metadata was preserved and extended
    assert chunks[0].metadata.source == "test.pdf"
    assert chunks[0].metadata.page_number == 1
    assert chunks[0].metadata.extra["chunk_index"] == 0
    assert chunks[1].metadata.extra["chunk_index"] == 1

def test_markdown_chunking():
    """Test that markdown files use the markdown splitter."""
    chunker = TextChunker(chunk_size=100, chunk_overlap=0)
    
    md_text = "# Header 1\nThis is under header 1.\n## Header 2\nThis is under header 2."
    
    doc = Document(
        text=md_text,
        metadata=DocumentMetadata(source="notes.md")
    )
    
    chunks = chunker.chunk_documents([doc])
    
    assert len(chunks) > 1
    assert chunks[0].metadata.source == "notes.md"
    assert chunks[0].metadata.extra["chunk_index"] == 0
