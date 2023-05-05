from tkinter import *
import requests

window = Tk()
window.title('New App Using API')
window.geometry("900x700")

def getNews():
	url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=9fb7c725870d49cbb75e1a0693dc624a')
	response = requests.get(url).json()
	art = response["articles"]

	res1 = []
	res2 = []
	res3 = []
	res4 = []
	my_news=""
	my_news2=""
	my_news3=""
	my_news4=""

	for i in art:
		res1.append(i["author"])
		res2.append(i["title"])
		res3.append(i["description"])
		res4.append(i["url"])

	for j in range(5):
		my_news=my_news+res1[j]+"\n"
		my_news2=my_news2+res2[j]+"\n"
		my_news3=my_news3+res3[j]+"\n"
		my_news4=my_news4+res4[j]+"\n"

	lb1.config(text=my_news)
	lb2.config(text=my_news2)
	lb3.config(text=my_news3)
	lb4.config(text=my_news4)


	# for i in art:
	# 	print()
	# 	print(i['author'])
	# 	print(i['title'])
	# 	print(i['description'])
	# 	print(i['url'])
	# 	lb1.config(text=i['author'])
	# 	lb2.config(text=i['title'])
	# 	lb3.config(text=i['description'])
	# 	lb4.config(text=i['url'])

	# for i in range(len(results)):
	# 	print(i+1,results[i])

btn1 = Button(window,text='Get News',command=getNews)
btn1.pack()




lb1 = Label(window,text='None')
lb1.pack()

lb2 = Label(window,text='None')
lb2.pack()

lb3 = Label(window,text='None')
lb3.pack()

lb4 = Label(window,text='None')
lb4.pack()

window.mainloop()