friends = []
name = None
names_of_friends = "Type the name of a friend: "
#LOOP STUFF
while name != "end":
    name = input(names_of_friends)
    if name != "end":
        friends.append(name)
print()
print("your friends are: ")
for friend in friends:
    print(friend)