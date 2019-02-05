import os
import time
import allure
import pytest
from selenium import webdriver


base_url = "https://opensource-demo.orangehrmlive.com/"


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


