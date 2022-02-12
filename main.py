# Copyright @ Ali Vorobiev (https://github.com/avcomps).
#!/usr/bin/env python3

import glob
from PIL import Image, ImageDraw
import requests as rq
import random
import json
import re
import urllib.request

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

def draw_white_square() :
    img_weigth, img_height = 160, 160; shape = [(0, 0), (img_weigth, img_height)]
    img_res = Image.new('RGB', (img_weigth, img_height))
    ImageDraw.Draw(img_res).rectangle(shape, fill=("#%06x" % random.randint(0, 0xFFFFFF)))
    
    return img_res

def draw_goal_image(img_goal:Image) :
    bias = 80
    img_goal = img_goal.crop(((img_goal.width - bias) // 2, (img_goal.height - bias) // 2, 
        (img_goal.width + bias) // 2, (img_goal.height + bias) // 2))
    img_goal.thumbnail((160, 160))

    return img_goal

def crawl_goal_images() :
    with open('./goals.json', 'r') as file_goals :
        goals = json.load(file_goals)
    
    i = 0
    for goal in goals :
        if "Season" in str(goal[0]) :
            del goals[i]; i += 1
    
    i = 0
    for goal in goals :
        url = "https://www.google.com/search?q=" + "cristiano+ronaldo+goal+vs+" + str(goal[6]) + "+" + str(goal[10]) + "+HD&rlz=1C1ONGR_esES976ES976&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6zq2ThfT1AhUQtaQKHSMEAwMQ_AUoAXoECAIQAw&biw=1536&bih=746&dpr=1.25"
        print(url)
        links = re.findall("https:\/\/encrypted.+[^\"]", rq.get(url=url).text)
        url_goals_img = str(links[0][:121])
        print(url_goals_img); print(i); i += 1
        urllib.request.urlretrieve(url_goals_img, "./goals/" + str(i) + "_" + str(goal[6]) + "_" + str(goal[10]) + ".jpg")
        if i == 5 :
            return

def draw_nft() :
    list_imgs = [Image.open(item) for i in [glob.glob('./goals/*.%s' % ext) for ext in ["jpg","png"]] for item in i]
    current_pos = 0
    first_segment : Image
    for y in range(25) :
        if (y == 0) :
            for x in range(27) :
                current_pos += 1
                if (x == 0) :
                    first_square = draw_goal_image(list_imgs[current_pos])
                first_square = concatenate_h(first_square, draw_goal_image(list_imgs[current_pos]))
            first_segment = first_square
        else :
            for x in range(27) :
                current_pos += 1
                if (x == 0) :
                    first_square = draw_goal_image(list_imgs[current_pos])
                first_square = concatenate_h(first_square, draw_goal_image(list_imgs[current_pos]))
            first_segment = concatenate_v(first_segment, first_square)
    
    first_segment.save("./example.jpg", "JPEG")


def main() :
    crawl_goal_images()
    draw_nft()

if __name__ == "__main__":
    try :
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")
