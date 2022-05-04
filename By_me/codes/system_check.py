#!/usr/bin/env python3
import shutil #module in which there is disk_usage function
import psutil #module in which there is cpu_percent function


#disk usage check function
def check_disk(disk):
    du = shutil.disk_usage('/') #stock disk usage info (total, free, used)
    free_space = (du.free/du.total)*100
    free_space = float("{:.2f}".format(free_space))
    return free_space #(< 20), #good if the free space is grater than 20%

# cpu utilization check function
def check_cpu():
    cpu_usage = psutil.cpu_percent(1)
    cpu_usage = float("{:.2f}".format(cpu_usage))
    return cpu_usage # (> 75) #good if the cpu utlzation is less than 75%


#main body of the script
if  check_disk("/") < 20 or check_cpu() > 75:
    print("We got a problem :( \nonly {} % disk space remain and CPU is used at {} %".format(check_disk("/"), check_cpu()))
else:
    print("Everything is OK :)")
