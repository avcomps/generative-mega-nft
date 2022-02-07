# Copyright @ Ali Vorobiev (https://github.com/avcomps).

# Modules & libraries.
import requests as rq
from PIL import Image, ImageDraw
# from icrawler.examples import GoogleImageCrawler

image_final_NFT = Image.new("RGB", (0, 0))

def main() : 
    crawlImages()
    createNFT()

def crawlImages() : 
    # goal example : ronaldo goal vs moreirense 2:0 solo run 2002/03
    # google_crawler = GoogleImageCrawler('./images/')
    # google_crawler.crawl(keyword='ronaldo goal vs moreirense 2:0 solo run 2002/03', offset=0, max_num=1, date_min=None, date_max=None,
    #     feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=4, min_size=(400,400), max_size=None)
    pass

def createNFT() : 
    drawGoalImage()
    for i in range(803) : 
        if i == 0 : 
            get_concat_h(image_final_NFT, drawWhiteSquare())
        else : 
            # if not first draw, concat new goal image or white-empty square
            pass


# ------------------------------------------------------

def drawGoalImage() : 
    pass

def drawWhiteSquare() : 
    w, h = 160, 160
    shape = [(0, 0), (w, h)]
    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, fill ="white")
    # img.save("./example.jpg")
    return img1

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

# get_concat_h(im1, im1).save('data/dst/pillow_concat_h.jpg')
# get_concat_v(im1, im1).save('data/dst/pillow_concat_v.jpg')


# Main of the program.
if __name__ == "__main__" : 
    try : 
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")