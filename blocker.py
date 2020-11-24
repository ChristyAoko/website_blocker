# To import time module
import time
# To import datetime class form datetime module
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="/etc/hosts"
# IP where browse visit will redirect to
redirect="127.0.0.1"
# Domains user wants to block
website_list=["www.facebook.com","facebook.com","www.twitter,com"]

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):
        #Prints between 8am and 4pm
        print("Working hours....")
        # Reads and appends the file
        with open(hosts_path,'r+') as file:
            # Loads file in content variable
            content=file.read()
            # Checks for domains in the list
            for website in website_list:
                if website in content:
                    pass
                else:
                    # Adds the domains to the host file
                    file.write(redirect+""+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            # Iterates through the content list
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        # Prints after 4pm and before 8am
        print("Fun hours....")
    # Prints every 5 seconds
    time.sleep(5)          
