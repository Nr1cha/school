people_list = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
ages = []
people = []
youngest_age = None
young_age_name = None

for line in people_list:
    clean_line = line.split(" ")
        #identifying information that is split
    person = clean_line[0]
    person_age = int(clean_line[1])

        #adding to arrays
    people.append(person)
    ages.append(person_age)

#find the youngest person in the list.
    if youngest_age == None or person_age < youngest_age:
        # Set the current age as the youngest
        youngest_age  = person_age
        # Set the current name as the youngest
        young_age_name = person

    # youngest = min(ages)

# print(ages)
print(f"Person list: {people}\nAge list: {ages}")
print()
print(f"the youngest age is {youngest_age} and that belongs to {young_age_name}")
