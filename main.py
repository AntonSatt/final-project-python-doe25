'''
This is a monitoring program for CPU, Memory and Storage data.
It also features alarms and a monitoring mode.
'''
import logging
import sys
import utils
import monitoring
import alarm

def starting_menu():
    utils.clear_console()
    print("1 - Start monitoring\n"
          "2 - List monitoring\n"
          "3 - Create or remove alarms\n"
          "4 - Show alarms\n"
          "5 - Monitoring mode\n"
          "6 - Quit the program")

def main():
    logging.info("Starting the program.") # Logging the start
    alarm.load_alarms()
    starting_menu_user_input()

def starting_menu_user_input():
    while True:
        starting_menu()
        user_choice = input("Pick from the list above: ")
        if user_choice == '1':
            monitoring.start_monitoring()
        elif user_choice == '2':
            monitoring.show_monitoring_list()
        elif user_choice == '3':
            alarm.alarm_start()
        elif user_choice == '4':
            alarm.show_alarms()
            utils.press_any_key()
        elif user_choice == '5':
            monitoring.monitoring_mode()
        elif user_choice == '6':
            utils.clear_console()
            logging.info("Closing the program")
            sys.exit()
        else:
            print("Not valid option.")
            utils.timer_short()

if __name__ == "__main__":
    main()