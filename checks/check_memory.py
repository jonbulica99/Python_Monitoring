#!/usr/bin/env python3
__author__ = 'jbu'

from checks.check import Check
from psutil import virtual_memory


class Memory(Check):

    def __init__(self, warning=30.0, critical=60.0, cron_time='* * * * *', logger=None):
        self.name = 'Memory'
        self.command = 'check_memory.py'
        super().__init__(name=self.name, command=self.command, warning=warning, critical=critical, cron_time=cron_time,
                         logger=logger)

    def set_value(self, value):
        self.warn_threshold = (value > float(self.warning))
        self.crit_threshold = (value > float(self.critical))
        super().set_value(value)

    def check(self):
        # second value in the mem_info tuple contains the memory usage in percent
        mem_info = virtual_memory()[2]
        self.set_value(mem_info)
        return mem_info
