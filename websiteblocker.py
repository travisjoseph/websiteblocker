import time
from tkinter import *
import gui
from datetime import datetime as dt

hostsPath="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.reddit.com","reddit.com"]

root = Tk()
root.title("Website Blocker")
gui.makeGUI(root)
root.mainloop()


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        with open(hostsPath, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        time.sleep(300)
    else:
        with open(hostsPath, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        time.sleep(300)
