import requests
import pytest
import json
from random import choice
import random
import string



correct_header = {'Content-Type': 'application/json'}
incorrect_header = {'Content-type': 'x-www-form-urlencoded'}

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201
NOT_FOUND = 404
INT_ERROR = 500

base_url = 'http://localhost:5004'


class TestAPIIntroCRUD:
    def test_api_get_auth_smoke(self):
        get_p_response = requests.get(base_url, '/authenticate')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_pswrdinit_smoke(self):
        get_p_response = requests.get(base_url, '/reset-password-init')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_pswrdfnl_smoke(self):
        get_p_response = requests.get(base_url, '/reset-password-finish')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_university_smoke(self):
        get_p_response = requests.get(base_url, '/university')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_department_smoke(self):
        get_p_response = requests.get(base_url, '/department')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_holiday_smoke(self):
        get_p_response = requests.get(base_url, '/holiday')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_curruser_smoke(self):
        get_p_response = requests.get(base_url, '/current-user')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_user_smoke(self):
        get_p_response = requests.get(base_url, '/user')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_userstats_smoke(self):
        get_p_response = requests.get(base_url, '/user-statistics')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_meetingstats_smoke(self):
        get_p_response = requests.get(base_url, '/meeting-statistics')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_gettogethers_smoke(self):
        get_p_response = requests.get(base_url, '/get-togethers')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_topinterests_smoke(self):
        get_p_response = requests.get(base_url, '/top-interests')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_topusers_smoke(self):
        get_p_response = requests.get(base_url, '/top-users')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_quickstats_smoke(self):
        get_p_response = requests.get(base_url, '/quick-stats')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS

    def test_api_get_meetingspots_smoke(self):
        get_p_response = requests.get(base_url, '/meeting-spot')
        status_code_to_test = get_p_response.status_code
        assert status_code_to_test == SUCCESS
