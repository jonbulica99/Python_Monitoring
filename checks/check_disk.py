#!/usr/bin/env python3
__author__ = 'jbu'
from checks.check import Check
from psutil import disk_usage


class Disk(Check):

    def __init__(self, path='/', warning=30.0, critical=60.0, cron_time='* * * * *', logger=None):
        self.name = 'Disk'
        self.command = 'check_disk.py'
        self.path = path
        super().__init__(name=self.name, command=self.command, warning=warning, critical=critical, cron_time=cron_time,
                         logger=logger)

    def set_value(self, value):
        self.warn_threshold = (value > float(self.warning))
        self.crit_threshold = (value > float(self.critical))
        super().set_value(value)

    def check(self):
        # third value in the disk_info tuple contains the disk usage in percent
        disk_info = disk_usage(self.path)[3]
        self.set_value(disk_info)
        return disk_info
