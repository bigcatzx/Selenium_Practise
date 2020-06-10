# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# element = WebDriverWait(driver, 5, 0.5).until(
#     EC.visibility_of_element_located((By.ID, "kw"))
# )
#
# element.send_keys('selenium')

from time import sleep, ctime
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())

driver.quit()