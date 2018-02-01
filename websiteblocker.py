import time
from tkinter import *
from datetime import datetime as dt

hostsPath="/etc/hosts"
temp_host = "hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.reddit.com","reddit.com"]
hoursList = ["00", "01", "03", "04", "05", "06", "07", "08", "09", "10", "11",
             "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
minutesList = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]


root = Tk()
root.title("Website Blocker")

def getTimes():
    print(int(startHour.get()))

#START TIME
lblStart = Label(root, text = "Start Time: ")
startHour = StringVar()
startHour.set(hoursList[0])
om_startHour = OptionMenu(root, startHour, *hoursList)
startMinute = StringVar()
startMinute.set(minutesList[0])
om_startMinute = OptionMenu(root, startMinute, *minutesList)

#END TIME
lblEnd = Label(root, text = "End Time: ")
endHour = StringVar()
endHour.set(hoursList[0])
om_endHour = OptionMenu(root, endHour, *hoursList)
endMinute = StringVar()
endMinute.set(hoursList[0])
om_endMinute = OptionMenu(root, endMinute, *hoursList)

#APPLY TIME
btnApply = Button(root, text = "Apply", command = getTimes)

#GRID LAYOUT
lblStart.grid(row=0, column=0)
om_startHour.grid(row=0, column=1)
om_startMinute.grid(row=0, column=3)
lblEnd.grid(row=0, column=4)
om_endHour.grid(row=0, column=5)
om_endMinute.grid(row=0, column=6)
btnApply.grid(row=1, column=3)

root.mainloop()



while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 14) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 9):
        with open(temp_host, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        time.sleep(300)
    else:
        with open(temp_host, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        time.sleep(300)
