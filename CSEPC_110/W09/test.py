friends = []
new_friend = ""
# new_friend = input("name a friend: ")
# friends.append(new_friend)


while new_friend != "quit":
    new_friend = input("name a friend: ")
    friends.append(new_friend)

for friend in friends:
    print(friend)