import requests

NEWS_API_KEY = '671121ad496547308763249441f565e9'
COMPANY_NAME = "Tesla"

def get_headlines(quantity:int):
    n = quantity

    news_params = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME,
        'from': '2025-01-22', #insert day beforebefore
        'to': '2025-01-24', #insert today
        'language': 'en',
        'sortBy': 'relevancy',
        'pageSize': n,
    }

    response = requests.get(url='https://newsapi.org/v2/everything?', params=news_params)
    data = response.json()
    #print(data['articles'])
    for article in data['articles']:
        print(article['description'])

