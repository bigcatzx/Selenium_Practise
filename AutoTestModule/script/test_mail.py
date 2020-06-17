from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.126.com")

# 登录
sleep(2)
email_frame = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
driver.switch_to.frame(email_frame)
driver.find_element_by_name('email').send_keys("username")
driver.find_element_by_name('password').send_keys("password")
driver.find_element_by_id('dologin').click()

sleep(5)

#退出
driver.find_element_by_link_text("退出").click()

driver.quit()
