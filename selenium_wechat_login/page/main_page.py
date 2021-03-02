from selenium import webdriver
from selenium.webdriver.common.by import By
from .register_page import RegisterPage
from .login_page import LoginPage

class MainPage():
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        # self.driver.get("https://work.weixin.qq.com/")
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.XPATH,'//*[@class="index_head_info_pCDownloadBtn"]').click()
        return RegisterPage(self.driver)        # 将driver传给注册页面。return 是为了链式调用

    def goto_login(self):
        self.driver.find_element(By.XPATH, '//*[@class="index_top_operation_loginBtn"]').click()
        return LoginPage(self.driver)