#!/usr/bin/env python3
__author__ = 'jbu'

from checks.check import Check
from psutil import net_connections


class Net(Check):

    def __init__(self, warning=50, critical=100, cron_time='* * * * *', logger=None):
        self.name = 'Net'
        self.command = 'check_net.py'
        self.warning = warning
        self.critical = critical
        self.cron_time = cron_time
        self.logger = logger
        super().__init__(self.name, self.command, self.value, self.warning, self.critical, self.cron_time, self.logger)

    def set_value(self, value):
        self.warn_threshold = (value > float(self.warning))
        self.crit_threshold = (value > float(self.critical))
        super().set_value(value)

    def check(self):
        # TODO finish this
        net_status = net_connections()
        # third value in the mem_info tuple contains the memory usage in percent
        self.set_value(0)
        return 0
