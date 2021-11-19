#!/usr/bin/env python3
import shutil #module in which there is disk_usage function
import psutil #module in which there is cpu_percent function


#disk usage check function
def check_disk(disk):
    du = shutil.disk_usage('/') #stock disk usage info (total, free, used)
    free_space = (du.free/du.total)*100
    return free_space > 20 #good if the free space is grater than 20%

# cpu utilization check function
def check_cpu():
    cpu_usage = psutil.cpu_percentage(1)
    return cpu_usage < 75 #good if the cpu utlzation is less than 75%

#main body of the script
if not check_disk("/") or not check_cpu():
    print("ounhmmm we got a problem :(")
else:
    prin("ouff !!! Everything is OK :)")




du_read = "{:.2f}".format(du_read)
print("{}% disk space is used".format(du_read))
