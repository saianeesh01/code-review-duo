FROM python:3.11-slim-bullseye

# Upgrade system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# 11434 not needed here – the Ollama container owns it
CMD ["python", "-m", "crewai_app.main"]
