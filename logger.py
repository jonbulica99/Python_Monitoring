import logging.config
import settings
import os


class Logger:
    def __init__(self, name="monitoring"):
        # create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("{}/{}/{}.log".format(os.path.dirname(__file__), settings.LOG_DIR, name))
        fh.setLevel(logging.DEBUG)
        # create console handler to log error in the console
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(settings.LOG_FORMAT)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self._logger = logger

    def get(self):
        return self._logger
