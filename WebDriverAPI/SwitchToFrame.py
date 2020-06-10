from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
sleep(2)

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_id("email").send_keys("username")
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()
