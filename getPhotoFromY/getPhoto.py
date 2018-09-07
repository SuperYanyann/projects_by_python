# -*- coding: UTF-8 -*-
import requests
import os
import re

# get photo from Y,page is the num of page you want
def getphoto(page):
    url = 'https://yande.re/post?page=' + str(page)
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    html1_1 = requests.get(url,headers=header)
    photo_lise = re.findall('<a class="directlink largeimg" href="(.*?)">',html1_1.text)
    numOfPhoto = len(photo_lise)

    for i in range(0,numOfPhoto):
        print i
        image_url = photo_lise[i]
        r = requests.get(image_url)
        binfile = open(str(i)+'jpg',"wb")
        binfile.write(r.content)
        binfile.close()
        print 'finish' + str(i)

if __name__ == '__main__':
    getphoto(1)
