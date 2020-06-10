# WebDriver中的常用方法
# click(): 单级元素
# send_keys(): 模拟按键输入
# clear(): 清除文本
# from selenium import webdriver
# driver = webdriver.Chrome()
# test_url = "http://www.baidu.com"
# driver.get(test_url)

# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

# submit():提交表单
# search_text = driver.find_element_by_id('kw')
# search_text.send_keys('selenium')
# search_text.submit()

# size：返回元素尺寸
# text：获取元素文本
# get_attribute(name): 获取属性值
# is_displayed(): 设置该元素是否用户可见

from selenium import webdriver
driver = webdriver.Chrome()
testurl = 'http://www.baidu.com'
driver.get(testurl)
# 获取搜索框的尺寸
size = driver.find_element_by_id('kw').size
print("搜索框的尺寸为%s" %size)

# 返回百度页面底部备案信息
text = driver.find_element_by_css_selector("div#s-bottom-layer-right").text
print(text)

# 返回元素的属性值，可以是id,name,type或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('autocomplete')
print(attribute)

# 返回元素的结果是否可见，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)