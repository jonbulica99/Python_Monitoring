from logger import Logger

log = Logger().get()
log.error("Fehler 123")


class Notification:
    name = ''
    message = ''

    def __init__(self, name='', message=''):
        self.name = name
        self.message = message
