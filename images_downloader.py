# Copyright @ Ali Vorobiev (https://github.com/avcomps).

import requests as rq
from bs4 import BeautifulSoup

PLAYER_URL = "https://www.transfermarkt.com/cristiano-ronaldo/alletore/spieler/8198/plus/0?saison=&verein=&liga=&wettbewerb=&pos=&minute=&pos=&torart=&stand="
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }

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

datasets = []
for row in table.find_all("tr")[1:]:
    print(row)
    dataset = zip(headings, (print(td.get_text()) for td in row.find_all("td")))
    datasets.append(dataset)

print (datasets)

# with open("goals.txt",'w',encoding = 'utf-8') as f:
#     f.write("my first file\n")

