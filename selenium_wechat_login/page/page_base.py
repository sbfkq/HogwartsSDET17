from selenium import webdriver

class PageBase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)