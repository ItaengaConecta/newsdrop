# News API and Crawler configs
# https://newsapi.org
import re
import time

# Default configuration
urls = []
urlNews = 'http://newsapi.org/v2/top-headlines?'
apiKey = '' # Your key for access APINews
country = 'br'


def setConfig(**args):
    """
        Define parametersconfigurations.
        urls - url
        urlNews - url for news
        apiKey - key for acces api
        country - place of news
        Format:
                setConfig(urlNews=<url>, apiKey=<key>, country=<country news>)
                Country news -> br, us, etc
    """

    urlNews = args['urlNews']
    apiKey = args['apiKey']
    country = args['country']
