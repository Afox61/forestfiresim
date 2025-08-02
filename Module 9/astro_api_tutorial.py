import requests

# Test API connection
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

# Print raw JSON data
print("\nRaw JSON Response:")
print(response.json())

# Format the output
data = response.json()
print("\nPeople Currently in Space:")
for person in data["people"]:
    print(f"{person['name']} aboard {person['craft']}")

