import time
from datetime import datetime as dt

hostsPath="/etc/hosts"
redirect="127.0.0.1"
website_lists=["www.facebook.com","facebook.com","www.reddit.com","reddit.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        print("Working Hours")
        time.sleep(5)
    else:
        print("Fun Hours...")
        time.sleep(5)
