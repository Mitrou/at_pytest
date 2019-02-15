from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toolbelt import base_url
from toolbelt import random_chars_and_numbers_string


class TestWebLoginPageLoad:
    def test_page_load(self):
        try:
            self.driver.get(base_url)
            self.driver.implicitly_wait(10)
        except:
            pytest.fail("Base URL smoke failure")


class TestLoginPageLogin:
    """5. When I enter correct combination of username and password, I would be redirected to my dashboard screen."""
    def test_neg_login_wrong_password(self):
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").send_keys('admin@intro.com')
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("submit").click()
        assert self.driver.find_element_by_id("login-error").get_attribute('innerText') == 'Invalid email or password'

    def test_neg_login_wrong_emailandpassword(self):
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string(), 'admin@intro.com')
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("submit").click()
        assert self.driver.find_element_by_id("login-error").get_attribute('innerText') == 'Invalid email or password'

    def test_wrong_email(self):
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").send_keys('admin@intro.com')
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("submit").click()
        assert self.driver.find_element_by_id("login-error").get_attribute('innerText') == 'Invalid email or password'

    def test_pos_login(self):
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").send_keys('admin@intro.com')
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").send_keys('admin')
        self.driver.find_element_by_id("submit").click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='user-avatar']"))
            )
        except:
            pytest.fail("User did not logged in properly in 10 seconds")

class TestTabsLoggedSmk:
    def test_page_home_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[0].click()
        # sleep(1) # //div[@class='mat-button-ripple mat-ripple']
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='mat-button-ripple mat-ripple']"))
            )
        except:
            pytest.fail("HOME tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute(
                'innerText') == 'Statistics'

    def test_page_users_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[1].click()
        # sleep(1) # datatable-body-cell-label
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//label[@class='datatable-checkbox ng-star-inserted']"))
            )
        except:
            pytest.fail("USERS tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute(
                'innerText') == 'Users'

    def test_page_holidays_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[2].click()
        sleep(1) # //button[@class='mat-stroked-button mat-primary']
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='mat-stroked-button mat-primary']"))
            )
        except:
            pytest.fail("HOLIDAYS tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute(
                'innerText') == 'Holidays'

    def test_page_universities_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[3].click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='datatable-body-cell-label']"))
            )
        except:
            pytest.fail("Universities tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute(
                'innerText') == 'Universities'

    def test_page_gettogethers_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[4].click()
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//wml-get-togethers-page[@class='ng-star-inserted']"))
            )
        except:
            pytest.fail("Get togethers tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute(
                'innerText') == 'Get togethers'


    def test_page_meetingspots_tab_click(self):
        self.driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")[5].click()
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='datatable-body-cell-label']"))
            )
        except:
            pytest.fail("Meeting Spots tab did not loaded in 2 secs")
        assert self.driver.find_elements_by_xpath("//div[@class='pull-left']/h1")[0].get_attribute('innerText') == 'Meeting Spots'


class TestLogOut:
    def test_logout_button(self):
        try:
            self.driver.find_element_by_xpath("//div[@class = 'mask']") is True
        except:
            pytest.fail("Log Out button did not found")

    def test_logout_func(self):
        self.driver.find_elements_by_xpath("//div[@class = 'mask']")[0].click()
        try:
            self.driver.find_element_by_xpath("//div[@class='auth-layout']").is_displayed()
        except:
            pytest.fail("User did not logged out")
