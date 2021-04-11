import selenium
from libs.crawler import crawl

url = 'https://www.instagram.com/kyungbuktravel/'

pageString = crawl(url)

print(pageString)

