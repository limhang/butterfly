import requests
from lxml import etree
import re
import time  
from urllib.request import urlopen, urlretrieve  
import shutil

url_or = 'http://www.sexinsex.net/bbs/forum-321-1.html'
# fileHtml = open('sis_00.html','r').read()
r = requests.get(url_or)

fileHtml = r.text

result = etree.HTML(fileHtml)

alink = result.xpath('//th/span/a//@href')

# thread-2699209-3-19.html
arr = []

for item in alink:
	short = item[15:]
	if (short[0]=='1' and short[1]=='-'):
		url = 'http://www.sexinsex.net/bbs/' + item
		arr.append(url)

# print(alink)

fuck = list(set(arr))
# print(fuck)
for item in fuck:
	print(item)