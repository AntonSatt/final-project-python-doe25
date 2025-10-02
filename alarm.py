import utils

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
              "4. Back to main menu")
        self.user_choice = input("Pick an option from 1-4 above: ")

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
    
# Making alarm global 
alarm = SystemAlarm()