import requests

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content