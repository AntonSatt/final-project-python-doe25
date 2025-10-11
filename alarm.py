'''
The part of the program takes care of the alarms.
Features like adding alarms and removing alarms,
and listing the current alarms.
'''
import utils

class Alarm():
    def __init__(self):
        pass



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
            pass
        elif user_choice== '2':
            pass
        elif user_choice== '3':
            pass
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