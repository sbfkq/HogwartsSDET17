import sys
# print(sys.path)
sys.path.append("..")
# print(sys.path)
import os
# print(os.getcwd())
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def get_chromedriver():
    driver =  webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/")
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def get_chromedriver_debug():
    chrome_arg = webdriver.ChromeOptions()
    chrome_arg.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=chrome_arg)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# def gen_id():
#     with open('.gen_ids.txt', 'r') as f:
#         latest_id = f.readline()
#         phone = f.readline()
#
#     datas = []
#     for i in range(10):
#         latest_id = str(int(latest_id) + 1)  # str
#         phone = str(int(phone) + 1)
#         uname = "user" + str(latest_id)
#         i += 1
#         datas.append([uname,latest_id,phone])
#
#     with open('testcase/gen_ids.txt', 'w') as f:
#         f.writelines([latest_id, "\n", phone])
#
#     return (datas,)
#
#
# @pytest.fixture(params=gen_id()[0])
# def get_account_from_fixture(request):
#     return request.param


if __name__ == '__main__':
    print(gen_id())