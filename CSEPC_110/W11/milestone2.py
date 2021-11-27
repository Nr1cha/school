# list_expectency = []
# with open("life-expectancy.csv") as life_expetancy:
#     for line in life_expetancy:
#         if line.startswith("Entity"): continue;  #this will skip the first line
#         #line format
#         clean_line = line.split(",")
#         striped_line = line.strip()

#         #variables
#         entity = striped_line[0]
#         code = striped_line[1]
#         year = int(clean_line[2])
#         expectency = float(clean_line[3])
#         # sorted = year.sort(reverse=True)
#         # print(expectency)
#         list_expectency.append(expectency)
#     list_expectency.sort(reverse = False)

#     print(list_expectency)



user_choice = None
max_life_expectancy = None
max_life_expectancy_year = None
max_life_expectancy_entity = None
min_life_expectancy = None
min_life_expectancy_year = None
min_life_expectancy_entity = None
country = None

with open("life-expectancy.csv") as life_expectency_file:

    # user_choice = int(input(f"Enter the year of interest: "))
    # # print(f"The overall max life expectancy is:")
    # print(f"The overall min life expectancy is:")
    # print(f"For the year {}:")
    # print(f"The average life expectancy across all countries was {}")


    for line in life_expectency_file:
        if line.startswith("Entity"): continue;
        clean_line = line.split(",")
        # striped_line = line.strip()
        entity = clean_line[0]
        code = clean_line[1]
        year = clean_line[2]
        expectency = clean_line[3]


        if min_life_expectancy == None or expectency < min_life_expectancy:
            min_life_expectancy = expectency
            min_life_expectancy_year = year
            min_country = entity
        

        if max_life_expectancy == None or expectency > max_life_expectancy:
            max_life_expectancy = expectency 
            max_life_expectancy_year = year
            max_country = entity

    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_life_expectancy_year}")
    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_life_expectancy_year}")