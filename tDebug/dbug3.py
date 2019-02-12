# import poplib
# import email
#
# pop_conn = poplib.POP3_SSL('pop.gmail.com')
# pop_conn.user('s.molch.test@gmail.com')
# pop_conn.pass_('gtkmvtyb')
#
# # Get messages from server:
# messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
#
# # Concat message pieces:
# messages1 = [b"\n".join(mssg[1]) for mssg in messages]
#
# # Parse message intom an email object:
# messages2 = [email.message_from_bytes(mssg) for mssg in messages1]
# for message in messages2:
#     print(message['subject'])
# pop_conn.quit()


"""
messages = [b"\n".join(mssg[1]) for mssg in messages] ;; 
messages = [email.message_from_bytes(mssg) for mssg in messages] """


import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "s.molch.test" + ORG_EMAIL
FROM_PWD    = "gtkmvtyb"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


def all_email_from_gmail():
        emails = []
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print(len(id_list))
        for i in range(latest_email_id, first_email_id, -1):
            typ, data = mail.fetch(str.encode(str(i)), '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = msg.get_payload()
                    print('From : ' + str(email_from) + '\n')
                    print('Subject : ' + str(email_subject) + '\n')
                    print('Body : ' + str(email_body) + '\n')


def last_email_from_gmail():
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


print(last_email_from_gmail())
