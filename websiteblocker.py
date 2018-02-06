import time
import backend
from datetime import datetime as dt
from tkinter import *

tmpHosts="hosts"
#hostsPath="/etc/hosts"
redirect="127.0.0.1"
website_list=[]
time_list=['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00',
           '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30',
           '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00',
           '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30',
           '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
           '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30',
           '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']

#  -----
# //GUI\\
#  -----
window = Tk()
window.title("Website Blocker")

#Start and end times
lbl_StartTime=Label(window, text="Start Time: ")
lbl_StartTime.grid(row=0, column=0)
StartTime = StringVar()
StartTime.set(time_list[0])
om_StartTime = OptionMenu(window, StartTime, *time_list)
om_StartTime.grid(row=0, column=1)
lbl_EndTime=Label(window, text="End Time: ")
lbl_EndTime.grid(row=0, column=2)
EndTime = StringVar()
EndTime.set(time_list[0])
om_EndTime = OptionMenu(window, EndTime, *time_list)
om_EndTime.grid(row=0, column=3)

#Blocked address list
lbl_blocked=Label(window, text="Blocked Website List")
lbl_blocked.grid(row=1, column=0, columnspan=4)
siteList=StringVar()
lst_siteList=Listbox(window, width=25, height=5)
lst_siteList.grid(row=2, column=1, rowspan=2, columnspan=3)
scrl_addressList=Scrollbar(window)
scrl_addressList.grid(row=2, column=0, rowspan=2)
lst_siteList.configure(yscrollcommand=scrl_addressList.set)
scrl_addressList.configure(command=lst_siteList.yview)

#List Actions
address=StringVar()
ent_address=Entry(window, textvariable=address)
ent_address.grid(row=4, column=0, rowspan=2, columnspan=3)
#Add Address
btn_addAddress=Button(window, text="Add")
btn_addAddress.grid(row=6, column=0, columnspan=2)
#Update Address
btn_addAddress=Button(window, text="Update")
btn_addAddress.grid(row=6, column=2)
#Remove Entry
btn_removeEntry=Button(window, text="Delete")
btn_removeEntry.grid(row=5, column=3)
#Search for website
btn_searchEntry=Button(window, text="Search")
btn_searchEntry.grid(row=4, column=3)


#Run Script
btn_start=Button(window, text="Run")
btn_start.grid(row=6, column=3)
window.mainloop()

# while True:
#     if dt(dt.now().year,dt.now().month,dt.now().day, 15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 20):
#         with open(tmpHosts, 'r+') as file:
#             content=file.read()
#             for website in website_list:
#                 if website in content:
#                     pass
#                 else:
#                     file.write(redirect + " " + website + "\n")
#         time.sleep(300)
#     else:
#         with open(tmpHosts, 'r+') as file:
#             content=file.readlines()
#             file.seek(0)
#             for line in content:
#                 if not any(website in line for website in website_list):
#                     file.write(line)
#             file.truncate()
#         time.sleep(300)
