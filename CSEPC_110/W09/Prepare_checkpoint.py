friends = []
name = None
names_of_friends = "Type the name of a friend: "
#LOOP STUFF
while name != 0 and name != "0":
    name = input(names_of_friends)
    if name != 0 and name != "0":
        friends.append(name)
print()
print("your friends are: ")
for friend in friends:
    print(friend)