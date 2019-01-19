"""
email sender class

sends only text emails
"""

import smtplib
from email.mime.text import MIMEText
from string import Template


class Sender(object):
    def __init__(self, message=None, email=None, password=None):
        self.__email = email
        self.__password = password
        self.__message = message

    def __create_email(self, subject, recipient, message_details):
        with open(self.__message, 'r') as message_txt:
            message = Template(message_txt.read())
            message = message.substitute(**message_details)
            message = MIMEText(message)
            message['Subject'] = subject
            message['From'] = self.__email
            message['To'] = recipient
            return message

    def send_mail(self, recipient, subject, message_details):
        email_message = self.__create_email(subject, recipient, message_details)
        server = smtplib.SMTP('localhost')
        server.sendmail(self.__email, recipient, email_message.as_string())
        server.quit()



