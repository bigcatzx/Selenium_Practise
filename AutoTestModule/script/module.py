class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """ 登录 """
        email_frame = self.driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
        self.driver.switch_to.frame(email_frame)
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('dologin').click()

    def logout(self):
        """ 退出 """
        self.driver.find_element_by_link_text("退出").click()