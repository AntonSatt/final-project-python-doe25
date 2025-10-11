'''
This is a monitoring program for CPU, Memory and Storage data.
It also features alarms and a monitoring mode.
'''
import logging
import sys
import time
import utils
import monitoring

def starting_menu():
    utils.clear_console()
    print("1 - Start monitoring\n"
          "2 - List monitoring\n"
          "3 - Create or remove alarms\n"
          "4 - Show alarms\n"
          "5 - Monitoring mode\n"
          "6 - Quit the program")


def main():
    while True:
        starting_menu()
        user_choice = input("Pick from the list above: ")
        if user_choice == '1':
            monitoring.start_monitoring()
        elif user_choice == '2':
            monitoring.show_monitoring_list()
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            pass
        elif user_choice == '6':
            sys.exit()
        else:
            print("Not valid option.")
            utils.timer_short()


if __name__ == "__main__":
    main()