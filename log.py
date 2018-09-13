import logging.config


class Log:
    def __init__(self, name):
        # create root logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('monitoring.log')
        fh.setLevel(logging.DEBUG)
        # create console handler to log error in the console
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)
