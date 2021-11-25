with open("hr_system.txt") as HR_list:
    for line in HR_list:
        clean_line = line.split()
        names = clean_line[0]
        job_title = clean_line[2]
        print(f"Name: {names} \nJob Title: {job_title}\n")