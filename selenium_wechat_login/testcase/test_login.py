import pytest
from selenium_wechat_login.page.main_page import MainPage


class TestLogin:
    def test_login(self,get_chromedriver,get_chromedriver_debug):
        login = MainPage(get_chromedriver).goto_login()
        login.login(get_chromedriver_debug)


if __name__ == '__main__':
    pytest.main(["test_login.py"])
