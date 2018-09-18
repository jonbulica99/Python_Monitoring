#!/usr/bin/env python3
import settings

__author__ = 'jbu'
from crontab import CronTab


class Cron:

    def __init__(self, command=settings.CRON_DEFAULT_COMMAND, time=settings.CRON_DEFAULT_TIME, logger=None):
        self.time = time
        self.command = command
        self.comment = 'Monitoring_{}'.format(self.command)
        self.logger = logger
        # Linux-only, loads the crontab from the $USER variable
        self.crontab = CronTab(user=True)
        self.logger.debug('Initialized Cron {} at interval {}'.format(self.command, self.time))

    def create_job(self, job=None):
        if job is None:
            job = self.crontab.new(command=self.command, comment=self.comment)

        job.setall(self.time)

        if job.is_valid():
            existing_jobs = self.crontab.find_comment(self.comment)
            if sum(1 for _ in existing_jobs) > 0:
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
