import json
from time import sleep
from selenium.webdriver.common.by import By

from selenium_wechat_login.page.member_page import MemberPage
from .admin_page import AdminPage


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def scan(self):
        pass

    def login(self,get_chromedriver_debug):
        driver = get_chromedriver_debug
        cookies = driver.get_cookies()
        with open("tmp.text", "w", encoding="utf-8") as f:
            json.dump(cookies, f)
        # print(cookies)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open('tmp.text', 'r', encoding='utf-8') as f:
            cookies = json.load(f)

        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        # sleep(1)

        return AdminPage(self.driver)


    def goto_register(self):
        self.driver.find_element(By.XPATH,'//*[@class="login_registerBar_link"]').click()


