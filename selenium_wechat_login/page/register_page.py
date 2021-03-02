


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys("xxxxx")

    def goto_mainpage(self):
        pass