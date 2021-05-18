import requests
from keys import KEYS


endpoint = "https://rest.coinapi.io/v1/trades/latest"
headers = {"X-CoinAPI-Key": KEYS[0], "Accept":"application/json"}
params = {"limit" : "1"}
response = requests.get(endpoint, headers = headers, params = params)

if response.status_code == 200:
	print(response.json())
elif response.status_code == 401:
	print("Problem with key!")
elif response.status_code == 403:
	print("No access!")
elif response.status_code == 429:
	print("Too many requests!")
elif response.status_code == 550:
	print("Missing data!")
