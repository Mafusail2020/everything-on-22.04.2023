import requests
from bs4 import BeautifulSoup
import time
from random import randint

pages_num = 3
songs_num = 20
total_songs = pages_num * songs_num
help_num = 0

for i in range(pages_num):
    link = f'https://now.morsmusic.org'
    url = f'/artist/100?page={i}'
    request = requests.get(link + url).text
    soup_main = BeautifulSoup(request, 'lxml')
    cont = soup_main.find('div', id='main-wrapper').find('div', class_='wrapper-elements')
    for j in range(songs_num):
        song_block = cont.find_all('div', class_='track mustoggler')[j].find('div', class_='track-control').find('div', class_='track-control-item track-duration').find('a').get('href')
        song = requests.get(link + song_block).content
        with open(f"Номер_песни_{help_num+1}.mp3", "wb") as file:
            file.write(song)
        print(f"Песен скачано {help_num+1}/{total_songs}")
        time.sleep(randint(1, 2))
        help_num += 1

# Helpful links
# https://mezzoforte.ru/s/leningrad.html
