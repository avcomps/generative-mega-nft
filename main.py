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

def concatenate_h(img_left, img_right) :
    img_new = Image.new('RGB', (img_left.width + img_right.width, img_left.height))
    img_new.paste(img_left, (0, 0))
    img_new.paste(img_right, (img_left.width, 0))
    return img_new

def concatenate_v(img_left, img_right) :
    img_new = Image.new('RGB', (img_left.width, img_left.height + img_right.height))
    img_new.paste(img_left, (0, 0))
    img_new.paste(img_right, (0, img_left.height))
    return img_new

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
