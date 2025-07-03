import os

GH_TOKEN = os.getenv('GH_TOKEN')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL')
CHROMA_DB_PATH = os.getenv('CHROMA_DB_PATH', './data/chroma_db')
MODEL_PATH = os.getenv('MODEL_PATH', './models')
