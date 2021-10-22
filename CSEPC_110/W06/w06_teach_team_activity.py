# no one under 36 inches may ever ride,
# either by themselves or with another rider.

# Normally, two riders sit in the car together.
# A single rider can only ride if they are at least 18 years old
# and
# at least 62 inches tall.

# If
# there are two riders
# and
# one of them is at least 18 years old,
# they may ride together.


# Prompt the user for the age and height of the first person.
# Then,
# ask whether there is a second rider, and
# if so, ask for their age and height.
# Handle the case of a single rider.
# Finish implementing the basic rules.
can_ride = False
print("the following questions will ask if your able to ride. ")

rider_age = int(input("what is the age of the first rider? "))
rider_height = int(input("what is the height of the first rider? "))
# GOLDEN PASSPORT
if rider_age >= 12 and rider_age < 18:
    golden1 = input("Does this rider have a golden passport (yes/no)? ")
# SECOND RIDER
is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    rider2_age = int(input("what is your age? "))
    rider2_height = int(input("what is your height? "))

    # STUFF
    if rider2_age >= 12 and rider2_age < 18:
        golden2 = input("Does this rider have a golden passport (yes/no)? ")
# STUFF

    # rule 1
    if rider_height < 36 or rider2_height < 36:
        can_ride = False
    else:
        # rule 3
        if rider_age >= 18 or rider2_age >= 18 or golden1.lower() == "yes" or golden2.lower() == "yes":
            can_ride = True
        else:
            # Neither is an adult

            # Rule 4
            if rider_age >= 12 and rider_height >= 52 and rider2_age >= 12 and rider2_height >= 52:
                can_ride = True
            elif (rider_age >= 16 and rider2_age >= 14) or (rider2_age >= 14 and rider2_age >= 16):
                # Rule 6
                can_ride = True
            else:
                can_ride = False


else:  # there is only one rider
    # rule 2
    if rider_age >= 18 and rider_height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
