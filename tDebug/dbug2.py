from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
driver = webdriver.Chrome()
driver.get('http://localhost:5005/#/login')
driver.find_element_by_id("email").send_keys('sdWWWWsdfsdf')
sleep(1)
try:
    driver.find_element_by_class_name('form-error').is_displayed()
    print('PRESENT!')
    print(driver.find_element_by_class_name('form-error')).get_text()
except:
    print('not present')
driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
driver.find_element_by_id("email").click()
sleep(1)
try:
    driver.find_element_by_class_name('form-error').is_displayed()
    print('PRESENT!')
    print(driver.find_element_by_class_name('form-error')).get_text()
except:
    print('not present')

driver.close()

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