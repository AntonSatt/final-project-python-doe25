'''
The part of the program takes care of the alarms.
Features like adding alarms and removing alarms,
and listing the current alarms.
'''
import utils
from main import logging

# Filled list for testing, removed when pushed to production.
user_alarms = [
    {"type": "CPU-alarm", "threshold": 5},
    {"type": "Memory-alarm", "threshold": 10},
    {"type": "Storage-alarm", "threshold": 10},
    {"type": "CPU-alarm", "threshold": 12}
]

def create_cpu_alarm():
    threshold = int(input("Please put in number: "))
    new_alarm = {
        "type": "CPU-alarm",
        "threshold": threshold
        }
    user_alarms.append(new_alarm)
    logging.info(f"Added CPU-alarm {threshold}%")

def create_memory_alarm():
    threshold = int(input("Please put in number: "))
    new_alarm = {
        "type": "Memory-alarm",
        "threshold": threshold
    }
    user_alarms.append(new_alarm)
    logging.info(f"Memory CPU-alarm {threshold}%")
    
def create_storage_alarm():
    threshold = int(input("Please put in number: "))
    new_alarm = {
        "type": "Storage-alarm",
        "threshold": threshold
    }
    user_alarms.append(new_alarm)
    logging.info(f"Added Storage-alarm {threshold}%")

def alarm_menu():
    utils.clear_console()
    print("Configure alarm\n"
            "1. CPU-usage\n"
            "2. Memory usage\n"
            "3. Disk usage\n"
            "4. Remove an alarm\n"
            "5. Back to main menu")
    user_choice = input("Pick an option from 1-5 above: ")
    return user_choice

def alarm_start():
    while True:
        user_choice = alarm_menu()
        if user_choice == '1':
            create_cpu_alarm()
        elif user_choice== '2':
            create_memory_alarm()
        elif user_choice== '3':
            create_storage_alarm()
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            print("Returning to main menu.")
            utils.timer_short()
            break
        else:
            print("Invalid choice. Try again.")
            utils.timer_short()
            continue

def show_alarms():
    utils.clear_console()
    sorted_alarms = sorted(user_alarms, key=lambda alarm: alarm["type"])
    for index, alarm in enumerate(sorted_alarms):
        user_number = index + 1

        alarm_type = alarm["type"]
        alarm_threshold = alarm["threshold"]

        print(f"{user_number}. {alarm_type} {alarm_threshold}%")
        
    utils.press_any_key()