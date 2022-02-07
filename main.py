# Copyright @ Ali Vorobiev (https://github.com/avcomps).

# Modules & libraries.
import requests as rq
from PIL import Image, ImageDraw
# from icrawler.examples import GoogleImageCrawler

image_final_NFT = Image.new("RGB", (160, 160))
    shape = [(0, 0), (w, h)]
    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, fill ="white")

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
    image_segment_h : Image
    global image_final_NFT
    drawGoalImage()
    for i in range(28) : 
        for j in range(28) : 
            if j == 0 : 
                # if is first draw, append just one initial white square to newly created horizontal segment
                image_segment_h = drawWhiteSquare()
            else : 
                # if isn't first draw, concat new goal-image or white-empty square to previous segment, until arrives 28 shapes (28 * 160 = 4480px.)
                image_segment_h = get_concat_h(image_segment_h, drawWhiteSquare())
                
        # append new full-completed horizontal segment to final NFT image
        image_final_NFT = get_concat_v(image_final_NFT, image_segment_h)

    image_final_NFT.save("./final_NFT.jpg")
    print("finished!")


def drawGoalImage() : 
    pass

def drawWhiteSquare() : 
    w, h = 160, 160
    shape = [(0, 0), (w, h)]
    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, fill ="white")
    return img

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