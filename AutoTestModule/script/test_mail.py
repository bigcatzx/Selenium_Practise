import time

from selenium import webdriver
from time import sleep
from script.module import Mail
from script.data import user

driver = webdriver.Chrome()
driver.maximize_window()
mail = Mail(driver)
driver.implicitly_wait(20)
for i in user:

    driver.get("http://www.126.com")

    # 调用Mail类并接受driver驱动


    # 登录

    mail.login(i[0], i[1])
    time.sleep(2)



# sleep(2)
# email_frame = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
# driver.switch_to.frame(email_frame)
# driver.find_element_by_name('email').send_keys("hzx4713972")
# driver.find_element_by_name('password').send_keys("HZX-+*zry_")
# driver.find_element_by_id('dologin').click()



# #退出
# mail.logout()
# # driver.find_element_by_link_text("退出").click()
#
# driver.quit()
