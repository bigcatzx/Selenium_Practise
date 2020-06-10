from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获取所有Cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

#添加Cookie信息