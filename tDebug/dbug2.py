from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)

err = 0
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.implicitly_wait(10)
def conf(self, arg):
    self.wait = WebDriverWait(self.driver, arg)
    return self.wait


try:
    conf(self, 10).until(EC.visibility_of_element_located((By.ID, 'welcome')))
    print("yuuup")
    driver.close()
except:
    print("noooop")
    driver.close()