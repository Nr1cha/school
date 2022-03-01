import csv

def main():
    student_list = read_list("CSE_111/9/students.csv")
    print(student_list)
    next(student_list)
    student_list.pop(0)
    student_list.pop()

    for i in range(len(student_list)):
        if student_list[i] == "AB":
            student_list[i] = "Alberta"

    count = student_list.count("Alberta")
    print()
    print(f"Alberta occurs {count} times in the modified list.")





def read_list(filename):
    
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            # clean_line.pop("AB")
            text_list.append(clean_line)



    return text_list



if __name__ == "__main__":
    main()
