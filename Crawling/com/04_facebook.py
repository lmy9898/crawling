from selenium import webdriver

rootPath = '..'
driver = webdriver.Chrome(
    executable_path="{}/webdriver/chromedriver".format(rootPath)
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_id("email").send_keys("lmy9898@naver.com")
driver.find_element_by_id("pass").send_keys("lee1710828!")
driver.find_element_by_name('login').click()
