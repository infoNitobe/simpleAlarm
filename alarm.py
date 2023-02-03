import datetime
import time

class alarm:
    SECONDS_IN_A_DAY = 86400

    def set_alarm(self, id, configured_value):
        seconds_until_alarm = self.__get_seconds_until_alarm(configured_value)
        if seconds_until_alarm < 0:
            seconds_until_alarm += self.SECONDS_IN_A_DAY

        print(f"[id = {id}] Alarm is set!")
        print("The alarm will ring at %s" % datetime.timedelta(seconds=seconds_until_alarm))
        time.sleep(seconds_until_alarm)
        print(f"[id = {id}] time to wake up!!!")
    
    def __get_seconds_until_alarm(self, configured_value):
        #e.g. covert h:mm to [h:mm]
        alarm_time = [int(n) for n in configured_value.split(":")]

        #validate
        if 0 < alarm_time[0] <= 24:
            pass
        elif 0 < alarm_time[1] <= 60:
            pass
        else:
            print("invalid time")
            return

        # Number of seconds in an Hour, Minute
        seconds_hms = [3600, 60]
        alarm_time_in_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

        now = datetime.datetime.now()
        now_in_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

        seconds_until_alarm = alarm_time_in_seconds - now_in_seconds
        
        return seconds_until_alarm
    
    def print_sumthing(self, id):
        print(f"test of {id}")