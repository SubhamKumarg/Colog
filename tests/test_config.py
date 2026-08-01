"""
Tests for the backend configuration module.
"""
import os
from pathlib import Path
from backend.config import Config

def test_config_defaults(monkeypatch):
    """Test that configuration uses reasonable defaults if environment variables are missing."""
    # Temporarily remove all env variables
    monkeypatch.delenv("DATA_DIR", raising=False)
    monkeypatch.delenv("UPLOAD_DIR", raising=False)
    monkeypatch.delenv("MODELS_DIR", raising=False)
    monkeypatch.delenv("LLM_BASE_URL", raising=False)
    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("DEBUG_MODE", raising=False)

    # Note: the Config class attributes are evaluated at import time, 
    # so we should test against the class logic if we mock. 
    # Better yet, let's just assert the default fallback values.
    
    # We will reload the module to ensure monkeypatch takes effect
    import importlib
    import backend.config
    importlib.reload(backend.config)
    
    config = backend.config.Config
    
    assert "database" in str(config.DATA_DIR)
    assert "uploads" in str(config.UPLOAD_DIR)
    assert "models" in str(config.MODELS_DIR)
    assert config.LLM_BASE_URL == "http://localhost:11434"
    assert config.LLM_MODEL == "llama2"
    assert config.DEBUG_MODE is True
