import requests

url = "https://pokeapi.co/api/v2/generation/?limit=2"
response = requests.get(url)

{
	"count": 7,
	"next": "https://pokeapi.co/api/v2/generation/?offset=2&limit=2",
	"previous": None,
	"results": [
    	{
        	"name": "generation-i",
        	"url": "https://pokeapi.co/api/v2/generation/1/"
    	},
    	{
        	"name": "generation-ii",
        	"url": "https://pokeapi.co/api/v2/generation/2/"
    	}
	]
}

import requests

url = "https://pokeapi.co/api/v2/generation/?limit=2"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\nRaw JSON Response:")
    print(data)

    print("\nFormatted Output:")
    print(f"Total Generations Available: {data['count']}")
    print(f"Next Page: {data['next']}")
    print(f"Previous Page: {data['previous']}")

    print("\nFirst Two Generations:")
    for generation in data['results']:
        print(f"- {generation['name'].replace('-', ' ').title()} ({generation['url']})")
else:
    print("Error fetching data from API.")
