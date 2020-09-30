from plyer import notification
import requests
import re
from time import sleep
import os

url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=11444a78f247489a881fe41fa6a39c16'

response = requests.get(url)
raw_text = response.json()

# print(raw_text)
# print(raw_text['totalResults'])
no = 0
for i in range(10):
	if raw_text['status'] == "ok":
		print("+++++++++++++++++++++++ News No. "+str(no+1)+" +++++++++++++++++++++++")
		articles = raw_text['articles']
		article = articles[no]
		source = article['source']
		# print(article.keys())
		if str(source) == "None":
			print("The Source of this news is Unknown.")
		else:
			print("The Source of this news is "+str(source['name'])+".")
		author = str(article['author'])
		if author == "None":
			print("The Author of this News is Unknown.")
		else:
			print("The Author of this News is "+str(article['author'])+".")
		title = article['title']
		print("The title of this News is ", end="")
		a = 0
		for i in range(len(title)):
			t =  title[a]
			if t==":":
				break
			print(t, end="")
			a = a+1
		print(".\n\nDescription:")
		print(str(article['description'])+".\n")
		con = article['content']
		if con != None:
			con = re.compile(r'<[^>]+>').sub('', con)
			con = con.replace('"', '')
		# elif con == "None":
		# 	continue
		else:
			pass
		print("Content:")
		print(con)
		time = article['publishedAt']
		print("This Article was Published on "+str(time[0:9]))
		print('\n\n')
		pwd = os.getcwd()
		des = str(article['description'])
		notification.notify(
			title = str(no+1)+'. Top News',
			message = des[0:225],
			app_icon = os.getcwd()+"\\news.ico",
			timeout = 5
		)
		sleep(6)
		no = no + 1
	else:
		print("Please Check Your Internet Connection!!!")
		exit()
