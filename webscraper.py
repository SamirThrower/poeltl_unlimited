import requests

url = "https://api.balldontlie.io/v1/players"
headers = {"Authorization": "3ecb5d27-0392-49d2-93e2-078d75e9b478"}
players = requests.get(url, headers=headers)

jsonplayers = players.json()
print(jsonplayers)