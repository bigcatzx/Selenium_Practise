from selenium import webdriver
# 调用Keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 在输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")

# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

# 输入组合键Ctrl+A，全选输入框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# 输入组合键Ctrl+X，剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

# 粘贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

# 用回车键代替单机
driver.find_element_by_id("su").send_keys(Keys.ENTER)

driver.quit()