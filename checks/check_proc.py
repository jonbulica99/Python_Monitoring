#!/usr/bin/env python3
__author__ = 'rosnerh'

from checks.check import Check
import psutil


class Proc(Check):

    def __init__(self, warning=50, critical=100, cron_time='* * * * *', logger=None):
        self.name = 'Proc'
        self.command = 'check_proc.py'
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
        proc_count = sum(1 for _ in psutil.process_iter())
        # third value in the mem_info tuple contains the memory usage in percent
        self.set_value(proc_count)
        return proc_count
