#9fb7c725870d49cbb75e1a0693dc624a

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=9fb7c725870d49cbb75e1a0693dc624a')
response = requests.get(url).json()
#print(response)

art = response["articles"]
# print(art)

results = []

for i in art:
	print()
	print(i['author'])
	print(i['title'])
	print(i['description'])
	print(i['url'])
	# print(f'''author:{i['author']}
	# 	       title:{i['title']}
	# 	       description:{i['description']}
	# 	       url:{i['url']}
	# 	''')


for i in range(len(results)):
	print(i+1,results[i])
