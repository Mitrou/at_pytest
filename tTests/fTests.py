from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver_get(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()

class TestSetup:
    def test_data_are_valid(self):
        assert 1 == 1

@pytest.mark.usefixtures("driver_get")
class TestLogin:
    def cls_config(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    def test_init_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        assert self.driver.title == "OrangeHRM"

    def test_login(self):
        err = 0
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.implicitly_wait(10)
        try:
            TestLogin.cls_config(self).until(EC.visibility_of_element_located((By.ID, 'welcome')))
        except:
            err = err + 1
        assert err == 0

    def test_logout(self):
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        assert self.driver.title == "OrangeHRM"

print("Test Completed")#