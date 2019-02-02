from selenium import webdriver
import time
import pytest

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)

err = 0
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.implicitly_wait(10)
try:
    driver.find_element_by_id("qqqq") is True
except:
    err = err + 1
print(err)

driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()
assert driver.title == "OrangeHRM"
driver.close()
print("Test Completed")