# -*- coidng:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os

def jandan(start_page, end_page, dirname):
	headers = {'content-type': 'application/json',
	           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

	count = 0
	for page in range(start_page, end_page):
		r = requests.get('http://jandan.net/pic/page-'+ str(page) +'#comments', headers = headers)
		soup = BeautifulSoup(r.text, 'html.parser')
		
		for i in soup.select('div.text'):
			try:
				img_url = i.find('p').find('a')['href']
				if not os.path.exists(dirname):
					os.mkdir(dirname)
				filename = dirname + str(count) + img_url[-4:]
				print('wrinting ' + filename)
				with open(filename, 'wb') as f:
					# for chunk in requests.get(img_url, stream = True).iter_content(chunk_size = 1024):
					# 	f.write(chunk)
					img = requests.get(img_url, headers = headers)
					f.write(img.content)
				print('--------success!--------')
				count += 1
			except Exception as e:
				print(e)
				print('-'*50)
				print('continue: ' + str(count))
				continue
		
	print('-----------------Finished------------------------')


if __name__ == '__main__':
	dirname = 'C:/Users/sun/Desktop/jandan/'
	jandan(2158, 2168, dirname)

		





