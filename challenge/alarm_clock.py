# Create an Alarm clock
# Create a function called alarm that sets an alarm clock for the user. The function should ask the user to enter time they want the alarm to go off. The user should enter the hour and minute. The function should then print out the time when the alarm will go off. When its alarm time, the code should let off a sound. Use the winsound module for sound.


import winsound 
import datetime
import time


def set_alarm(): # Enter hour
    hour = input("Please enter hour: ") # Enter minute
    minute = input("Please enter minute: ") # concatenate hour and minute 
    seconds =input("Please enter seconds: ")
    alarm_time = hour + ':' + minute + ':' + seconds
    # let the user know the alarm time set 
    print("You have set alarm for ", alarm_time)
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        # print(alarm_time)
        print(now)
        if alarm_time == now:
            print("Wake up") 
            print("Wake up") 
            print("Wake up")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            break


set_alarm()
