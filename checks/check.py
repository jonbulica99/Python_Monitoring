#!/usr/bin/env python3
__author__ = 'jbu'


class Check:
    warn_threshold = False
    crit_threshold = False
    cron_time = '* * * * *'

    def __init__(self, name='Check', command='check.py', value=0, warning=0, critical=0, cron_time='* * * * *',
                 logger=None):
        self.name = name
        self.value = value
        self.command = command
        self.warning = warning
        self.critical = critical
        self.cron_time = cron_time
        self.logger = logger

    def set_value(self, value):
        self.value = value
        self.check_threshold()

    def check_threshold(self):
        if self.crit_threshold:
            self.crit()
        elif self.warn_threshold:
            self.warn()
        else:
            self.ok()

    def warn(self):
        self.logger.warning("Check {} with value {} exceeded WARNING threshold of {}"
                            .format(self.name, self.value, self.warning))

    def crit(self):
        self.logger.critical("Check {} with value {} exceeded CRITICAL threshold of {}"
                             .format(self.name, self.value, self.critical))

    def ok(self):
        self.logger.info("Check {} with value {} returned status OK"
                         .format(self.name, self.value))
