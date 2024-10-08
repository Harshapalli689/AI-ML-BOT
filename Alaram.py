import os
def alarm(Data):
    timehere = open("Alarmtext.txt","a")
    timehere.write(Data)
    timehere.close()
    os.startfile("alarm.py")