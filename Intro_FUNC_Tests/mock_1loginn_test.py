from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toolbelt import base_url_mock
import allure


class TestWebSmoke:
    def test_page_load(self):
        try:
            self.driver.get(base_url_mock)
            self.driver.implicitly_wait(10)
        except:
            pytest.fail("Base URL smoke failure")


class TestLogin:
    def cls_config(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    def test_init_page(self):
        self.driver.get(base_url_mock)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "OrangeHRM11"

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

class TestPost:
    def test_post_condition(self):
        self.driver.close()

