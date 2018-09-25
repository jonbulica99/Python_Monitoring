__author__ = 'jbu'

import settings


class Notification:

    def __init__(self, name='', _type='generic', message=settings.MAIL_DEFAULT_MESSAGE, logger=None):
        self.name = name
        self.type = _type
        self.message = message
        self.logger = logger

    def set_message(self, check=None, message=None):
        if check is None:
            self.logger.error("You should provide a check object for the message to be constructed")
            exit(1)
        if message is not None:
            self.message = message
        self.format_message(check)

    def format_message(self, check=None):
        self.logger.debug("Formatting message for check {}".format(check.name))

    def notify(self):
        self.logger.debug("Sending notification {} of type {}".format(self.name, self.type))
