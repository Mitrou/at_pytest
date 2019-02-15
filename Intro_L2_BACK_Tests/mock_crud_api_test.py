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

FIRST_NAMES = ('john', 'paul', 'ringo', 'george', 'phil', 'pete')
LAST_NAMES = ('lennon', 'mccartney', 'starr', 'harrison', 'spector', 'best')
SENIORITY = ('junior', 'middle', 'senior', 'tech lead')
POSITIONS = ('tester', 'dev-ops', 'developer', 'admin')
empty_str = ''
base_url = 'http://qainterview.cogniance.com/candidates'



def json_body_generator(arg):
	thousand_chars_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10000)])
	ten_chars_spec_symbols = ''.join([random.choice(string.punctuation) for n in range(10)])
	fl_name_positive = choice(FIRST_NAMES) + ' ' + choice(LAST_NAMES)
	position_positive = choice(SENIORITY) + ' ' + choice(POSITIONS)
	request_body = ''
	if arg == 'POS':
		request_body = '{"name": "'+ fl_name_positive + '", "position": "' + position_positive + '"}'
	elif arg == 'int_name':
		request_body = '{"name": "'+ '123' + '", "position": "' + position_positive + '"}'
	elif arg == 'int_position':
		request_body = '{"name": "'+ fl_name_positive + '", "position": "' + '123' + '"}'
	elif arg == '10k_chars_name':
		request_body = '{"name": "'+ thousand_chars_str + '", "position": "' + position_positive + '"}'
	elif arg == '10k_chars_position':
		request_body = '{"name": "'+ fl_name_positive + ', "position": "' + thousand_chars_str + '"}'
	elif arg == '10_chars_spec_symbols':
		request_body = '{"name": "'+ ten_chars_spec_symbols + '", "position": "' + ten_chars_spec_symbols + '"}'
	elif arg == 'N_blank_whole':
		request_body = '{}'
	elif arg == 'N_blank_values':
		request_body = '{"name": ,"position": }'
	elif arg == 'N_blank_keys':
		request_body = '{ :"'+ fl_name_positive + '", :"' + thousand_chars_str + '"}'
	elif arg == 'N_no_name':
		request_body = '{"position": "' + position_positive + '"}'
	elif arg == 'N_no_position':
		request_body = '{"name": "' + fl_name_positive + '"}'
	elif arg == 'tree_elements':
		request_body = '{"name": "value1", "position": "value1", "key3": "value3"}'
	return request_body


def test_api_get_smoke():
	get_p_responce = requests.get(base_url)
	status_code_to_test = get_p_responce.status_code
	assert status_code_to_test == SUCCESS
	
def test_check_get_all_and_existing_data():
	global list_of_existing_ids
	list_of_existing_ids = []
	get_p_responce = requests.get(base_url)
	json_to_operate = get_p_responce.json()['candidates']
	try:
		for i in json_to_operate:
			list_of_existing_ids.append(i['id'])
	except:
		pytest.fail('No initial data loadad')

def test_data_are_valid():
	to_test = json_body_generator("POS")
	assert type(to_test) is str

def test_api_post_positive_status_code():
	positive_post_body = json_body_generator('POS')
	post_p_responce = requests.post(base_url, data = positive_post_body, headers=correct_header)
	status_code_to_test = post_p_responce.status_code
	global json_to_operate_in_post
	global posted_id
	json_to_operate_in_post = post_p_responce.json()['candidate']
	posted_id = json_to_operate_in_post.get('id')
	assert status_code_to_test == ADDED

def test_api_post_positive_crosscheck_by_get_ids():
	get_p_responce = requests.get(base_url)
	json_to_operate = get_p_responce.json()['candidates']
	a = dict(json_to_operate[-1]).get('id')
	b =  posted_id
	print(a)
	assert a == b

def test_api_post_positive_crosscheck_by_get_values():
	get_p_responce = requests.get(base_url)
	json_to_operate = get_p_responce.json()['candidates']
	a = dict(json_to_operate[-1])
	b =  json_to_operate_in_post
	assert a == b

def test_delete_pos_status_code():
	del_errors = []
	del_p_responce = requests.delete(base_url+ '/' + str(posted_id))
	if del_p_responce.status_code != SUCCESS:
		del_errors.append("Status code is unexpected")
	assert len(del_errors) == 0

def test_10_posts_10_deletes():
	ids_posted = []
	ids_left_after_delete = []
	ten_posts_dels_errors = []
	a = list_of_existing_ids
	for i in range(10):
		positive_post_body = json_body_generator('POS')
		post_p_ten_posts_test = requests.post(base_url, data=positive_post_body, headers=correct_header)
		ten_posts_test_json = post_p_ten_posts_test.json()['candidate']
		ten_posts_test_posted_id = ten_posts_test_json.get('id')
		ids_posted.append(ten_posts_test_posted_id)
	if len(ids_posted) != 10:
		ten_posts_dels_errors.append('count of posts is not cool')
	for i in ids_posted:
		requests.delete(base_url+ '/' + str(i))
	get_p_responce = requests.get(base_url)
	json_to_operate = get_p_responce.json()['candidates']
	for i in json_to_operate:
		ids_left_after_delete.append(i['id'])
	if a != ids_left_after_delete:
		ten_posts_dels_errors.append('something went wrong with delete')
	assert len(ten_posts_dels_errors) == 0

def test_final_data_comparison():
	global list_of_updated_ids
	list_of_updated_ids = []
	a = list_of_existing_ids
	get_p_responce = requests.get(base_url)
	json_to_operate = get_p_responce.json()['candidates']
	for i in json_to_operate:
		list_of_updated_ids.append(i['id'])
	print(len(a), len(list_of_updated_ids))
	assert a == list_of_updated_ids

