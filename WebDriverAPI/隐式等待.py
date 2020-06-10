from time import ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# 设置隐式等待为10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()