#!/usr/bin/env python3
__author__ = 'jbu'
from checks.check import Check
from psutil import cpu_percent


class Cpu(Check):

    def __init__(self, warning=30.0, critical=60.0, cron_time='* * * * *', logger=None):
        self.name = 'CPU'
        self.command = 'check_cpu.py'
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
        cpu = cpu_percent()
        self.set_value(cpu)
        return cpu
