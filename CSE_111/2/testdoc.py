city = "salt lake"
with open("CSE_111/2/volumes.txt", mode="at") as volumes:

    print(f"{city}", file=volumes)
    # print(city, file=volumes)
print("end of program")