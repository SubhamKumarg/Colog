"""
Unit tests for the PDF Parser module.
"""
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from backend.ingestion.pdf_parser import parse_pdf, IngestionError, clean_text
from backend.ingestion.document import Document

@pytest.fixture
def mock_pdf_path(tmp_path):
    """Fixture for a temporary path representing a PDF."""
    pdf_path = tmp_path / "test.pdf"
    # Touch it so it 'exists'
    pdf_path.touch()
    return pdf_path

def test_clean_text():
    """Test the text cleaning logic."""
    raw = "This   is  a\n\n\n\nstring with   spaces."
    cleaned = clean_text(raw)
    assert "This is a\n\nstring with spaces." == cleaned
    assert clean_text("   \n\n  ") == ""

def test_parse_file_not_found():
    """Test that missing file raises IngestionError."""
    with pytest.raises(IngestionError, match="File not found"):
        parse_pdf(Path("does_not_exist.pdf"))

@patch('backend.ingestion.pdf_parser.fitz.open')
def test_parse_corrupted_pdf(mock_fitz_open, mock_pdf_path):
    """Test that fitz opening errors are wrapped in IngestionError."""
    mock_fitz_open.side_effect = Exception("Fitz failed to open")
    
    with pytest.raises(IngestionError, match="Corrupted or invalid PDF"):
        parse_pdf(mock_pdf_path)

@patch('backend.ingestion.pdf_parser.fitz.open')
def test_parse_empty_pdf(mock_fitz_open, mock_pdf_path):
    """Test handling of a PDF with 0 pages."""
    mock_doc = MagicMock()
    mock_doc.__len__.return_value = 0
    mock_fitz_open.return_value = mock_doc
    
    docs = parse_pdf(mock_pdf_path)
    assert len(docs) == 0

@patch('backend.ingestion.pdf_parser.fitz.open')
def test_parse_valid_pdf(mock_fitz_open, mock_pdf_path):
    """Test normal extraction of text from a multi-page PDF."""
    # Create fake pages
    page1 = MagicMock()
    page1.get_text.return_value = "Page 1 content."
    
    page2 = MagicMock()
    page2.get_text.return_value = "Page 2 content."
    
    page3 = MagicMock()
    page3.get_text.return_value = "   " # Empty text, should be skipped
    
    mock_doc = MagicMock()
    mock_doc.__len__.return_value = 3
    # Make the doc iterable to simulate iterating over pages
    mock_doc.__iter__.return_value = iter([page1, page2, page3])
    
    mock_fitz_open.return_value = mock_doc
    
    docs = parse_pdf(mock_pdf_path)
    
    assert len(docs) == 2
    assert docs[0].text == "Page 1 content."
    assert docs[0].metadata.page_number == 1
    assert docs[0].metadata.total_pages == 3
    
    assert docs[1].text == "Page 2 content."
    assert docs[1].metadata.page_number == 2
    
    # Assert close was called
    mock_doc.close.assert_called_once()
