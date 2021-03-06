#!/usr/bin/env python3
__author__ = 'jbu'

import os
import settings
from sys import platform
from crontab import CronTab
from utils.logger import Logger


class Cron:

    def __init__(self, command=settings.CRON_DEFAULT_COMMAND, check=settings.CRON_DEFAULT_CHECK,
                 time=settings.CRON_DEFAULT_TIME):
        self.time = time
        self.command = command
        self.check = check
        # command must contain the python interpreter and the full path to the module
        self.full_command = '{} {}/client.py -c {}'.format(sys.executable, os.path.dirname(__file__), check)
        self.comment = 'Monitoring_{}'.format(check)
        self.logger = Logger().get()
        # Linux-only, loads the crontab from the $USER variable
        if platform == "linux" or platform == "linux2":
            self.crontab = CronTab(user=True)
            self.logger.debug('Initialized Cron {} at interval {}'.format(self.command, self.time))
        else:
            self.logger.error("Crontab only works in Linux-based systems where crontab is installed!")

    @staticmethod
    def from_check(check=None, logger=None):
        if check is None:
            logger.error('This won\'t work unless you provide a check object.')
            exit(1)
        return Cron(command=check.command, check=check.name.lower(), time=check.cron_time, logger=logger)

    def create_job(self, job=None):
        if job is None:
            job = self.crontab.new(command=self.full_command, comment=self.comment)

        job.setall(self.time)

        if job.is_valid():
            existing_jobs = self.crontab.find_comment(self.comment)
            if sum(1 for _ in existing_jobs) > 1:
                self.logger.info("Cronjob {} at interval {} already exists in {}'s crontab and won't be duplicated"
                                 .format(self.command, self.time, self.crontab.user))
                return

            self.logger.info("Cronjob {} is valid and will be written to {}'s crontab"
                             .format(self.command, self.crontab.user))
            job.enable()
            self.crontab.write()
        else:
            self.logger.error("Cronjob {} is invalid and won't be written to {}'s crontab"
                              .format(self.command, self.crontab.user))
