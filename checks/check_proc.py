#!/usr/bin/env python3
__author__ = 'rosnerh'

from checks.check import Check
from psutil import process_iter


class Proc(Check):

    def __init__(self, warning=50, critical=100, cron_time='* * * * *'):
        self.name = 'Proc'
        self.command = 'check_proc.py'
        super().__init__(name=self.name, command=self.command, warning=warning, critical=critical, cron_time=cron_time)

    def set_value(self, value):
        self.warn_threshold = (value > float(self.warning))
        self.crit_threshold = (value > float(self.critical))
        super().set_value(value)

    def check(self):
        proc_count = sum(1 for _ in process_iter())
        # third value in the mem_info tuple contains the memory usage in percent
        self.set_value(proc_count)
        return proc_count
