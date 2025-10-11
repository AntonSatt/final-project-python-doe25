'''
This is a monitoring program for CPU, Memory and Storage data.
It also features alarms and a monitoring mode.
'''
import logging
import time


def starting_menu():
    print("1 - Start monitoring",
          "2 - List monitoring",
          "3 - Create or remove alarms",
          "4 - Show alarms",
          "5 - Monitoring mode",
          "6 - Quit the program")


def main():
    starting_menu()
    user_choice = input("Pick from the list above: ")
    if user_choice == '1':
        pass
    if user_choice == '2':
        pass
    if user_choice == '3':
        pass
    if user_choice == '4':
        pass
    if user_choice == '5':
        pass
    if user_choice == '6':
        pass
    else:
        print("Not valid option.")
        time.sleep(1)