FROM python:3.11-slim

# Install git for committing logs
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install requests

CMD ["python", "send_data.py"]
