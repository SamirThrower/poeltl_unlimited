# import requests

# url = "https://api.balldontlie.io/v1/players"

# players = requests.get(url, headers=headers)

# jsonplayers = players.json()
# print(jsonplayers)

import requests

url = "https://api-nba-v1.p.rapidapi.com/players"

querystring = {"team":"1","season":"2021"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())