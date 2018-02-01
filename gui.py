from tkinter import *

hoursList = ["00", "01", "03", "04", "05", "06", "07", "08", "09", "10", "11",
             "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
minutesList = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]

def makeGUI(root):
    #START TIME
    lblStart = Label(root, text = "Start Time: ")
    startHour = StringVar()
    startHour.set(hoursList[0])
    startHour = OptionMenu(root, startHour, *hoursList)
    startMinute = StringVar()
    startMinute.set(minutesList[0])
    startMinute = OptionMenu(root, startMinute, *minutesList)


    #END TIME
    lblEnd = Label(root, text = "End Time: ")
    endHour = StringVar()
    endHour.set(hoursList[0])
    endHour = OptionMenu(root, endHour, *hoursList)
    endMinute = StringVar()
    endMinute.set(hoursList[0])
    endMinute = OptionMenu(root, endMinute, *hoursList)

    #APPLY TIME
    btnApply = Button(root, text = "Apply")


    #GRID LAYOUT
    lblStart.grid(row=0, column=0)
    startHour.grid(row=0, column=1)
    startMinute.grid(row=0, column=3)
    lblEnd.grid(row=0, column=4)
    endHour.grid(row=0, column=5)
    endMinute.grid(row=0, column=6)
    btnApply.grid(row=1, column=3)
