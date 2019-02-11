from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from toolbelt import base_url




driver = webdriver.Chrome()
driver.get('http://localhost:5005/#/login')
driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
driver.find_element_by_id("email").send_keys('admin@intro.com')
driver.find_element_by_id("password").send_keys(Keys.CONTROL, "a", Keys.DELETE)
driver.find_element_by_id("password").send_keys('admin')
driver.find_element_by_id("submit").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='user-avatar']"))
    )
    print('LOCATED!')
except:
    print('not located :(')
a = driver.find_elements_by_xpath("//div[@class ='side-nav']/ul/li")
a[0].click()
print(len(a))


# driver.find_element_by_id("email").send_keys('sdWWWWsdfsdf')
# driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)

# try:
#     driver.find_element_by_class_name('form-error').is_displayed()
#     print('PRESENT!')
#     print(driver.find_element_by_class_name('form-error')).get_text()
# except:
#     print('not present')
# driver.find_element_by_id("email").send_keys(Keys.CONTROL, "a", Keys.DELETE)
# driver.find_element_by_id("email").click()
# sleep(1)
# try:
#     driver.find_element_by_class_name('form-error').is_displayed()
#     print('PRESENT!')
#     print(driver.find_element_by_xpath("//div[@class='form-error']/p").get_text())
# except:
#     print('not present')
# a = driver.find_elements_by_xpath("//div[@class='form-error']/p")
# print(a)
# print(a[1].get_attribute('innerText'))
# print(len(a))
# driver.close()

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