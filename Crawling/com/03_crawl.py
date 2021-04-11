from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver"
)

url = "https://www.instagram.com/explore/tags/발레/"
driver.get(url) # 주소입력하고 enter
sleep(5)
pageString = driver.page_source
print(pageString)

# 인스타 내용 <div class='Nng7C weEfm">
driver.close()
