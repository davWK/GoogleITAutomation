#!/usr/bin/env python3
import sys
import csv

#populate data
source  = sys.argv[1]
report = sys.argv[2]

#Read employee data and store it into list of dictionary
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees(source)


#Process employee data and return dictionary in form of Department:number of employees
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)


#generate report file
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')

write_report(dictionary, report)
