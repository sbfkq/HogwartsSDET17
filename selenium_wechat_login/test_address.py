import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='class')
def get_chromedriver():
    driver =  webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def get_chromedriver_debug():
    chrome_arg = webdriver.ChromeOptions()
    chrome_arg.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=chrome_arg)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def get_id():
    with open('ids.txt', 'r') as f:
        latest_id = f.readline()
        phone = f.readline()

        latest_id = str(int(latest_id) + 1)  # str
        new_phone = str(int(phone) + 1)
        uname = "user" + str(latest_id)

    with open('ids.txt', 'w') as f:
        f.writelines([latest_id,"\n",new_phone])

    return uname, latest_id,new_phone



class TestLogin:

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

    def test_address(self,get_chromedriver):
        driver = get_chromedriver
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        def wait_name(driver):
            btns = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
            btns[-1].click()
            eles =  driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles)>0

        WebDriverWait(driver,10).until(wait_name)

        # time.sleep(2)
        # driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()

        time.sleep(2)
        username,id,phone = get_id()
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(id)
        driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys(phone)

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@name="sendInvite"]').click()

        driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]')[1].click()



if __name__=="__main__":
    pytest.main(["test_address.py::TestLogin","-v"])


