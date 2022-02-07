# Copyright @ Ali Vorobiev (https://github.com/avcomps).

# Modules & libraries.
import requests as rq
import logging
from icrawler import GoogleImageCrawler

def main() : 
    # goal example : ronaldo goal vs moreirense 2:0 solo run 2002/03
    google_crawler = GoogleImageCrawler('./images/')
    google_crawler.crawl(keyword='ronaldo goal vs moreirense 2:0 solo run 2002/03', offset=0, max_num=1, date_min=None, date_max=None,
        feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=4, min_size=(400,400), max_size=None)










# Main of the program.
if __name__ == "__main__" : 
    try : 
        main()
    except(KeyboardInterrupt) :
        print("\n") 
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.error("Script finished by keyboard interrupt")
