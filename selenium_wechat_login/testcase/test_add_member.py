import pytest
from selenium import webdriver
from ..page.main_page import MainPage


def gen_id(num):
    with open('ids.txt', 'r') as f:
        latest_id = f.readline()
        phone = f.readline()

    datas = []
    for i in range(num):
        latest_id = str(int(latest_id) + 1)  # str
        phone = str(int(phone) + 1)
        uname = "user" + str(latest_id)
        i += 1
        datas.append([uname,latest_id,phone])

    with open('ids.txt', 'w') as f:
        f.writelines([latest_id, "\n", phone])

    return (datas,)


@pytest.fixture(params=gen_id(3)[0])
def get_account_from_fixture(request):
    return request.param

class TestAddMember:

    def setup_class(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.get("https://work.weixin.qq.com/")

        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.chrome_driver_debug = webdriver.Chrome(options=chrome_arg)
        self.chrome_driver_debug.implicitly_wait(5)

        self.loginpage = MainPage(self.chrome_driver).goto_login()
        self.adminpage = self.loginpage.login(self.chrome_driver_debug)
        self.memberpage = self.adminpage.goto_member_page()

    def teardown_class(self):
        self.chrome_driver.quit()
        self.chrome_driver_debug.quit()

    def test_add_member(self,get_account_from_fixture):
        username = get_account_from_fixture[0]
        uid = get_account_from_fixture[1]
        phone = get_account_from_fixture[2]
        self.memberpage.add_member(username,uid,phone)


if __name__ == '__main__':
    import os
    print(os.getcwd())
    pytest.main(["test_add_member.py"])