# Monitering application 
import sys
import monitoring
from monitoring import logging
import utils
import alarm


# Shows the starting menu
def starting_menu():
    utils.clear_console()
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

def main():
    logging.info("Starting the program.") # Logging the start
    while True:
        starting_menu()
        user_selection = input("Please pick an option from 1-6 above. ")
        if user_selection == '1':
            monitoring.monitor.start()
        elif user_selection == '2':
            show_monitoring_status()
        elif user_selection == '3':
            alarm.alarm.alarm_menu()
        elif user_selection == '4':
            alarm.alarm.show_alarms()
        elif user_selection == '5':
            monitoring.monitor._check_alarms()
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