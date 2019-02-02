from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="session")
def driver(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()