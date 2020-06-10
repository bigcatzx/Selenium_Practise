# 鼠标操作
# ActionChains类中提供了鼠标操作的常用方法：
# perform(): 执行ActionChains类存储的所有行为
# context_click(): 右击
# double_click(): 双击
# drag_and_drop(): 拖动
# move_to_element(): 鼠标悬停

# 鼠标悬停
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# 定位到要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()