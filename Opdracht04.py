import requests

from bs4 import BeautifulSoup

import pandas as pd


def get_data():
    r = requests.get("https://www.top40.nl/top40")

    soup = BeautifulSoup(r.content)

    posities = soup.find_all('div', class_='dot-icon')
    vorige_en_weken = soup.find_all('div', class_='statcolumn pull-left text-center hidden-md-down')
    vorigen = []
    weken = []
    for i in range(len(vorige_en_weken)):
        if i % 2 == 0:
            vorigen.append(vorige_en_weken[i])
        else:
            weken.append(vorige_en_weken[i])

    titles = soup.select("h3.title")
    artists = soup.select("p.artist")

    return posities, vorigen, weken, titles, artists


def make_data_frame(data):
    posities, vortigen, weken, titles, artists = data
    songs = []

    for i in range(len(posities)):
        dic = {"positie": posities[i].text,
               "vorige positie": vorigen[i].text.strip(),
               "weken": weken[i].text.strip(),
               "titel": titles[i].text.strip(),
               "artiest": artists[i].text.strip()
               }
        songs.append(dic)

    songs = pd.DataFrame(data = songs)
    return songs


data = get_data()

songs = make_data_frame(data)
songs.to_csv("Top40.csv")
print(songs.info())
print(songs.head())
