'''
This is a monitoring program for CPU, Memory and Storage data.
It also features alarms and a monitoring mode.
'''
import utils
import monitoring
import alarm
import logger_config
import logging

def starting_menu():
    utils.clear_console()
    print("1 - Start monitoring\n"
          "2 - List monitoring\n"
          "3 - Create or remove alarms\n"
          "4 - Show alarms\n"
          "5 - Monitoring mode\n"
          "6 - Quit the program")

def main():
    logger_config.setup_logging()
    logging.info("Booting start-menu!")
    alarm.load_alarms()
    starting_menu_user_input()
    

def starting_menu_user_input():
    while True:
        starting_menu()
        user_choice = input("Pick from the list above: ")
        match user_choice:
            case '1':
                monitoring.start_monitoring()
            case '2':
                monitoring.show_monitoring_list()
            case '3':
                alarm.alarm_start()
            case '4':
                alarm.show_alarms()
                utils.press_any_key()
            case '5':
                monitoring.monitoring_mode()
            case '6':
                utils.clear_console()
                logging.info("Closing the program")
                break
            case _:
                print("Not valid option.")
                utils.timer_short()
  

if __name__ == "__main__":
    main()