'''
Monitoring program that keeps track of cpu, memory and storage data.
'''
import utils
import psutil
import logging
import time
import alarm

class Monitoring:
    def __init__(self):
        self.cpu_usage = 0
        self.memory_percent = 0
        self.used_memory_in_GB = 0
        self.total_memory_in_GB = 0
        self.storage_used_in_GB = 0
        self.storage_total_in_GB = 0
        self.storage_percent = 0

        self.monitoring_running = False
    
    def check_if_monitoring_is_running(self):
        if self.monitoring_running == False:
            self.monitoring_running = True
            return False
        else:
            return True
        
    def update_data(self):

        # To convert to GB from Byte
        GB_FACTOR = 1024**3
        
        # Check's the CPU usage
        self.cpu_usage = psutil.cpu_percent(interval=0.1)

        # Check's the memory
        memory = psutil.virtual_memory()
        self.memory_percent = memory.percent
        # Convert used memory to GB
        byte_used_value = memory.used
        self.used_memory_in_GB = byte_used_value / GB_FACTOR
        # Convert total memory to GB
        byte_total_value = memory.total
        self.total_memory_in_GB = byte_total_value / GB_FACTOR

        # Check's the storage
        storage = psutil.disk_usage('/')
        self.storage_percent = storage.percent
        # Calculate storage usage to GB
        storage_used_value = storage.used
        self.storage_used_in_GB = storage_used_value / GB_FACTOR
        # Calculate storage total to GB
        storage_total_value = storage.total
        self.storage_total_in_GB = storage_total_value / GB_FACTOR

    
system = Monitoring()

def start_monitoring():
    
    if system.check_if_monitoring_is_running() == True:
        print("Monitoring already running.")
        utils.timer_short()

    else:
        print("Monitoring activated!")
        utils.timer_short()
    return

def show_monitoring_list():
    system.update_data()
     # Get the current data as a string for printing in main.py
    if not system.monitoring_running:
        print("Nothing is being monitored currently.") 
        utils.timer_short()
        return
    utils.clear_console()
    print(f"CPU-användning: {round(system.cpu_usage)}%\n"
          f"Minnesanvändning: {system.memory_percent}% ({system.used_memory_in_GB:.1f} GB av {system.total_memory_in_GB:.1f} GB använt)\n"
          f"Diskanvändning: {system.storage_percent}% ({round(system.storage_used_in_GB)} GB av {round(system.storage_total_in_GB)} GB använt)") 
    utils.press_any_key()
    return

def monitoring_mode():
     # Checking CPU alarms
    utils.clear_console()
    logging.info("Monitoring mode activated.")
    loop = True
    while loop:
        
        print("Monitoring mode activated, press any key to go back to menu.")
        time.sleep(1)

        for times in range(2): # We go over the alarm checks 2 times before printing out monitoring mode
            system.update_data()
            
            # Checks the lists of alarms if any is triggered by the current data
            for alarm_warning in alarm.sort_alarms():
                if alarm_warning["type"] == "CPU-alarm":
                    if alarm_warning["threshold"] <= system.cpu_usage:
                        print(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {alarm_warning["threshold"]}%***")
                        logging.warning(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {alarm_warning["threshold"]}%***")
            for alarm_warning in alarm.sort_alarms():
                if alarm_warning["type"] == "Memory-alarm":
                    if alarm_warning["threshold"] <= system.memory_percent:
                        print(f"***WARNING, ALARM ACTIVATED, MEMORY USAGE OVER {alarm_warning["threshold"]}%***")
                        logging.warning(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {alarm_warning["threshold"]}%***")
            for alarm_warning in alarm.sort_alarms():
                if alarm_warning["type"] == "Storage-alarm":
                    if alarm_warning["threshold"] <= system.storage_percent:
                        print(f"***WARNING, ALARM ACTIVATED, STORAGE USAGE OVER {alarm_warning["threshold"]}%***")
                        logging.warning(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {alarm_warning["threshold"]}%***")

            if utils.wait_for_any_key_or_timeout(5):
                loop = False
                break
                