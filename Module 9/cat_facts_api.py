import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()