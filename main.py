# Copyright @ Ali Vorobiev (https://github.com/avcomps).

#!/usr/bin/env python3

import random, json, re, glob, urllib.request, requests as rq
from PIL import Image, ImageDraw

def concatenate_h(img_left, img_right) :
    img_new = Image.new('RGB', (img_left.width + img_right.width, img_left.height))
    img_new.paste(img_left, (0, 0)); img_new.paste(img_right, (img_left.width, 0))

    return img_new

def concatenate_v(img_left, img_right) :
    img_new = Image.new('RGB', (img_left.width, img_left.height + img_right.height))
    img_new.paste(img_left, (0, 0)); img_new.paste(img_right, (0, img_left.height))

    return img_new

def draw_color_square() :
    img_weigth, img_height = 160, 160; shape = [(0, 0), (img_weigth, img_height)]
    img_res = Image.new('RGB', (img_weigth, img_height))
    ImageDraw.Draw(img_res).rectangle(shape, fill=("#%06x" % random.randint(0xFFFEEE, 0xFFFFFF)))

    return img_res

def draw_goal_image(img_goal:Image) :
    zoom = 160
    img_res = img_goal.crop(((img_goal.width - zoom) // 2, (img_goal.height - zoom) // 2, 
                            (img_goal.width + zoom) // 2, (img_goal.height + zoom) // 2))
    img_res.thumbnail((160, 160))

    return img_res

def crawl_goal_images() :
    with open('./goals.json', 'r') as file_goals : goals = json.load(file_goals)
    i = 0
    for goal in goals :
        if "Season" in str(goal[0]) :
            del goals[i]; i += 1
    i = 0
    for goal in goals :
        url = "https://www.google.com/search?q=" + "cristiano+ronaldo+goal+vs+" + str(goal[6]) + "+" + str(goal[10]) + "+HD&" + """rlz=1C1ONGR_esES976ES976
            &source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6zq2ThfT1AhUQtaQKHSMEAwMQ_AUoAXoECAIQAw&biw=1536&bih=746&dpr=1.25"""
        links = re.findall("https:\/\/encrypted.+[^\"]", rq.get(url=url).text)
        urllib.request.urlretrieve(str(links[0][:121]), "./goals/" + str(i) + "_" + str(goal[6]) + "_" + str(goal[10]) + ".jpg")
        i += 1

def draw_nft() :
    list_imgs = [Image.open(item) for i in [glob.glob('./goals/*.%s' % ext) for ext in ["jpg","png"]] for item in i]
    res = []
    with open('./arrays.txt', 'r') as file_art_pos :
        for line in file_art_pos.readlines() :
            for x in line.splitlines(False) : res.append(x.split(" - "))
        new_res = []
        for pos in res :
            for i in pos :
                if ":" in str(i) :
                    pos_x_from = int(str(i).split(":")[0])
                    pos_x_to = int(str(i).split(":")[1].split(",")[0])
                    pos_y = int(str(i).split(":")[1].split(",")[1])
                    for j in range(pos_x_from, pos_x_to + 1) : new_res.append((j, pos_y))
                else :
                    new_res.append((int(str(i).split(",")[0]), int(str(i).split(",")[1])))
        res = new_res

    first_segment : Image; current_pos_x = 0; current_pos_x_seg = 1; current_pos_y = 1
    for y in range(25) :
        current_pos_x_seg = 0
        if y == 0 :
            for x in range(27) :
                if (current_pos_x_seg, current_pos_y) in res :
                    if x == 0 : first_square = draw_color_square()
                    first_square = concatenate_h(first_square, draw_color_square())
                else :
                    if x == 0 : first_square = draw_goal_image(list_imgs[current_pos_x])
                    first_square = concatenate_h(first_square, draw_goal_image(list_imgs[current_pos_x]))
                    current_pos_x += 1
                current_pos_x_seg += 1
            first_segment = first_square
        else :
            for x in range(27) :
                if (current_pos_x_seg, current_pos_y) in res :
                    if x == 0 : first_square = draw_color_square()
                    first_square = concatenate_h(first_square, draw_color_square())
                else :
                    if x == 0 : first_square = draw_goal_image(list_imgs[current_pos_x])
                    first_square = concatenate_h(first_square, draw_goal_image(list_imgs[current_pos_x]))
                    current_pos_x += 1
                current_pos_x_seg += 1
            first_segment = concatenate_v(first_segment, first_square)
        current_pos_y += 1
    
    first_segment.save("./example.jpg", "JPEG")


def main() :
    crawl_goal_images()
    draw_nft()

if __name__ == "__main__":
    try :
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")
