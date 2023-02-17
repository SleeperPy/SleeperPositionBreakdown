#!python3
"""Use this to get all the players in the NFL through sleeper API.
Use this once per day AT MOST"""

# Importing
import requests
import json

# Get all the players/player IDS
response = requests.get(f'https://api.sleeper.app/v1/players/nfl')
player_info = response.json() 

# Serializing json object
json_object = json.dumps(player_info, indent=4)

# Writing to a file to be used with other scripts
with open('player_info.json', 'w') as player:
    player.write(json_object)
