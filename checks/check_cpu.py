#!/usr/bin/env python3
from checks.check import Check
from psutil import cpu_percent

__author__ = 'jbu'


class CPU(Check):

    def __init__(self, warning=30.0, critical=50.0, cron_time='* * * * *'):
        self.name = 'CPU'
        self.command = 'check_cpu.py'
        self.warning = warning
        self.critical = critical
        self.cron_time = cron_time
        super().__init__(self.name, self.command, self.value, warning, critical, cron_time)

    def set_value(self, value):
        self.warn_threshold = (value > float(self.warning))
        self.crit_threshold = (value > float(self.critical))
        super().set_value(value)

    def check(self):
        self.set_value(cpu_percent())



