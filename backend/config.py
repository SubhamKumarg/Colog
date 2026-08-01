"""
Configuration Module for Colog.
Loads environment variables and provides structured configuration objects.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Central configuration class."""
    
    # System Paths
    # We resolve against BASE_DIR to handle relative paths in .env gracefully
    DATA_DIR: Path = BASE_DIR / os.getenv("DATA_DIR", "database/db_data")
    UPLOAD_DIR: Path = BASE_DIR / os.getenv("UPLOAD_DIR", "uploads")
    MODELS_DIR: Path = BASE_DIR / os.getenv("MODELS_DIR", "models")
    
    # LLM Configuration
    LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "http://localhost:11434")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama2")
    
    # App Configuration
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "True").lower() in ("true", "1", "yes")

    @classmethod
    def ensure_directories(cls):
        """Ensure all required directories exist."""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        cls.MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Instantiate a global configuration object
config = Config()
