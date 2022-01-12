# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import time
import datetime
import os

# current_time = int(time.strftime("%H:%M:%S"))

desktop_path = "C:/Users/timtu/Desktop"

current_path = os.getcwd()

if (current_path != desktop_path):
    os.chdir(desktop_path)

    items = []

    items.append(os.listdir())

    for item in items:
        if os.path.getsize(item) < 14:
            os.system('del'+item)
            print("Deleted" + item)

# //list the directories/files in the desktop path that are less than 14 bytes

# gets the current time in HH:MM:SS format
current_time = datetime.datetime.now()

# //gets current hour in 24 hr format
hour = current_time.hour

time_range = range(15, 18)

while (hour in time_range):
    print("You can delete files now")