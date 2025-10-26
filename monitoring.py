'''
Monitoring program that keeps track of cpu, memory and storage data.
'''
import utils
import psutil
import logging
import time
import alarm

class Monitor:
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

    
system = Monitor()

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
    print(f"CPU-usage: {round(system.cpu_usage)}%\n"
          f"Memory-usage: {system.memory_percent}% ({system.used_memory_in_GB:.1f} GB of {system.total_memory_in_GB:.1f} GB used)\n"
          f"Storage-usage: {system.storage_percent}% ({round(system.storage_used_in_GB)} GB of {round(system.storage_total_in_GB)} GB used)") 
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

        for times in range(2): # Looping 2 times before going back to the start of while loop
            system.update_data()
            all_alarms = alarm.user_alarms

            '''
            Finding the closest alarm to the current threshold
            Kinda like King of the hill, replace when found a closer number to the current target
            And you just repeat it for Memory and Storage after CPU
            '''

            # CPU
            highest_cpu_alarm_found = None

            for current_alarm in all_alarms:
                if current_alarm["type"] == "CPU-alarm":
                    if current_alarm["threshold"] <= system.cpu_usage:
                        if highest_cpu_alarm_found == None:
                            highest_cpu_alarm_found = current_alarm
                        elif current_alarm["threshold"] > highest_cpu_alarm_found["threshold"]:
                            highest_cpu_alarm_found = current_alarm

            if highest_cpu_alarm_found is not None:
                print(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {highest_cpu_alarm_found['threshold']}%***")
                logging.warning(f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {highest_cpu_alarm_found['threshold']}%***")
            
            # Memory
            highest_memory_alarm_found = None

            for current_alarm in all_alarms:
                if current_alarm["type"] == "Memory-alarm":
                    if current_alarm["threshold"] <= system.memory_percent:
                        if highest_memory_alarm_found == None:
                            highest_memory_alarm_found = current_alarm
                        elif current_alarm["threshold"] > highest_memory_alarm_found["threshold"]:
                            highest_memory_alarm_found = current_alarm

            if highest_memory_alarm_found is not None:
                print(f"***WARNING, ALARM ACTIVATED, MEMORY USAGE OVER {highest_memory_alarm_found['threshold']}%***")
                logging.warning(f"***WARNING, ALARM ACTIVATED, MEMORY USAGE OVER {highest_memory_alarm_found['threshold']}%***")

            # Storage
            highest_storage_alarm_found = None

            for current_alarm in all_alarms:
                if current_alarm["type"] == "Storage-alarm":
                    if current_alarm["threshold"] <= system.storage_percent:
                        if highest_storage_alarm_found == None:
                            highest_storage_alarm_found = current_alarm
                        elif current_alarm["threshold"] > highest_storage_alarm_found["threshold"]:
                            highest_storage_alarm_found = current_alarm

            if highest_storage_alarm_found is not None:
                print(f"***WARNING, ALARM ACTIVATED, STORAGE USAGE OVER {highest_storage_alarm_found['threshold']}%***")
                logging.warning(f"***WARNING, ALARM ACTIVATED, STORAGE USAGE OVER {highest_storage_alarm_found['threshold']}%***")

            if utils.wait_for_any_key_or_timeout(5):
                loop = False
                break
                