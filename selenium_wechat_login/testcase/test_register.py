import pytest
from selenium import webdriver

from selenium_wechat_login.page.main_page import MainPage
from time import sleep


class TestRegiester:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def teardown_class(self):
        self.driver.quit()

    def test_register(self):
        main = MainPage(self.driver)
        main.goto_register().register()
        sleep(5)


if __name__ == '__main__':
    pytest.main(['test_register.py'])