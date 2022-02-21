import requests

KIWI_ENDPOINT="https://tequila-api.kiwi.com/locations/query"

sheet_data=[{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
            {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
            {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
            {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
            {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
            {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
            {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
            {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
            {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]


heads={
    "apikey":"yourkey"
}

query = {"term": "brussels", "location_types": "city"}

response = requests.get(url=KIWI_ENDPOINT, headers=heads, params=query)
results = response.json()["locations"]
print(results)



