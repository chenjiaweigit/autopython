# coding: utf-8
import time
import os
import shutil
from PIL import Image, ImageColor
import uiautomator2 as ut2
# import matplotlib.pyplot as plt
d = ut2.connect()

def appscreenshot():  # 截图
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(timestamp)
    name = timestamp + ".jpg"
    print(name)
    d.screenshot(name)
    file = r"E://banben"
    if os.path.exists(name):
        print(1)
        if os.path.isdir(file):
            pass
        else:
            os.mkdir(file)
            pass
        shutil.copy(name, file)
    else:
        print(2)
        pass
    l = file + "/" + timestamp + ".jpg"
    print(l)
    if os.path.exists(l):
        print(1)
        if os.path.exists(name):
            os.remove(name)
    else:
        print(2)
        pass

def find():
    import aircv as ac
    imsrc = ac.imread(r'E:\banben\20180109153426.jpg')
    ims = ac.imread(r'E:\banben\jietu.jpg')
    result = ac.find_template(imsrc, ims)
    print(result)
    if result == None:
        return False
    elif result['confidence'] < 0.95:
        return False
    else:
        location = result['result']
        return location


if __name__ == '__main__':
    im_path = r'E:\banben\20180109153426.jpg'
    im = Image.open(im_path)
    # width, height = im.size
    # # 宽高
    # a,b = width/4, height/4
    # print(a,b)
    # print(im.format, im.format_description)
    # print(im.mode)
    img2 = im.crop(
        (
            302,
            610,
            520,
            900
        )
    )
    img2.save(r'E:\banben\jietu.jpg')
    loca = find()
    if loca:
        d.click(loca[0], loca[1])
    else:
        print
        "未找到"




    # appscreenshot()
    # import math
    # import operator
    # from functools import reduce
    #
    # image1 = Image.open(r'E:\banben\jietu.jpg')
    # image3 = Image.open(r'E:\jietu\jietu_rupinyinliao.jpg')
    # # 把图像对象转换为直方图数据，存在list h1、h2 中
    # h1 = image1.histogram()
    # h2 = image3.histogram()
    # result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    # print(result)
    # f = r'E:\jietu\jietu_rupinyinliao.jpg'

