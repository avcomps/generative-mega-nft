# Copyright @ Ali Vorobiev (https://github.com/avcomps).

import requests as rq
from bs4 import BeautifulSoup

PLAYER_URL = "https://www.transfermarkt.com/cristiano-ronaldo/alletore/spieler/8198/plus/0?saison=&verein=&liga=&wettbewerb=&pos=&minute=&pos=&torart=&stand="
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
# goal example : ronaldo goal vs moreirense 2:0 solo run 2002/03


html_res = rq.get(PLAYER_URL, headers=headers).text

print("----------------------------------------")

soup = BeautifulSoup(html_res, features="lxml")
table = soup.find("table", attrs={"class":"details"})

print(soup)
print("----------------------------------------")
print(table)
print("----------------------------------------")

# The first tr contains the field names.
headings = [th.get_text() for th in table.find("tr").find_all("th")]

for row in table.find_all("tr")[1:]:
    print(row)
    print("111111111111111111111110000000000000000000")


