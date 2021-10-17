#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import newspaper
from newspaper import Article
import os
import json
from time import sleep

rq = requests.Session()

red = "\033[1;31;40m"
green = "\033[1;32;40m"
white = "\033[1;37;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
rednhay = "\033[5;31;40m"
kieu1 = "\033[1;33;40m"
kieu2 = "\033[1;35;40m"


print("{0}{1}Tool auto đăng bài lên httpgroup".format(" "*10,green))
print()
print("{0}{1}Made by NguyenQuy with luv {2}<3 <3 <3".format(" "*30,"\033[3;32;40m",red))
print("{0}{1}Last update: 18/10/2021".format(" "*30,"\033[3;32;40m"))


def login(email,passwd):
    global rq
    link = "https://httpgroup.vn/ajax/?method=loginquery&email={0}&password={1}".format(email,passwd)
    data = rq.get(link).json()["status"]
    return(data=="success")



def listBaiViet(link):
    listlink = []
    cnn_paper = newspaper.build(link)
    for article in cnn_paper.articles:
        listlink.append(article.url)
    return(listlink)
    

def dangtin(link):
    global rq

    article = Article(link)
    article.download()
    article.parse()
    title = article.title
    noidung = article.text
    link = "https://httpgroup.vn/dang-bai-viet.dangtinf"
    files = {
        "ten": (None,title),
        "danhmuc": (None,"0005"),
        "noidung": (None,noidung),
        "method": (None, "question")
            }
    res = rq.post(link, files = files)
    return(title)


def config():
	f = open("config.json")
	data = json.load(f)
	f.close()
	return(data)
	

data = config()
email = data["username"]
passwd = data["password"]
print()
for i in data:
    if "url" in i:
        print("",i[-1],".",data[i])
print()
choose = int(input(" {0}[?] {1}Chọn báo điện tử: ".format(red,green)))
linkbao = data["url{0}".format(choose)]
print(" {0}> Báo điện tử : {1}{2}".format(white,blue,linkbao))
print()
print(" {0}> Email: {1}{2}".format(white,blue,email))

try:
	if login(email,passwd):
		print(" {0}[*] Đăng nhập thành công ^^".format(green))
		print()
	else:
		print(" {0}[!] {1}Kiểm tra lại thông tin đăng nhập plss :>".format(rednhay,white))
		sleep(3)
		exit()
except:
	print(" {0}[!] Error!".format(red))
	sleep(3)
	exit()

listtus = listBaiViet(linkbao)
print(" {0}[*] Số bài viết trên {1}{2}: {3}{4}".format(white,blue,linkbao,red,len(listtus)))
if len(listtus) == 0:
	print(" {0}[*] Chưa có bài viết mới trên {1}{2}".format(white,blue,linkbao))
	print(" {0}[*] Vui lòng chọn báo điện tử khác hoặc quay lại sau ít phút {1}<3".format(white,red))
	exit()
else:
	print(" {0}[*] Đang đăng bài viết lên httpgroup".format(white))
	print()

count = 0 
for i in listtus:
    count = count + 1
    if count % 2 == 0:
    	style = kieu1
    else: 
    	style = kieu2
    print(" {0}{1}. {2}".format(style,count,dangtin(i)))

