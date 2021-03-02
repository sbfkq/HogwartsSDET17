import time

from selenium.webdriver.common.by import By


class MemberPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self,username,id,phone):
        time.sleep(2)

        # def wait_name(driver):
        #     btns = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
        #     btns[-1].click()
        #     eles =  driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
        #     return len(eles)>0
        #
        # WebDriverWait(driver,10).until(wait_name)

        self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(id)
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys(phone)
        self.driver.find_element(By.XPATH, '//*[@name="sendInvite"]').click()

        self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]')[1].click()

if __name__ == '__main__':
    print()