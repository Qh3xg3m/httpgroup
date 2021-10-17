#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import random as rd

rq = requests.Session()


def login(email, passwd):
	global rq
	link = "https://httpgroup.vn/adminweb/?checklogin=1"
	data = {"email":email,"matkhau":passwd}
	res = rq.post(link, data=data)
	return(res)


def duyetbai(code):
	tong = 0
	tien = "1000"
	link = "https://httpgroup.vn/adminweb/ajax.php"
	data = {"op":"dangtin","name":"duyetbai","id":code,"value":"1000"}
	res = rq.post(link,data=data)
	return(code, res, tien)

def main(number):
	email = passwd = "bifilo7611@cytsl.com"
	print(login(email,passwd)," --- Dang nhap thanh cong!")
	print()
	tong = 0
	listcode = number.split(" ")
	count = 0
	tien = 0
	for code in listcode:
		count = count + 1
		data = duyetbai(code)
		print(count,data)
		tien = tien + int(data[2])

		print(" > ",tien)
		tong = tong + tien
		print()
	return(" > Tong so tien thu dc: {0}".format(tong))


number = input(" [?] Bai viet: ")
print(main(number))
