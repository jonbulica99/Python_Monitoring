__author__ = 'jbu'


class Notification:

    def __init__(self, name='', _type='generic', message='', logger=None):
        self.name = name
        self.type = _type
        self.message = message
        self.logger = logger

    def notify(self):
        self.logger.debug("Sending notification {} of type {}".format(self.name, self.type))
