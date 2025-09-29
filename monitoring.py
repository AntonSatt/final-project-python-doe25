# This program runs the monitoring
import psutil
import time
import threading

def monitoring(start=False):
    
    monitoring_status = start
    if not monitoring_status:
        print("Monitoring not started.")
        time.sleep(2)
        return None

    #Just fancy text to let the user know that the monitoring has started. 
    matrix_text = "Starting up monitoring..."
    matrix_text_2 = "...monitoring started, going back to main menu in 2 seconds. \n"
    for x in matrix_text:
        print(x, end='', flush=True)
        time.sleep(0.05)
    for x in range(3):
        print(".")
        time.sleep(0.5)
    for x in matrix_text_2:
        print(x, end='', flush=True)
        time.sleep(0.05)
    time.sleep(2)

    while monitoring_status:
    
        # To convert to GB from Byte
        GB_FACTOR = 1024**3
        
        # Check's the CPU usage
        cpu_data = psutil.cpu_times_percent(interval=None)
        # CPU usages calculation
        cpu_idle = cpu_data.idle
        cpu_usage = 100 - cpu_idle
        print(f"CPU-användning: {round(cpu_usage)}%")

        # Check's the memory
        memory = psutil.virtual_memory()
        
        # Convert used memory to GB
        byte_used_value = memory.used
        used_memory_in_GB = byte_used_value / GB_FACTOR
        # Convert total memory to GB
        byte_total_value = memory.total
        total_memory_in_GB = byte_total_value / GB_FACTOR
        print(f"Minnesanvändning: {memory.percent}% ({used_memory_in_GB:.1f} GB av {total_memory_in_GB:.1f} GB använt)")

        # Check's the storage
        storage = psutil.disk_usage('/')
        # Calculate storage usage to GB
        storage_used_value = storage.used
        storage_used_in_GB = storage_used_value / GB_FACTOR
        # Calculate storage total to GB
        storage_total_value = storage.total
        storage_total_in_GB = storage_total_value / GB_FACTOR
        print(f"Diskanvändning: {storage.percent}% ({round(storage_used_in_GB)} GB av {round(storage_total_in_GB)} GB använt)")

        # How often we run for new data
        time.sleep(10)
