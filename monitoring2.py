'''
This program runs the monitoring


'''
import logging
import time
import utils
import alarm
import psutil

logging.basicConfig(filename='alarms.log', level=logging.INFO, format='%(asctime)s %(message)s')

class Monitor:
    def __init__(self):
        self.cpu_usage = 0 
        self.memory_usage = 0
        self.storage_usage = 0
        self.monitoring_running = False

    def checks_if_monitoring_is_running(self):
        if not self.monitoring_running:
            self.monitoring_running = True
            return False
        else:
            return True

