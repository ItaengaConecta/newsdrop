import urllib.request as req
import newsapi.config

url = ('http://newsapi.org/v2/top-headlines?'
       'country='+newsapi.config.country+'&'
       'apiKey='+newsapi.config.apiKey)
data = req.urlopen(url).read().decode()
print(data)
n = 0
with open('/tmp/news.json', 'w') as fl:
    fl.write(data)
    fl.close()
    
import json
dw = json.loads(data)
text = ''
size = len(dw['articles'])
for i in dw['articles']:
    print('\n\n {} \n{}\n{}'.format( i['title'],i['description'], i['url']))
    #print(i)
    n += 1
    text += '\n\n'+i['title']+'\n'+repr(i['description']) + '\n' + i['url']
    if n== size:
        break
with open('/tmp/news-br.txt', 'w') as fl:
    fl.write(text)
    fl.close()
