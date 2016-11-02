# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import xlwt
import os

def gs(username, password, dirname):

	headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Connection':'keep-alive',
		'Host':'gsdb.bjtu.edu.cn',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
	}
	login_url = 'https://gsdb.bjtu.edu.cn/client/login/'
	score_url = 'https://gsdb.bjtu.edu.cn/score/history/'
	table_head = ['课程名','教师','学期','课程属性','学分','分数']
	table_index = [1, 3, 4, 7, 8, 10]

	session = requests.Session()
	session.post(login_url, {'u':username, 'p': password,}, headers=headers)
	resp = session.get(score_url) 

	soup = BeautifulSoup(resp.text, 'html.parser')

	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet(username)

	for i in range(6):
		sheet.write(0,i,table_head[i])

	row = 1
	for tr in soup.find_all('tr'):
		l = [td.text.strip() for td in tr.find_all('td')]
		for i in range(6):
			sheet.write(row, i, l[table_index[i]])
		row += 1

		_,course_name,_,teacher,term,_,_,porper,credit,_,score,_ = l
		print('course_name :',course_name)
		print('teacher : ',teacher)
		print('term : ',term)
		print('porper : ',porper)
		print('credit : ',credit)
		print('score : ',score)
		print('-' * 50)

	if not os.path.exists(dirname):
		os.mkdir(dirname)
	workbook.save(dirname + username + '.xls')
	print('--------Finished--------')




if __name__ == '__main__':
	dirname = 'C:/Users/sun/Desktop/'
	username = '********'
	password = '--------'
	gs(username, password, dirname)






