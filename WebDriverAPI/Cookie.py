from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获取所有Cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

# 添加Cookie信息
driver.add_cookie({'name':'key-aaaaaaaa', 'value':'value-bbbbbbb'})

# 遍历指定的Cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
