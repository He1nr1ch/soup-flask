from bs4 import BeautifulSoup

import requests


website = requests.get('https://steamcommunity.com/id/BuriyDude/')
soup = BeautifulSoup(website.content, 'lxml')

data = soup.find('div', class_ = 'profile_in_game_header')
game = soup.find('div', class_ = 'profile_in_game_name')

print(data.text)
print(game.text)