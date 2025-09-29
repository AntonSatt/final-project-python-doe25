# Monitering application 
import os
import threading
import monitoring


# Shows the starting menu
def starting_menu():
    clear_console()
    print(('Welcome to the program, pick an option below!\n'
           '1 - to start monitoring your computers usage.\n'
           '2 - to show a list what you are monitoring.\n'
           '3 - to create an alarm.\n'
           '4 - to show all current alarms.\n'
           '5 - to start monitoring mode.\n'))

# Clears the console for a better viewing exerience
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    MENU_START = True
    while MENU_START:
        starting_menu()
        user_selection = input("Please pick an option from 1-5 above. ")
        if user_selection == '1':
            monitoring.monitoring(start=True)
        elif user_selection == '2':
            monitoring.monitoring()
        elif user_selection == '3':
            print()
        elif user_selection == '4':
            print()
        elif user_selection == '5':
            print()
        else:
            print()
    


# Runs back to main when script is executed directly
if __name__ == "__main__":
    main()