#!/usr/bin/env python3
__author__ = 'jbu'

from notifications.notification import Notification
import settings


class Mail(Notification):

    def __init__(self, name='mail', message='', logger=None, recipient=settings.MAIL_DEFAULT_RECIPIENT,
                 server=settings.MAIL_DEFAULT_SERVER):
        super().__init__(name=name, _type='Mail', message=message, logger=logger)
        self.recipient = recipient
        self.server = server

    def send_mail(self):
        # TODO implement mail sending here
        self.logger.info("Successfully sent mail to {} via {}".format(self.recipient, self.server))

    def notify(self):
        super().notify()
        self.send_mail()
