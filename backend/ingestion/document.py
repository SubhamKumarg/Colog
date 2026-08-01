"""
Standard Document models for Colog Ingestion.
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    """Metadata associated with an extracted document chunk/page."""
    source: str = Field(..., description="The original filename or URL")
    page_number: Optional[int] = Field(None, description="Page number for PDFs, if applicable")
    total_pages: Optional[int] = Field(None, description="Total pages in the source document")
    extra: Dict[str, Any] = Field(default_factory=dict, description="Any additional metadata")

class Document(BaseModel):
    """The standard unit of extracted text."""
    text: str = Field(..., description="The extracted text content")
    metadata: DocumentMetadata = Field(..., description="Metadata identifying the source")
