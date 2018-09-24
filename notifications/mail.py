#!/usr/bin/env python3
__author__ = 'jbu'

from notifications.notification import Notification


class Mail(Notification):

    def __init__(self, name='mail', message='', logger=None, recipient='root@localhost'):
        super().__init__(name=name, _type="Mail", message=message, logger=logger)
        self.recipient = recipient

    def send_mail(self):
        # TODO implement mail sending here
        self.logger.info("Successfully sent mail to {}".format(self.recipient))

    def notify(self):
        super().notify()
        self.send_mail()
