# -*- coding: utf-8 -*-
'''
第一个示例：简单的网页爬虫

爬取豆瓣首页
'''

import urllib.request
import urllib.error as error
import re
#网址
url = "http://www.lakala.com/"
#请求
request = urllib.request.Request(url)
#爬取结果
response = urllib.request.urlopen(request)
data = response.read()
#设置解码方式
data = data.decode('utf-8')
#打印结果
print(data)
print("----------------------------------")
#打印爬取网页的各类信息
print(type(response))
print("----------------------------------")
print(response.geturl())
print("----------------------------------")
print(response.info())
print("----------------------------------")
print(response.getcode())
print("----------------------------------")
imgre = re.compile('<img src=\"(.+?)\"')
imglist = imgre.findall(data)  # re.findall() 方法读取html 中包含 imgre（正则表达式的数据)
# 把筛选的图片地址通过for循环遍历并保存到本地
# 核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
x = 0
dirpath = 'D:/test/'
for imgurl in imglist:
    pattern = re.compile(r'^http://.*.jpg$')
    if pattern.match(imgurl):
        try:
            image_data = urllib.request.urlopen(imgurl).read()
            image_path = dirpath + str(x) + '.png'
            x += 1
            print(image_path)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_data)
            image_file.close()
        except error.URLError as e:
            print('Download failed')