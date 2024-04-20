import requests

url = 'http://localhost:5000/upload'
files = "/Users/B0295868/Downloads/together-1.1.2/testing.jsonl"
response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
