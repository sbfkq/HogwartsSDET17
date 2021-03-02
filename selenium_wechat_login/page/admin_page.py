from selenium.webdriver.common.by import By
from .member_page import MemberPage

class AdminPage:
    def __init__(self,driver):
        self.driver = driver

    def goto_member_page(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return MemberPage(self.driver)
