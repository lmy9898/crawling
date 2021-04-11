from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver"
)

url = "https://www.instagram.com/explore/tags/발레/"

driver.get(url)
#driver.close()
