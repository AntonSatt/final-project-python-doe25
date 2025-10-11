# Monitoring application 
import sys
import monitoring
from monitoring import logging
import utils
import alarm
import time


# Shows the starting menu
def starting_menu():
    utils.clear_console()
    logging.info("Starting the program.") # Logging the start
    print(('Welcome to the program, pick an option below!\n'
           '1 - to start monitoring your computers usage.\n'
           '2 - to show a list what you are monitoring.\n'
           '3 - to create an alarm.\n'
           '4 - to show all current alarms.\n'
           '5 - to start monitoring mode.\n'
           '6 - to exit the program.\n'))


# Checks if monitoring is started in monitoring.py, if started returns formated data. 
def show_monitoring_status():
    utils.clear_console()
    status = monitoring.monitor.get_status()
    print(status)
    utils.press_any_key()


def get_alarm_value():
    while True:
        try:
            alarm_value = int(input("Pick a number from 0-100: "))
            if 0 <= alarm_value <= 100:
                return alarm_value
            print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number from 0-100.")


def alarm_menu():
    while True:
        utils.clear_console()
        print("Configure alarm\n"
              "1. CPU-usage\n"
              "2. Memory usage\n"
              "3. Disk usage\n"
              "4. Remove an alarm\n"
              "5. Back to main menu")
        user_choice = input("Pick an option from 1-5 above: ")
        if user_choice == '1':
            value = get_alarm_value()
            alarm.alarm.add_cpu_alarm(value)
            print(f"Alarm added to list: {value}%.")
            logging.info(f"Alarm added to list: {value}%.")
            utils.short_timer()
        elif user_choice == '2':
            value = get_alarm_value()
            alarm.alarm.add_mem_alarm(value)
            print(f"Alarm added to list: {value}%.")
            logging.info(f"Alarm added to list: {value}%.")
            utils.short_timer()
        elif user_choice == '3':
            value = get_alarm_value()
            alarm.alarm.add_disk_alarm(value)
            print(f"Alarm added to list: {value}%.")
            logging.info(f"Alarm added to list: {value}%.")
            utils.short_timer()
        elif user_choice == '4':
            remove_alarm_menu()
        elif user_choice == '5':
            print("Returning to main menu.")
            utils.short_timer()
            break
        else:
            print("Invalid choice. Try again.")
            utils.short_timer()


def remove_alarm_menu():
    utils.clear_console()
    all_alarms = []
    all_alarms.extend([('cpu', v) for v in alarm.alarm.cpu_alarms])
    all_alarms.extend([('mem', v) for v in alarm.alarm.mem_alarms])
    all_alarms.extend([('disk', v) for v in alarm.alarm.disk_alarms])
    if not all_alarms:
        print("No alarms configured to remove.")
        utils.press_any_key()
        return
    print("Pick an alarm to remove: ")
    for i, (typ, value) in enumerate(all_alarms, start=1):
        if typ == 'cpu':
            print(f"{i}. CPU-alarm {value}%")
        elif typ == 'mem':
            print(f"{i}. Memory-alarm {value}%")
        elif typ == 'disk':
            print(f"{i}. Disk-alarm {value}%")
    try:
        choice = int(input("> ")) - 1
        if 0 <= choice < len(all_alarms):
            typ, value = all_alarms[choice]
            removed = alarm.alarm.remove_alarm(typ, value)
            if removed:
                if typ == 'cpu':
                    desc = f"CPU-alarm {value}%"
                elif typ == 'mem':
                    desc = f"Memory-alarm {value}%"
                else:
                    desc = f"Disk-alarm {value}%"
                print(f"Removed: {desc}")
                logging.info(f"Alarm removed: {desc}")
            else:
                print("Alarm not found.")
        else:
            print("That number doesn't exist.")
    except ValueError:
        print("Enter a valid number.")
    utils.press_any_key()


def show_alarms():
    utils.clear_console()
    if alarm.alarm.cpu_alarms:
        print("CPU alarms:")
        for a in alarm.alarm.cpu_alarms:
            print(f"CPU-alarm {a}%")
    if alarm.alarm.mem_alarms:
        print("Memory alarms:")
        for a in alarm.alarm.mem_alarms:
            print(f"Memory-alarm {a}%")
    if alarm.alarm.disk_alarms:
        print("Disk alarms:")
        for a in alarm.alarm.disk_alarms:
            print(f"Disk-alarm {a}%")
    utils.press_any_key()


def monitoring_mode():
    utils.clear_console()
    logging.info("Monitoring mode activated.")
    print("Monitoring mode activated, press any key to go back to menu.")
    while True:
        monitoring.monitor.update_data()
        for aw in alarm.alarm.cpu_alarms:
            if monitoring.monitor.cpu_usage >= aw:
                msg = f"***WARNING, ALARM ACTIVATED, CPU USAGE OVER {aw}%***"
                print(msg)
                logging.warning(msg)
        for aw in alarm.alarm.mem_alarms:
            if monitoring.monitor.memory_percent >= aw:
                msg = f"***WARNING, ALARM ACTIVATED, MEMORY USAGE OVER {aw}%***"
                print(msg)
                logging.warning(msg)
        for aw in alarm.alarm.disk_alarms:
            if monitoring.monitor.storage_percent >= aw:
                msg = f"***WARNING, ALARM ACTIVATED, DISK USAGE OVER {aw}%***"
                print(msg)
                logging.warning(msg)
        if utils.wait_for_any_key_or_timeout(10):
            break


def main():
    while True:
        starting_menu()
        user_selection = input("Please pick an option from 1-6 above. ")
        if user_selection == '1':
            if monitoring.monitor.is_running:
                print("Already running...")
                utils.short_timer()
            else:
                utils.typing_effect("Starting up monitoring...")
                utils.short_timer()
                monitoring.monitor.start()
                utils.typing_effect("...monitoring started, going back to main menu in 2 seconds. \n")
                utils.short_timer()
                print("Thread started!")
        elif user_selection == '2':
            show_monitoring_status()
        elif user_selection == '3':
            alarm_menu()
        elif user_selection == '4':
            show_alarms()
        elif user_selection == '5':
            monitoring_mode()
        elif user_selection == '6':
            logging.info("Closing the program.") # Logging the exit
            print("Closing the program.")
            utils.short_timer()
            sys.exit()
        else:
            print("Choice not vaild. Please choose from a menu of 1-5", end='')
            utils.short_timer()


# Runs back to main when script is executed directly
if __name__ == "__main__":
    main()