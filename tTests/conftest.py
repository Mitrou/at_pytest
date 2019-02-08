import os
import time
import allure
import pytest
from selenium import webdriver
import random
import string


base_url_mock = "https://opensource-demo.orangehrmlive.com/"
base_url = "http://localhost:5005"


@pytest.fixture(autouse=True, scope='session')
def driver(request):
    import allure
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    for item in request.node.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield driver
    driver.close()


def pytest_exception_interact(node, call, report):
    allure.attach(
        name='ololo',
        body=node.parent._obj.driver.get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG
    )


def random_chars_and_numbers_string(length=8, mode=0):
    random_keys = ''
    if mode == 0:
        random_keys = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    elif mode == 1:
        random_keys = ''.join(random.choices(string.ascii_uppercase, k=length))
    elif mode == 2:
        random_keys = ''.join(random.choices(string.digits, k=length))
    return random_keys

