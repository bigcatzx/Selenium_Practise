from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(5)
# sleep()可以根据实际网络速度进行调整，若sleep时间太短可能导致拉取页面文本元素失败的场景

# 定位一组元素
texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

print(len(texts))

for t in texts:
    print(t.text)

