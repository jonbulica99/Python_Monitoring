#!/usr/bin/env python3
__author__ = 'jbu'

from notifications.notification import Notification
import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail(Notification):

    def __init__(self, name='mail', subject=settings.MAIL_DEFAULT_SUBJECT, message=settings.MAIL_DEFAULT_MESSAGE,
                 logger=None, recipient=settings.MAIL_DEFAULT_RECIPIENT, server=settings.MAIL_DEFAULT_SERVER,
                 port=settings.MAIL_DEFAULT_SERVER_PORT):
        self.subject = subject
        self.recipient = recipient
        self.server = server
        self.port = port
        self.client = smtplib.SMTP(host=server, port=port)
        super().__init__(name=name, _type='Mail', message=message, logger=logger)

    def send_mail(self):
        mail = MIMEMultipart()
        # setup mail parameters
        mail['From'] = "monitoring"
        mail['To'] = self.recipient
        mail['Subject'] = self.subject

        # inject the message
        mail.attach(MIMEText(self.message, 'plain'))

        # send the mail
        self.client.sendmail(mail['From'], mail['To'], mail.as_string())
        self.client.quit()
        self.logger.info("Successfully sent mail to {} via {}".format(self.recipient, self.server))

    def notify(self):
        super().notify()
        self.send_mail()

    def format_message(self, check=None):
        self.message = self.message.format(self.recipient, check.name, check.value)
        super().format_message(check)
