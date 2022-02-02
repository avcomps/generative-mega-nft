# Copyright @ Ali Vorobiev (https://github.com/avcomps).

# Modules & libraries.
import requests as rq
import cv2 as cv
import logging

# Procedures & functions.

def main() : 
    url = "https://www.transfermarkt.com/cristiano-ronaldo/alletore/spieler/8198/plus/0?saison=2003&verein=&liga=&wettbewerb=&pos=&minute=&pos=&torart=&stand="
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
    response = rq.get(url, headers = headers).text
    print(response)


# Main of the program.

if __name__ == "__main__" : 
    try : 
        main()
    except(KeyboardInterrupt) : 
        print("\nERROR: Script finished by keyboard interrupt")
