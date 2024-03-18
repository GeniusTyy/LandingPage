import requests

response = requests.get("http://localhost:1080/messages")

data = response.json()

recipient = "test@test.com"
for item in data:
    email = [
        recipient.replace("<", "").replace(">", "") for recipient in item["recipients"]
    ]
    if recipient in email:
        print(email[0] == recipient)
