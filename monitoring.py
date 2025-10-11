# This program runs the monitoring
import logging
import time
import threading
import utils
import alarm
import psutil

logging.basicConfig(filename='alarms.log', level=logging.INFO, format='%(asctime)s %(message)s')

class SystemMonitor:
    
    def __init__(self):
        self.cpu_usage = 0
        self.memory_percent = 0
        self.total_memory_in_GB = 0
        self.used_memory_in_GB = 0
        self.storage_used_in_GB = 0
        self.storage_total_in_GB = 0
        self.storage_percent = 0
        self.is_running = False
        self.stop_event = threading.Event()
        self.thread = None

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

    # How often the data is gonna update    
    def _monitoring_loop(self):
        while not self.stop_event.is_set():
            self.update_data()
            time.sleep(10)

    def start(self):
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.thread.start()
        self.is_running = True
        return self

    def get_status(self):
        # Get the current data as a string for printing in main.py
        if not self.is_running:
            return "Nothing is being monitored currently."
        return(f"CPU-användning: {round(self.cpu_usage)}%\n"
               f"Minnesanvändning: {self.memory_percent}% ({self.used_memory_in_GB:.1f} GB av {self.total_memory_in_GB:.1f} GB använt)\n"
               f"Diskanvändning: {self.storage_percent}% ({round(self.storage_used_in_GB)} GB av {round(self.storage_total_in_GB)} GB använt)")


    
# To be able to call easy globaly
monitor = SystemMonitor()