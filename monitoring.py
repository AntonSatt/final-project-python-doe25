# This program runs the monitoring
import psutil
import time

def monitoring():
    cpu_usage = psutil.cpu_times_percent(interval=1)
    print(f"System cpu usage: {cpu_usage}")
    input("enter to quit")