list_expectency = []
with open("life-expectancy.csv") as life_expetancy:
    for line in life_expetancy:
        if line.startswith("Entity"): continue;  #this will skip the first line
        clean_line = line.split(",")
        striped_line = line.strip()
        entity = striped_line[0]
        code = striped_line[1]
        year = int(clean_line[2])
        expectency = float(clean_line[3])
        # sorted = year.sort(reverse=True)        
        # print(expectency)
        list_expectency.append(expectency)
    list_expectency.sort(reverse = False)

    print(list_expectency)