import time
from datetime import datetime as dt

hostsPath_temp="hosts"
hostsPath="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.reddit.com","reddit.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        with open(hostsPath_temp, 'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        time.sleep(5)
    else:
        with open(hostsPath_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
        time.sleep(5)
