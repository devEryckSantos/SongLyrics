import requests


endpoint = "https://api.lyrics.ovh/v1/sia/chandelier"

response = requests.get(endpoint)

print(response.json()["lyrics"])