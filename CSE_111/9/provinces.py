def main():
    provinces_list = read_list("CSE_111/9/provinces.txt")
    print(provinces_list)
    provinces_list.pop(0)
    provinces_list.pop()

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    count = provinces_list.count("Alberta")
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
