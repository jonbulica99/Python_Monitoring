#!/usr/bin/env python3
__author__ = 'jbu'

from checks.check import Check
import http.client


class Net(Check):

    def __init__(self, warning=0, critical=0, cron_time='* * * * *', logger=None):
        self.name = 'Net'
        self.command = 'check_net.py'
        super().__init__(name=self.name, command=self.command, warning=warning, critical=critical, cron_time=cron_time,
                         logger=logger)

    def set_value(self, value):
        # self.warn_threshold = (value == float(self.warning))
        self.crit_threshold = (value == float(self.critical))
        super().set_value(value)

    def check(self):
        connection = int(self.is_connected())
        self.set_value(connection)
        return connection

    @staticmethod
    def is_connected():
        # noinspection PyUnresolvedReferences
        conn = http.client.HTTPConnection("www.google.com", timeout=5)
        # noinspection PyBroadException
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False
