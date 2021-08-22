# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-


# https://www.krazyprogrammer.com/2020/11/create-window-login-form-in-python.html
# https://ichi.pro/vi/tao-ung-dung-may-tinh-bang-tkinter-huong-dan-day-du-ve-tkinter-270848488687640


from tkinter.font import Font
from tkinter import *
import newspaper
from newspaper import Article
import requests
import json
from time import sleep

rq = requests.Session()



#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("Điền thiếu kìa!")
    else:
        link = "https://httpgroup.vn/ajax/?method=loginquery&email={0}&password={1}".format(uname,pwd)
        data = rq.get(link).json()["status"]
        if data == "success":
            login_screen.destroy()
            inputUrl()
            # listBaiViet()
        else:
            message.set("Sai rùi :(")

def howto():
    howto = """ * Cách hoạt động của tool nè:
- Xác thực tài khoản người dùng
- Lấy bài viết mới trên trang báo nào đó
- Đăng bài viết mới lên httpgroup"""
    text = StringVar()
    label = Message(login_screen, textvariable=text, width = 5000, font=("Arial Bold", 20)).place(x=50,y=180)
    text.set(howto)
    return(label)

#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.resizable(0, 0)

    #Setting title of screen
    login_screen.title("Tool auto đăng bài trên httpgroup - Made by NguyenQuy with love <3")
    #setting height and width of screen
    login_screen.geometry("600x500")
    #declaring variable
    global message
    global username
    global password
    global howto

    # giai thich cach hoat dong
    howto()


    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Đăng nhập đi, đọc cái gì?", bg="orange",fg="white",font=("Arial", 10)).pack()
    #Username Label
    Label(login_screen, text="Username ",font=("Arial Bold", 20)).place(x=100,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username, font=("Arial Bold", 12)).place(x=260,y=50)
    #Password Label
    Label(login_screen, text="Password ",font=("Arial Bold", 20)).place(x=100,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*", font=("Arial Bold", 12)).place(x=260,y=90)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,font=("Arial Bold", 10),fg="red").place(x=300,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login,font=("Arial Bold", 10)).place(x=300,y=145)

    login_screen.mainloop()


def inputUrl():
    global linkinput
    global sitebao
    global messageLink

    sitebao = Tk()
    sitebao.resizable(0,0)
    sitebao.title("Tool auto đăng bài trên httpgroup - Made by NguyenQuy with love <3")
    sitebao.geometry("700x300")

    linkinput = StringVar()
    messageLink = StringVar()
    baodientu = "VD: https://dantri.com.vn, https://vnexpress.net, https://vietnamnet.vn, etc..."
    Label(sitebao, text="Url trang báo điện tử ",font=("Arial Bold", 20)).place(x=200,y=40)
    Label(sitebao, text=baodientu,font=("Arial", 15)).place(x=30,y=80)
    Entry(sitebao, textvariable=linkinput, font=("Arial Bold", 12)).place(x=240,y=125)
    Label(sitebao, text="",textvariable=messageLink,font=("Arial Bold", 10),fg="red").place(x=280,y=150)
    Button(sitebao, text="Ok", width=10, height=1, bg="orange",command=listBaiViet,font=("Arial Bold", 10)).place(x=280,y=180)
    sitebao.mainloop()


def listBaiViet():
    global linkinput
    global listlink
    url = linkinput.get()
    if url == "" or "http" not in url:
        messageLink.set("Đọc kĩ vào :>")
    else:
        listlink = []
        baodientu = newspaper.build(url)
        for article in baodientu.articles:
            listlink.append(article.url)
        messageLink.set("Đang lấy thông tin bài viết mới")
        sitebao.destroy()
        return(listlink)


def dangtin(link):
    global rq
    global count 
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
    title = "- {0}".format(title)
    return(title)


Loginform()
# inputUrl()


dangbai = Tk()
dangbai.resizable(0,0)
dangbai.title("Tool auto đăng bài trên httpgroup - Made by NguyenQuy with love <3")
dangbai.geometry("700x400")
scrollbar = Scrollbar(dangbai)
scrollbar.pack(side = RIGHT, fill = Y)
mylist = Listbox(dangbai, yscrollcommand = scrollbar.set)



link = StringVar()
# Label(dangbai, text="Đang đăng bài lên httpgroup...",font=("Arial Bold", 20)).place(x=150,y=0)

def hienthi():
    global listlink
    global dangbai
    count = 0
    # try:
    #     linkbaiviet = listlink[count]
    #     tieude = dangtin(linkbaiviet)
    #     tile_frame = Label(text=tieude,font=("Arial", 15),fg="green")
    # except:
    #     if count > len(listlink):
    #         tieude = "Xong rùi đóo ^^"
    #         tile_frame = Label(text=tieude,font=("Arial", 15),fg="red")           
    #     else:
    #         tieude = "Có lỗi xảy ra, contact admin plss!"
    #         tile_frame = Label(text=tieude,font=("Arial", 15),fg="red")
    # tile_frame = Label(text=tieude,font=("Arial", 15),fg="green")
    linkbaiviet = listlink[count]
    tieude = dangtin(linkbaiviet)
    tile_frame = Label(text=tieude,font=("Arial", 15),fg="green")
    tile_frame.pack()
    dangbai.after(1000,hienthi)
    listlink.remove(linkbaiviet)
    count = count + 1

dangbai.after(0,hienthi)
dangbai.mainloop()




