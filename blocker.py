import time                                     #imports time module
from datetime import datetime as dt             #imports datetime class from datetime module

hosts_temp="hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"                            #IP where browse visit will be redirected to
website_list=["www.facebook.com","facebook.com","www.twitter,com"]  #domains you want to block

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):
        print("Working hours....")              #prints between 8am and 4pm
        with open(hosts_path,'r+') as file:     #reads and appends the file
            content=file.read()                 #loads file in content variable
            for website in website_list:        #checks for domains in the list
                if website in content:
                    pass
                else:
                    file.write(redirect+""+ website+"\n")           #adds the domains to the host file
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:                #iterates through the content list
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours....")                  #prints after 4pm and before 8am
    time.sleep(5)                               #prints every 5 seconds
