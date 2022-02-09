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

def draw_nft() :
    first_segment = draw_white_square()
    for y in range(30) :
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


def main():
    draw_nft()

if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt):
        print("\nERROR: KeyboardInterrupt")
