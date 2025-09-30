import utils

class SystemAlarm:
    def __init__(self): #variables we need to change
        self.cpu_alarm_value = None
        self.mem_alarm_value = None
        self.disk_alarm_value = None
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
                self.cpu_alarm_value = self.set_alarm(self.cpu_alarm_value)
            elif self.user_choice == '2':
                self.mem_alarm_value = self.set_alarm(self.mem_alarm_value)
            elif self.user_choice == '3':
                self.disk_alarm_value = self.set_alarm(self.disk_alarm_value)
            elif self.user_choice == '4':
                print("Returning to main menu.")
                utils.short_timer()
                break
            else:
                continue
        return
    
    def set_alarm(self, alarm_value):
        while(True):
            try:
                alarm_value = int(input("Pick a number from 0-100: "))
                if not 0 <= alarm_value <= 100:
                    print("Please enter a number between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number from 0-100.")
        print(f"Alarm set to {alarm_value}%.")
        utils.short_timer()
        return alarm_value
    
# Making alarm global 
alarm = SystemAlarm()