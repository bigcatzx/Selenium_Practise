from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800, 600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

sleep(1)

# 通过JS设置浏览器的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
