import os
os.system("clear")

# input("what is your name? ")
names = ["nick","brooke","ric","carolyn","don","susan","dallin","amanda","amy",]
ages = [10, 2, 78, 69, 21, 36, 44, 19, 100, 88]

#! 1ST LOOP =====================
print("NAMES ARRAY PART")
for name in names:
    # print(f"{name}")
    for letter_of_name in name:
        # print(letter_of_name, end=", ")
        if letter_of_name == "n":
            print(letter_of_name)
        elif letter_of_name == "i":
            print(letter_of_name)
        else:
            print(f"--> {letter_of_name}")

#! 2ND LOOP ====================
    # if name == "brooke":
    #     print(f"{name} your hot!")
    # else:
    #     print(f"ew {name} you are not her")
    # for single_letter in name:
    #     print(f"{single_letter}")
    #     if single_letter == "o":
    #         print("this is correct ")
    #     else:
    #         print("this is not correct ")
print()

#AGES ARRAY
print("AGES ARRAY PART")
for under_30 in ages:
    if under_30 < 30:
        print(f"{under_30:4} = young ")
    else:
        print(f"{under_30:4} = old")
print()