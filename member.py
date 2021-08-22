#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://codelearn.io/sharing/thu-thap-du-lieu-trang-tin-tuc-bat-ky-voi-5-dong-code
# https://newspaper.readthedocs.io/en/latest/



import requests
import newspaper
from newspaper import Article

rq = requests.Session()


def login(email,passwd):
    global rq
    link = "https://httpgroup.vn/ajax/?method=loginquery&email={0}&password={1}".format(email,passwd)
    data = rq.get(link)
    return(data)



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

    title = "TT "+title 
    link = "https://httpgroup.vn/dang-bai-viet.dangtinf"
    files = {
        "ten": (None,title),
        "danhmuc": (None,"0005"),
        "noidung": (None,noidung),
        "method": (None, "question")
            }
    res = rq.post(link, files = files)
    return(res, title)


email = passwd = "xxm93396@cuoly.com"
login(email,passwd)

listtus = listBaiViet("https://dantri.com.vn/")
print(" > Số bài viết: {0}".format(len(listtus)))

count = 0 
for i in listtus:
    count = count + 1
    print(count,dangtin(i))
