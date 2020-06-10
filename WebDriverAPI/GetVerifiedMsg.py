from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print('Before search---------------')

# 打印当前页的title
title = driver.title
print("title:"+ title)

# 打印当前页的url
url = driver.current_url
print("current_url:"+ url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

print('After search===============')

# 再次打印当前页面的title
title = driver.title
print("title:"+title)

now_url = driver.current_url
print("Now url:"+now_url)

# 获取搜索结果条数
num = driver.find_element_by_class_name('nums_text').text
print("result:"+num)

driver.quit()