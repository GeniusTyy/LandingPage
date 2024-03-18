import requests

response = requests.get("http://localhost:1080/messages")
email = response.json()
print(response.status_code)
print(email)
