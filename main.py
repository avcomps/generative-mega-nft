# Copyright @ Ali Vorobiev (https://github.com/avcomps).

# Modules & libraries.
import requests as rq
import cv2 as cv
import logging

# Procedures & functions.

def main() : 
    # Search for all images according to number of Ronaldo's goals: 803 scored.
    searchImage()
    downloadImage()
    imageTreatment()

    url = "https://www.transfermarkt.com/cristiano-ronaldo/alletore/spieler/8198/plus/0?saison=&verein=&liga=&wettbewerb=&pos=&minute=&pos=&torart=&stand="
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
    response = rq.get(url, headers = headers).text
    print(response)

def getImage() : 
    pass


# Main of the program.

if __name__ == "__main__" : 
    try : 
        main()
    except(KeyboardInterrupt) :
        print("\n") 
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.error("Script finished by keyboard interrupt")
