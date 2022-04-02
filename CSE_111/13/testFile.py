#Example List
fruit = ['apples', 'bannas', 'grapes', 'soda', 'chips', 'water', 'soda', 'chips', 'apples', 'soda']
chosen_word = "soda"
fruit_position = fruit.index(chosen_word)
i_before = fruit[fruit_position - 1]
i_after = fruit[fruit_position + 1]
numbers = [1,3,45,3,2,67,8,5,34,89,76]
#Use Known Entites In The List To Find The Index Of An Unknown Object
Index_Number_For_Bannas = fruit.index('apples')
#Print The Object
# print(fruit[Index_Number_For_Bannas])
# print(fruit)
# print(type(fruit))

for i in range(len(fruit)):

    if fruit[i] == chosen_word:
        print()
        print(type(i_before))
        print(i_before, i, fruit[i], i_after)




stuff = ["item0","item1","item2"]
user_word = "item1"
word = stuff.index(user_word)
a = stuff[word - 1]
b = stuff[word + 1]

print(type(a))
print(a, user_word, b)