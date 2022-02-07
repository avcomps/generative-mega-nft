# Copyright @ Ali Vorobiev (https://github.com/avcomps).

import requests as rq
from PIL import Image, ImageDraw

image_final_NFT = Image.new("RGB", (160, 160))

def draw_white_square():
    w, h = 160, 160
    shape = [(0, 0), (w, h)]
    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, fill="white")
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


def crawl_images():
    print


def create_NFT():
    global image_final_NFT
    image_segment_h = Image.new("RGB", (160, 160))

    for i in range(28):
        for j in range(28):
            if j == 0:
                image_segment_h = draw_white_square()
            else:
                image_segment_h = get_concat_h(
                    image_segment_h, draw_white_square())

        image_final_NFT = get_concat_v(image_final_NFT, image_segment_h)

    image_final_NFT.save("./final_NFT.jpg")
    print("finished!")


def main():
    crawl_images()
    create_NFT()


if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt):
        print("\nERROR: KeyboardInterrupt")
