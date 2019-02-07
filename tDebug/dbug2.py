from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def random_chars_and_numbers_string(length=8):
    random_keys = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return random_keys

print(random_chars_and_numbers_string())
print(random_chars_and_numbers_string(0))
print(random_chars_and_numbers_string(1))
print(random_chars_and_numbers_string(14))
print(random_chars_and_numbers_string(22))
# driver = webdriver.Chrome()
# driver.get("http://localhost:5005")
# driver.implicitly_wait(10)
# is_masked = driver.find_element_by_id("password").get_attribute("type")
# print(is_masked)
# driver.close()
# # err = 0
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# driver.implicitly_wait(10)
# print(driver.current_url)
# driver.get_screenshot_as_file()
# def conf(self, arg):
#     self.wait = WebDriverWait(self.driver, arg)
#     return self.wait
#
#
# try:
#     conf(self, 10).until(EC.visibility_of_element_located((By.ID, 'welcome')))
#     print("yuuup")
#     driver.close()
# except:
#     print("noooop")
#     driver.close()