import csv

def main():
    student_name = 1
    i_index = 0

    student_list = read_dict("students.csv", i_index)
    user_input = input("what is your I# ? ")

    if user_input in student_list:
        value = student_list[user_input]
        studentName = value[student_name]
        print(studentName)
    else:
        print(f"No such student. ")



def read_dict(filename, key_column_index):
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list


    return dictionary




if __name__ == "__main__":
    main()
