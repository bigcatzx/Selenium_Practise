from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

# 打开搜索设置
above = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_link_text("搜索设置").click()

sleep(2)

driver.find_element_by_class_name("prefpanelgo").click()

# 获取警告框位置
alert = driver.switch_to.alert

# 获取警告框提示信息
alert_text = alert.text
print(alert_text)

# 接收警告框
alert.accept()

driver.quit()


