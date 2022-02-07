# Copyright @ Ali Vorobiev (https://github.com/avcomps).

import requests as rq
from bs4 import BeautifulSoup
from icrawler.examples import GoogleImageCrawler

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
# goal example : ronaldo goal vs moreirense 2:0 solo run 2002/03

google_crawler = GoogleImageCrawler('./images/')
google_crawler.crawl(keyword='ronaldo goal vs moreirense 2:0 solo run 2002/03', offset=0, max_num=1, date_min=None, date_max=None,
    feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=4, min_size=(400,400), max_size=None)



