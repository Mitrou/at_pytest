from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
# from conftest import base_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toolbelt import base_url
from toolbelt import random_chars_and_numbers_string
import allure


class TestSetup:
    def test_data_are_valid(self):
        assert 1 == 1


class TestWebLoginPageLoad:
    def test_page_load(self):
        try:
            self.driver.get(base_url)
            self.driver.implicitly_wait(10)
        except:
            pytest.fail("Base URL smoke failure")


class TestLoginPageControlsPresence:
    """1. I should view the user name (text box), password (Text box) and login button.
    """
    def test_login_email_present(self):
        try:
            self.driver.find_element_by_id("email").is_displayed()
        except:
            pytest.fail("Base URL smoke failure")

    def test_login_password_present(self):
        try:
            self.driver.find_element_by_id("password").is_displayed()
        except:
            pytest.fail("Base URL smoke failure")

    def test_login_loginbutton_present(self):
        try:
            self.driver.find_element_by_id("submit").is_displayed()
        except:
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
    """4. I should be displayed error message
    When I enter a wrong combination of user name and password
    When my username/password field is empty
    NO RECS ON EXACT TEXT SO ANY APPLIED
    """
    def test_email_emptyerrorfrom(self):
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").click()
        try:
            self.driver.find_element_by_class_name('form-error').is_displayed()
        except:
            pytest.fail("No error form on empty EMAIL field")

    def test_email_emptyerrortext(self):
        errors = []
        error_messages = self.driver.find_elements_by_xpath("//div[@class='form-error']/p")
        if not len(error_messages) == 2:
            errors.append("Error messages count different from expected")
        if not error_messages[0].get_attribute('innerText') == 'Email is required!':
            errors.append("Error message for empty email FAILURE")
        if not error_messages[1].get_attribute('innerText') == 'Please input a valid email!':
            errors.append("Error message for email format FAILURE")
        assert not errors, "errors occured:{}".format(" ".join(errors))

    def test_email_empty_flow1(self):
        errors = []
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string())
        error_messages = self.driver.find_elements_by_xpath("//div[@class='form-error']/p")
        if not len(error_messages) == 1:
            errors.append("Error messages count different from expected")
        if not error_messages[0].get_attribute('innerText') == 'Please input a valid email!':
            errors.append("Error message for wrong email format FAILURE")
        assert not errors, "errors occured:{}".format(" ".join(errors))

    def test_email_empty_flow2(self):
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("email").send_keys('@')
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("email").send_keys('.')
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string(2, 1))
        error_messages = self.driver.find_elements_by_xpath("//div[@class='form-error']/p")
        assert len(error_messages) == 0

    def test_email_empty_flow3(self):
        errors = []
        self.driver.find_element_by_id("email").send_keys(Keys.BACKSPACE*2)
        error_messages = self.driver.find_elements_by_xpath("//div[@class='form-error']/p")
        if not len(error_messages) == 1:
            errors.append("Error messages count different from expected")
        if not error_messages[0].get_attribute('innerText') == 'Please input a valid email!':
            errors.append("Error message for wrong email format FAILURE")
        assert not errors, "errors occured:{}".format(" ".join(errors))

    def test_email_empty_flow4(self):
        self.driver.find_element_by_id("email").send_keys(random_chars_and_numbers_string(3, 1))
        assert len(self.driver.find_elements_by_xpath("//div[@class='form-error']/p")) == 0

    def test_password_emptyform(self):
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("password").click()
        try:
            self.driver.find_element_by_class_name('form-error').is_displayed()
        except:
            pytest.fail("No error message on empty EMAIL field")

    def test_password_empty_message(self):
        self.driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element_by_id("email").send_keys('fully@walid.eml')
        self.driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        assert len(self.driver.find_elements_by_xpath("//div[@class='form-error']/p")) == 1

    def test_password_empty_message1(self):
        assert self.driver.find_elements_by_xpath("//div[@class='form-error']/p")[0].get_attribute('innerText') == 'Password is required!'

    def test_password_empty_flow1(self):
        self.driver.find_element_by_id("password").send_keys(random_chars_and_numbers_string())
        assert len(self.driver.find_elements_by_xpath("//div[@class='form-error']/p")) == 0

