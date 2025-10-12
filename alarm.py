'''
The part of the program takes care of the alarms.
Features like adding alarms and removing alarms,
and listing the current alarms.
'''
import utils
from main import logging
import json
import os

ALARM_FILEPATH = "alarms.json"

ALARM_SORT_ORDER = {
    "CPU-alarm": 1,
    "Memory-alarm": 2,
    "Storage-alarm": 3
}

def load_alarms():
    # Loads alarms from the JSON file or says if no list exists. 
    if os.path.exists(ALARM_FILEPATH):
        with open(ALARM_FILEPATH, 'r') as f:
            loaded_data = json.load(f)
            user_alarms.extend(loaded_data)
        print(f"Loading previously configured alarms...")
        utils.timer_short()
    else:
        print(f"No {ALARM_FILEPATH} found. Startin with a new empty alarm list.")
        utils.timer_short()
            
def save_alarms():
    # Saves alarms to the JSON file.
    with open(ALARM_FILEPATH, 'w') as f:
        json.dump(user_alarms, f, indent=4)
        logging.info("Alarms saved succesfully.")
        

# Filled list for testing, removed when pushed to production.
user_alarms = [
    
]

def remove_alarm():

    while True:
        sorted_list = sort_alarms()

        if not sorted_list:
            print("No alarms to remove.")
            utils.timer_short()
            return
        
        show_alarms()
        user_input = input(f"Enter the number of the alarm to remove (1-{len(sorted_list)}):")

        try:
            selection_number = int(user_input)

            if 1 <= selection_number <= len(sorted_list):
                index_to_remove = selection_number - 1
                alarm_to_remove = sorted_list[index_to_remove]
                user_alarms.remove(alarm_to_remove)
                save_alarms() # <--- SAVE ALARMS
                logging.warning(f"Removed alarm: {alarm_to_remove['type']} at {alarm_to_remove['threshold']}%")
                print(f"Alarm {selection_number} ({alarm_to_remove['type']} {alarm_to_remove['threshold']}%) removed.")
                utils.timer_short() 
                break 
            else:
                print(f"Invalid choice. Selection must be between 1 and {len(sorted_list)}.")
                utils.timer_short()

        except ValueError:
            print("Invalid input. Please enter a valid number")
            utils.timer_short()




def create_alarm(type_of_alarm):
    # Prompts the user for threshold and adds a new alarm to the list.
    while True:
        try:
            threshold = int(input("Type a number from 0-100: "))
            if not 0 <= threshold <= 100:
                print("Please enter a number between 0 and 100.")
                utils.timer_short()
                continue
            new_alarm = {
                "type": type_of_alarm,
                "threshold": threshold
                }
            user_alarms.append(new_alarm)
            save_alarms() # <--- SAVE ALARMS
            logging.info(f"Added {type_of_alarm} {threshold}%")
            print(f"Added {type_of_alarm} {threshold}%")
            utils.timer_short()
            return
        except ValueError:
            print("Invalid input, please enter a valid number between 0-100.")

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
            create_alarm("CPU-alarm")
        elif user_choice== '2':
            create_alarm("Memory-alarm")
        elif user_choice== '3':
            create_alarm("Storage-alarm")
        elif user_choice == '4':
            remove_alarm()
        elif user_choice == '5':
            print("Returning to main menu.")
            utils.timer_short()
            break
        else:
            print("Invalid choice. Try again.")
            utils.timer_short()
            continue

def sort_alarms():
    sorted_alarms = sorted(user_alarms, key=lambda alarm: ALARM_SORT_ORDER.get(alarm["type"], 4))
    return sorted_alarms

def show_alarms():
    utils.clear_console()
    sorted_list = sort_alarms()

    if not sorted_list:
        print("No alarms currently.")
        return

    for index, alarm in enumerate(sorted_list):
        user_number = index + 1

        alarm_type = alarm["type"]
        alarm_threshold = alarm["threshold"]

        print(f"{user_number}. {alarm_type} {alarm_threshold}%")
        
    

