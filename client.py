#!/usr/bin/env python3
__author__ = 'jbu'

import os
import psutil
import platform
import datetime
import importlib
from argparse import ArgumentParser
from notifications.mail import Mail
from logger import Logger
from cron import Cron


class Client:
    def __init__(self, address='127.0.0.1'):
        log = Logger().get()
        log.debug("Initialized client ({})".format(address))
        self.log = log
        self.send_mail = False
        self.cron = False

    def system_status(self):
        _os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "I am currently running on %s version %s.  " % (_os, version)
        response += "This system is named %s and has %s CPU cores.  " % (name, cores)
        response += "Current disk_percent is %s percent.  " % disk_percent
        response += "Current CPU utilization is %s percent.  " % cpu_percent
        response += "Current memory utilization is %s percent. " % memory_percent
        response += "it's running since %s." % running_since
        self.log.debug(response)
        return response

    def check_by_name(self, check_name=None):
        if check_name is None:
            self.log.error('This won\'t work unless you provide check_name')
            return
        try:
            # noinspection PyPep8Naming
            Check = getattr(importlib.import_module("checks.check_{}".format(check_name.lower())), check_name.title())
            check = Check(logger=self.log)
            output = check.check()

            if self.send_mail:
                mail = Mail(logger=self.log)
                mail.format_message(check=check)
                mail.send_mail()
            elif self.cron:
                cron = Cron.from_check(check=check, logger=self.log)
                cron.create_job()

            return output
        except ImportError:
            self.log.error("No module or class called '{}' exists".format(check_name))

    @staticmethod
    def get_supported_checks():
        checks = []
        for file in os.listdir("./checks/"):
            if "check_" in file:
                checks.append(file.split('_')[1].split('.')[0])
        return checks


if __name__ == "__main__":
    client = Client()
    parser = ArgumentParser()
    parser.add_argument("-a", "--check-all", dest="all", action='store_true', help="Run all checks once.")
    parser.add_argument("-c", "--checks", nargs='+', dest="checks", help="Specify what to check after.")
    parser.add_argument("-m", "--mail-notification", dest='mail', action='store_true', help="Send a mail notification.")
    parser.add_argument("-j", "--cron-job", dest='cron', action='store_true', help="Set a cron job for the check.")
    parser.add_argument("-s", "--system-status", dest='status', action='store_true', help="Output the system status.")
    args = parser.parse_args()

    # Determine whether we should send a mail
    client.send_mail = args.mail

    # Determine whether we should set a cron job
    client.cron = args.cron

    if args.status:
        client.log.info("Checked system status.")
        print(client.system_status())
    elif args.all:
        for i in client.get_supported_checks():
            client.check_by_name(i)
    elif args.checks:
        for i in args.checks:
            client.check_by_name(i)
    else:
        client.log.error("Provided arguments are invalid.")
