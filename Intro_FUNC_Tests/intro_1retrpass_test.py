from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toolbelt import base_url
from toolbelt import random_chars_and_numbers_string
import allure


class TestWebLoginPageLoad:
    def test_page_load(self):
        try:
            self.driver.get(base_url)
            self.driver.implicitly_wait(10)
        except:
            pytest.fail("Base URL smoke failure")


class TestLoginPageLoginFront:
    """As a admin, I should be able to recover password in case I forget my password.
    Forgot Password link should be available on Sign In / Sign Up page and it should include below fields on form
    User Name
    On submission of User Name, system will send an email with link to reset password.
    Reset Password page should contain
    Reset Password (Password input field)
    Upon successful reset, user should be redirected to login page."""
    def test_forgorpasslink_available(self):
        self.driver.get(base_url + '/#/login')
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='reset-password-holder']/a"))
            )
        except:
            pytest.fail("Forgot Password link is not available")

    def test_forgorpasslink_click(self):
        self.driver.find_element_by_xpath("//div[@class='reset-password-holder']/a").click()
        assert self.driver.page_source.find("Reset Password")

    def test_forgotpass_email(self):
        self.driver.find_element_by_id("email").send_keys('s.molch.test@gmail.com')
        try:
            self.driver.find_element_by_xpath("//span[@class = 'mat-button-wrapper']").is_enabled()
        except:
            pytest.fail("Reset password button is disabled while valid email entered")
        self.driver.find_element_by_xpath("//span[@class = 'mat-button-wrapper']").click()
        assert self.driver.page_source.find("Email sent")


# class TestLoginPageLoginFlow:
#     def test_pos_forgotpass_email_sent(self):
#         pass
#
#     def test_pos_forgotpass_reset_password_page(self):
#         pass
#
#     def test_pos_forgotpass_reset_password_changed(self):
#         pass
