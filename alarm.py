class SystemAlarm:
    def __init__(self): #variables we need to change
        self.cpu_alarms = [] # We need lists to be able to store multiple alarms
        self.mem_alarms = []
        self.disk_alarms = []

    def add_cpu_alarm(self, threshold):
        self.cpu_alarms.append(threshold)

    def add_mem_alarm(self, threshold):
        self.mem_alarms.append(threshold)

    def add_disk_alarm(self, threshold):
        self.disk_alarms.append(threshold)

    def remove_alarm(self, alarm_type, threshold):
        removed = False
        if alarm_type == 'cpu':
            if threshold in self.cpu_alarms:
                self.cpu_alarms.remove(threshold)
                removed = True
        elif alarm_type == 'mem':
            if threshold in self.mem_alarms:
                self.mem_alarms.remove(threshold)
                removed = True
        elif alarm_type == 'disk':
            if threshold in self.disk_alarms:
                self.disk_alarms.remove(threshold)
                removed = True
        return removed
    

# Making alarm global 
alarm = SystemAlarm()