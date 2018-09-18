#!/usr/bin/env python3
__author__ = 'jbu'
import psutil
import platform
import datetime
from logger import Logger
from checks.check_cpu import CPU
from cron import Cron


class Client:
    def __init__(self, address='127.0.0.1'):
        log = Logger().get()
        log.debug("Initialized client ({})".format(address))
        self.log = log

        if __name__ == '__main__':
            cpu = CPU(logger=log)
            cpu.check()

    def system_status(self):
        os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "I am currently running on %s version %s.  " % (os, version)
        response += "This system is named %s and has %s CPU cores.  " % (name, cores)
        response += "Current disk_percent is %s percent.  " % disk_percent
        response += "Current CPU utilization is %s percent.  " % cpu_percent
        response += "Current memory utilization is %s percent. " % memory_percent
        response += "it's running since %s." % running_since
        self.log.debug(response)
        return response

    def register_job(self):
        cron = Cron(logger=self.log)
        cron.create_job()


client = Client()
client.register_job()
# client.system_status()

