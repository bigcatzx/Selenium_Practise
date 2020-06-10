# 设置浏览器窗口大小
from selenium import webdriver
driver = webdriver.Chrome()

# driver.get("http://www.baidu.com")
# 参数数字为像素
# print("设置浏览器宽480、高800")
# driver.set_window_size(480, 800)
#设置全屏
# print("设置为全屏")
# driver.maximize_window()
# driver.quit()

# 访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" %first_url)
driver.get(first_url)

# 访问新闻页
sec_url = 'http://news.baidu.com'
print("now access %s" %sec_url)
driver.get(sec_url)

# 返回后退到百度首页
print("back to %s" %first_url)
driver.back()

# 前进到新闻页面
print("forward to %s" %sec_url)
driver.forward()

# 刷新当前页
print("Refresh it!")
driver.refresh()

driver.quit()