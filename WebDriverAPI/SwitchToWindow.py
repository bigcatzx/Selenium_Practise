import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.baidu.com")

# 获取百度搜索窗口句柄
search_window = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

# 获得当前所有打开的窗口句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != search_window:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_name("userName").send_keys('hzx')
        driver.find_element_by_name("phone").send_keys('13671953858')
        time.sleep(2)
        driver.close()

driver.switch_to.window(search_window)
print(driver.title)

