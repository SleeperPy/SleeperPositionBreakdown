#!python3
"""The purpose of this script is going to be determine the position breakout of players in a Sleeper Fantasy
Football League utilizing the Sleeper API. It will also take that information and visualize it."""

# imports
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt

# Get the users Sleeper League ID. This is found in the URL of the individual league on sleeper.app or in the settings of the sleeper mobile app
league_id = input('Enter your league ID: ')

# Get league info using the league ID above
response = requests.get(f'https://api.sleeper.app/v1/league/{league_id}')
league_info = response.json() 

# Get all of the users in the league
response = requests.get(f'https://api.sleeper.app/v1/league/{league_id}/users')
league_users = response.json()

# Get all rosters in the league, this is where max points for is stored (seems like it gets rid of the max points for value when the season is restarted)
response = requests.get(f'https://api.sleeper.app/v1/league/{league_id}/rosters')
league_rosters = response.json()

# This script depends on the full list of players pulled from the Sleeper API, since this is such a large file, Sleeper recommends you don't pull it often so I
# included another script in this repository that will pull that list and save it to your computer
# Write the full list of players to a python dictionary
with open('player_info.json', 'r') as player:
    players = json.load(player)

# Making a list that will have the owner's identifier and the IDs for the players on their team
new_dict = []
placeholder = ''

for i, j in enumerate(league_rosters):
    new_dict += [{'display_name':league_rosters[i]['owner_id'], 'players':league_rosters[i]['players']}]
    

# Replacing the IDs of each player on each team with their corresponding position
for o, p in enumerate(new_dict):
    for n, m in enumerate(new_dict[o]['players']):
        placeholder = new_dict[o]['players'][n]
        new_dict[o]['players'][n] = players[placeholder]['position']
        
# Adding the user's actual display name to the list
for i, j in enumerate(new_dict):
    for k, l in enumerate(league_users):
        if new_dict[i]['display_name'] == league_users[k]['user_id']:
            new_dict[i]['display_name'] = league_users[k]['display_name']

# Turning our list into a pandas dataframe
df = pd.DataFrame(new_dict)

# Exploding the lists of position groups each manager has 
df2 = df.apply(pd.Series.explode)

# Renaming the column names of our data for the graph
df2.rename(columns={'display_name': 'Manager', 'players': 'Position'}, inplace=True)

# Making the graph
df2.groupby(['Manager', 'Position']).size().unstack(fill_value=0).plot.bar()

plt.tight_layout()
plt.show()
