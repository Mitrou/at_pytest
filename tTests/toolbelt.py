import os
import time
import allure
import pytest
from selenium import webdriver
import random
import string

# variables
base_url_mock = "https://opensource-demo.orangehrmlive.com/"
base_url = "http://localhost:5005"


# tools-n-data
def random_chars_and_numbers_string(length=8, mode=0):
    random_keys = ''
    if mode == 0:
        random_keys = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    elif mode == 1:
        random_keys = ''.join(random.choices(string.ascii_uppercase, k=length))
    elif mode == 2:
        random_keys = ''.join(random.choices(string.digits, k=length))
    return random_keys
