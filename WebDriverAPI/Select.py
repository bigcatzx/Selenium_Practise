# 下拉框处理
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://test.saas.yidianlife.cn/")
driver.get("http://www.baidu.com")

# driver.find_element_by_name('username').send_keys('hzx')
# driver.find_element_by_name('password').send_keys('111111')
# sleep(0.5)
# driver.find_element_by_class_name("el-button").click()

# 打开搜索设置
above = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_class_name('setpref').click()
sleep(1)
driver.find_element_by_xpath('//li[@data-tabid="advanced"]').click()

# 获取时间下拉框
sel = driver.find_element_by_class_name('c-select-selection')

Select(sel).select_by_value('20')
sleep(2)

Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

Select(sel).select_by_index(0)
sleep(2)

driver.quit()
