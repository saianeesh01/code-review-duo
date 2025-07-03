# code-review-duo

Automated code review and fix agent using CrewAI/AutoGen, Ollama, and GitHub Actions.

## Features
- Automated code review on PRs
- Suggests fixes and improvements
- Uses tree-sitter for code chunking
- Embeddings via Ollama
- Chroma/FAISS for RAG

## Setup
1. Copy `.env.example` to `.env` and fill in your secrets.
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `python -m crewai_app.main`

## GitHub Action
See `.github/workflows/pr_review.yaml` for CI setup.
