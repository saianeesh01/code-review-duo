import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

OLLAMA_BASE = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
CHAT_MODEL  = os.getenv("CHAT_MODEL",  "mistral:7b-instruct")
EMBED_MODEL = os.getenv("EMBED_MODEL", "mistral:7b")
VECTOR_DB   = Path(os.getenv("VECTOR_DB", BASE_DIR / "data")).expanduser()
CHUNK_LINES = int(os.getenv("CHUNK_LINES", "150"))
