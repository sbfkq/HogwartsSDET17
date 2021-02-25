import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

@pytest.fixture(scope='class')
def get_chromedriver():
    driver =  webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def get_chromedriver_debug():
    chrome_arg = webdriver.ChromeOptions()
    chrome_arg.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=chrome_arg)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



class TestSelenium:

    def setup_method(self,method):
        self.var = {}

    def teardown_method(self,method):
        pass

    def test_open(self,get_chromedriver):
        driver  = get_chromedriver
        driver.get("https://work.weixin.qq.com/")
        driver.find_element(By.XPATH, '//*[@class="index_head_info_pCDownloadBtn"]').click()
        driver.find_element(By.XPATH, '//*[@class="qui_inputText ww_inputText ww_inputText_Big"]').send_keys("Bravo!")
        time.sleep(3)

    def test_cookie_save(self,get_chromedriver_debug):
        # 存入 cookie
        driver = get_chromedriver_debug
        cookies = driver.get_cookies()
        with open("tmp.text", "w", encoding="utf-8") as f:
            json.dump(cookies, f)
        print(cookies)

    def test_cookie_login(self,get_chromedriver):
        # 读取 cookie
        driver = get_chromedriver
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open('tmp.text', 'r', encoding='utf-8') as f:
            cookies = json.load(f)

        for i in cookies:
            driver.add_cookie(i)
        driver.refresh()

        driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        time.sleep(3)


if __name__=="__main__":
    pytest.main(["test_selenium.py::test_cookie","-v"])
