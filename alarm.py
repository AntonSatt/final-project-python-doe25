import utils
from monitoring import logging


class SystemAlarm:
    def __init__(self): #variables we need to change
        self.cpu_alarms = [] # We need lists to be able to store multiple alarms
        self.mem_alarms = []
        self.disk_alarms = []
        self.user_choice = None

    def alarm_menu_text(self):
        print("Configure alarm\n"
              "1. CPU-usage\n"
              "2. Memory usage\n"
              "3. Disk usage\n"
              "4. Remove an alarm\n"
              "5. Back to main menu")
        self.user_choice = input("Pick an option from 1-5 above: ")

    def alarm_menu(self):
        alarm_loop = True
        
        while alarm_loop:
            utils.clear_console()
            self.alarm_menu_text()
            if self.user_choice == '1':
                self.add_alarm_to_list(self.cpu_alarms)
            elif self.user_choice == '2':
                self.add_alarm_to_list(self.mem_alarms)
            elif self.user_choice == '3':
                self.add_alarm_to_list(self.disk_alarms)
            elif self.user_choice == '4':
                self.remove_alarm()
            elif self.user_choice == '5':
                print("Returning to main menu.")
                utils.short_timer()
                break
            else:
                print("Invalid choice. Try again.")
                utils.short_timer()
                continue
        return
    
    def add_alarm_to_list(self, alarm_list):
        new_value = self.set_alarm()
        alarm_list.append(new_value)
        print(f"Alarm added to list: {new_value}%.")
        # Logging when new alarm added
        logging.info(f"Alarm added to list: {new_value}%.")
        utils.short_timer()

    def set_alarm(self):
        while True:
            try:
                alarm_value = int(input("Pick a number from 0-100: "))
                if not 0 <= alarm_value <= 100:
                    print("Please enter a number between 0 and 100.")
                    continue
                return alarm_value
            except ValueError:
                print("Invalid input. Please enter a number from 0-100.")

    def show_alarms(self): # If list is empty the if statement makes sure it doesn't print
        utils.clear_console()
        if self.cpu_alarms: # An empty list in Python is counted as False
            for alarm in self.cpu_alarms:
                print(f"CPU-larm {alarm}%")
        if self.mem_alarms:
            for alarm in self.mem_alarms:
                print(f"Minneslarm {alarm}%")
        if self.disk_alarms:
            for alarm in self.disk_alarms:
                print(f"Disklarm {alarm}%")
        utils.press_any_key()
        return
    
    def remove_alarm(self): #Remove an alarm function
        utils.clear_console()
        # Temperary list to to store all alarms.
        all_alarms = []
        all_alarms.extend([(value, 'cpu') for value in self.cpu_alarms])
        all_alarms.extend([(value, 'mem') for value in self.mem_alarms])
        all_alarms.extend([(value, 'disk') for value in self.disk_alarms])

        # If no alarms, return to menu
        if not all_alarms:
            print("No alarms configured to remove.")
            utils.press_any_key()
            return
    
        # Checks the temp list of all alarms 
        print("Pick an alarm to remove: ")
        # With enumerate we can add an number for the list, we start at 1
        for i, (value, alarm_type) in enumerate(all_alarms, start=1):
            if alarm_type == 'cpu':
                print(f"{i}. CPU-alarm {value}%")
            elif alarm_type == 'mem':
                print(f"{i}. Memory-alarm {value}%")
            elif alarm_type == 'disk':
                print(f"{i}. Disk-alarm {value}%")
        
        try:
            choice = int(input("> ")) - 1  # Convert to 0 for index
            if 0 <= choice < len(all_alarms):
                # Picks out the alarm value (exampel 50) and the alarm type from all_alarms.
                removed_value, alarm_type = all_alarms[choice]
                # Checks alarm type (exampel cpu) and remove the value that was picked from the original list.
                if alarm_type == 'cpu':
                    self.cpu_alarms.remove(removed_value)
                    desc = f"CPU-alarm {removed_value}%"
                elif alarm_type == 'mem':
                    self.mem_alarms.remove(removed_value)
                    desc = f"Memory-alarm {removed_value}%"
                elif alarm_type == 'disk':
                    self.disk_alarms.remove(removed_value)
                    desc = f"Disk-alarm {removed_value}%"
                
                print(f"Removed: {desc}")
                # Loggs the removal
                logging.info(f"Alarm removed: {desc}")
            else:
                print("That number doesn't exist.")
        except ValueError:
            print("Enter a valid number.")
        
        utils.press_any_key()
        
        

    
# Making alarm global 
alarm = SystemAlarm()