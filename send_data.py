import requests
import json
import os
from datetime import datetime

# API endpoint
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")

print(f"Sending data to {API_URL}")

# Load JSON payload
with open("data.json", "r") as f:
    data = json.load(f)

# Make POST request
response = requests.post(API_URL, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# === LOG THIS RUN ===
log_entry = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "status_code": response.status_code,
    "payload_sent": data,
    "response_received": response.json()
}

# Load existing history or create new
try:
    with open("run_history.json", "r") as f:
        history = json.load(f)
except FileNotFoundError:
    history = []

# Append new entry
history.append(log_entry)

# Save updated history
with open("run_history.json", "w") as f:
    json.dump(history, f, indent=2)

print("✅ Run logged to run_history.json")
