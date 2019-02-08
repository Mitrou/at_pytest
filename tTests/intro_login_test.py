from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import base_url, random_chars_and_numbers_string
import allure



class TestWebLoginPageLoad:
    def test_page_load(self):
        try:
            self.driver.get(base_url)
            self.driver.implicitly_wait(10)
        except SmkError:
            pytest.fail("Base URL smoke failure")


class TestLoginPageControlsPresence:
    """1. I should view the user name (text box), password (Text box) and login button.
    """
    def test_login_email_present(self):
        try:
            self.driver.find_element_by_id("email").is_displayed()
        except ElementIsNotPresent:
            pytest.fail("Base URL smoke failure")

    def test_login_password_present(self):
        try:
            self.driver.find_element_by_id("password").is_displayed()
        except ElementIsNotPresent:
            pytest.fail("Base URL smoke failure")

    def test_login_loginbutton_present(self):
        try:
            self.driver.find_element_by_id("submit").is_displayed()
        except ElementIsNotPresent:
            pytest.fail("Base URL smoke failure")


class TestLoginPageControlsAttributes:
    """2. When I type in my password it should be displayed in encrypted format.
    """
    def test_password_encription(self):
        assert self.driver.find_element_by_id("password").get_attribute("type") == "password"


class TestLoginPageFieldsFill:
    """3. I should be able to enter my user name.
    """
    def test_username_entering(self):
        test_field = self.driver.find_element_by_id("email")
        test_field.send_keys(random_chars_and_numbers_string())
        assert (len(test_field.get_attribute("value")) == 8)


class TestLoginPageErrors:
    driver = webdriver.Chrome()
    """4. I should be displayed error message
    When I enter a wrong combination of user name and password
    When my username/password field is empty
    NO RECS ON EXACT TEXT SO ANY APPLIED
    """
    def test_email_emptyerror(self):
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").click()
        try:
            self.driver.find_element_by_class_name('form-error').is_displayed()
        except ElementIsNotPresent:
            pytest.fail("No error message on empty EMAIL field")
    def test_password_emptyerror(self):
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").click()
        try:
            self.driver.find_element_by_class_name('form-error').is_displayed()
        except ElementIsNotPresent:
            pytest.fail("No error message on empty EMAIL field")


class TestLoginPageLogin:
    """5. When I enter correct combination of username and password, I would be redirected to my dashboard screen."""
    def test_neg_login_wrong_email(self):
        pass

    def test_neg_login_wrong_password(self):
        pass

    def test_neg_login_wrong_emailandpassword(self):
        pass

    def test_pos_login(self):
        pass
