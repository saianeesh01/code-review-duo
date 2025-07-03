# Dockerfile for code-review-duo
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Start Ollama server and run the main app
CMD ["sh", "-c", "ollama serve & python -m crewai_app.main"]
