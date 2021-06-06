from datetime import datetime
from bs4 import BeautifulSoup
import requests

def Misha():
    website = requests.get('https://steamcommunity.com/id/BuriyDude/')
    soup = BeautifulSoup(website.content, 'lxml')

    data = soup.find('div', class_ = 'profile_in_game_header')
    game = soup.find('div', class_ = 'profile_in_game_name')

    print(data.text)

    if game == None:
        game_status = "<a> Not playing </a>"
    else:
        game_status = '<a>' + game.text + '</a>'

    now = datetime.now() # current date and time

    bettertime = now.strftime('%Y-%m-%d %H-%M')


    print(bettertime)

    f = open("templates/record.html", "a")
    f.write('<a>' + bettertime + ' </a>' + ' <a> ' + data.text + ' </a> ' + game_status + '<br>')
    f.close()

