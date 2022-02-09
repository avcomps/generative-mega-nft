# Copyright @ Ali Vorobiev (https://github.com/avcomps).

import requests as rq
from PIL import Image, ImageDraw
import random

def draw_white_square() :
    w, h = 160, 160
    shape = [(0, 0), (w, h)]
    img = Image.new("RGB", (w, h))
    ImageDraw.Draw(img).rectangle(shape, fill=("#%06x" % random.randint(0, 0xFFFFFF)))

    return img

def draw_goal_image() : 
    pass

def concatenate_h(im1, im2) :
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))

    return dst

def concatenate_v(im1, im2) :
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))

    return dst

def crawl_images() :
    pass

def create_NFT() :
    # First, create horizontal segment by repeating white-squares 28 times
    image_segment_h = draw_white_square()
    for x in range(27) : 
        image_segment_h = concatenate_h(draw_white_square(), image_segment_h)

    # Secondly, repeat horizontal segment vertically another 28 times
    image_final_NFT = image_segment_h    
    for y in range(27) : 
        image_final_NFT = concatenate_v(image_segment_h, image_final_NFT)   

    image_final_NFT.save("./example.jpg")
    print("------------------- Finished !!! --------------------------")


def main():
    first_segment = draw_white_square()
    for y in range(27) :
        if (y == 0) :
            for x in range(27) :
                if (x == 0) :
                    first_square = draw_white_square()
                first_square = concatenate_h(first_square, draw_white_square())
            first_segment = first_square
        else :
            for x in range(27) :
                if (x == 0) :
                    first_square = draw_white_square()
                first_square = concatenate_h(first_square, draw_white_square())
            first_segment = concatenate_v(first_segment, first_square)
    
    first_segment.save("./example.jpg")

if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt):
        print("\nERROR: KeyboardInterrupt")
