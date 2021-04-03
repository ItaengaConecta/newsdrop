# API key e url de acesso a API de noticias
# www
import config
import requests
import json

# Uso: config.config['APIKey'] -> guarda a chave de acesso a plataforma de noticias
"""
Módulo config.py

config = {'APIKey':'',
        'url':''}

"""
url = 'https://newsapi.org/v2/everything'

response = requests.get(url+'?q=brasil&language=pt&'+'apiKey='+config.config['APIKey'])
dat = json.loads(response.text)
print(response)
print([ i for i in map( lambda n: n['title'], dat['articles'][:2])][0:])
print(response.json)

#print(response.text)
#with open('news-pt.json', 'w') as f:
#    f.write(response.text)
#    f.close()
