import os 
os.system("clear")
with open("hr_system.txt") as HR_list:
    for line in HR_list:
        clean_line = line.split()
        name = clean_line[0]
        ID_Number = clean_line[1]
        job_title = clean_line[2]
        salary = float(clean_line[3])
        divided_salary = salary / 24
        if job_title == "Engineer" and divided_salary:
            print(f"Name: {name} ID Number: ({ID_Number}), Job Title: {job_title} - ${divided_salary + 1000:.2f}\n")
        else:
            print(f"Name: {name} ID Number: ({ID_Number}), Job Title: {job_title} - ${divided_salary:.2f}\n")
        # print(f"Name: {name} ID Number: ({ID_Number}), Job Title: {job_title} - ${divided_salary:.2f}\n")