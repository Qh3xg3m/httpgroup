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

def findCode(page):
	global rq
	match = "duyetbai\\('(.*)', this\\);"
	link = "https://httpgroup.vn/adminweb/?op=dangtin&tukhoa=TT&page={0}".format(page)
	text = rq.get(link).text
	listcode = re.findall(match,text)
	return(listcode)


def duyetbai(code):
	tong = 0
	number = rd.randint(1,9)
	tien = str(number)+"000"
	link = "https://httpgroup.vn/adminweb/ajax.php"
	data = {"op":"dangtin","name":"duyetbai","id":code,"value":tien}
	res = rq.post(link,data=data)
	return(code, res, tien)

def main(number):
	email = passwd = "bifilo7611@cytsl.com"
	print(login(email,passwd)," --- Dang nhap thanh cong!")
	print()
	tong = 0
	for page in range(1,number//20 + 2):
		listcode = findCode(page)
		print(" > Page {0} : Co {1} bai viet!".format(page,len(listcode)))
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


number = int(input(" [?] So bai viet: "))
print(main(number))
