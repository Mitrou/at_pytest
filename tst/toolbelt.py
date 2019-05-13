import os
import time
import allure
import pytest
import random
import string
import imaplib
import email


# variables
base_url_mock = "https://opensource-demo.orangehrmlive.com/"
base_url = "http://localhost:5005"
base_url_snz = 'https://snijana.qa.research.ring.com/?videoId=341513f7da49.20180803_221712&validated_by=sergii.molchanov@ring.com&precise=0'

# tools-n-data
# generates string with parameters set
def random_chars_and_numbers_string(length=8, mode=0):
    random_keys = ''
    if mode == 0:
        random_keys = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    elif mode == 1:
        random_keys = ''.join(random.choices(string.ascii_uppercase, k=length))
    elif mode == 2:
        random_keys = ''.join(random.choices(string.digits, k=length))
    return random_keys


# last email on gmail, returns a three component list: FROM, SUBJ, BODY
def last_email_from_gmail():
    ORG_EMAIL = "@gmail.com"
    FROM_EMAIL = "s.molch.test" + ORG_EMAIL
    FROM_PWD = "<password here>"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    emails = []
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id = int(id_list[-1])
    print(len(id_list))
    typ, data = mail.fetch(str.encode(str(latest_email_id)), '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            email_subject = msg['subject']
            email_from = msg['from']
            email_body = msg.get_payload()
            # print('From : ' + str(email_from) + '\n')
            # print('Subject : ' + str(email_subject) + '\n')
            # print('Body : ' + str(email_body) + '\n')
            return[email_from, email_subject, email_body]
