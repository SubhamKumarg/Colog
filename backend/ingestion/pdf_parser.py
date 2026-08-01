"""
PDF Parser using PyMuPDF (fitz).
"""
import re
import logging
from pathlib import Path
from typing import List

import fitz  # PyMuPDF
from backend.ingestion.document import Document, DocumentMetadata

logger = logging.getLogger(__name__)

class IngestionError(Exception):
    """Base exception for errors during file ingestion."""
    pass

def clean_text(text: str) -> str:
    """Basic text cleaning to remove excessive whitespace and unprintable characters."""
    # Replace multiple spaces/newlines with a single space, but preserve paragraph breaks
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def parse_pdf(file_path: Path) -> List[Document]:
    """
    Reads a PDF file and extracts text page by page.
    
    Args:
        file_path: Path to the PDF file.
        
    Returns:
        A list of Document objects, one for each page with extracted text.
        
    Raises:
        IngestionError: If the file is missing or corrupted.
    """
    if not file_path.exists():
        raise IngestionError(f"File not found: {file_path}")
        
    documents = []
    
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        logger.error(f"Failed to open PDF {file_path}: {e}")
        raise IngestionError(f"Corrupted or invalid PDF: {file_path}") from e

    total_pages = len(doc)
    
    if total_pages == 0:
        logger.warning(f"Empty PDF (0 pages): {file_path}")
        return []
        
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        cleaned_text = clean_text(text)
        
        # We might skip entirely empty pages
        if not cleaned_text:
            logger.info(f"Page {page_num} of {file_path.name} is empty or an image without OCR.")
            continue
            
        metadata = DocumentMetadata(
            source=file_path.name,
            page_number=page_num,
            total_pages=total_pages
        )
        
        documents.append(Document(text=cleaned_text, metadata=metadata))
        
    doc.close()
    
    if not documents:
        logger.warning(f"PDF yielded no extractable text (possibly scanned image): {file_path}")
        
    return documents
