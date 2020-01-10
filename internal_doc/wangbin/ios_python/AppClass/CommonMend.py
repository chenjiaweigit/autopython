# -*- coding: UTF-8 -*-


import random
"""用于随机生成汉字"""
def randomChinese():
    str2 = ""
    for j in range(0, 10):
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = (head << 8) | (body << 4) | tail
        str1 = "%x" % val
        str2 += str1.decode('hex').decode('gb2312').encode("utf-8")
    return str2

ll = randomChinese()
print(ll)