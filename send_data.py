import requests
import json
import os

# Get the API endpoint (environment variable or default test URL)
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")

print(f"Sending data to {API_URL}")

# Load JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Make POST request
response = requests.post(API_URL, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
