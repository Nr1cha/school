#Example List
fruit = ['apples', 'bannas', 'grapes', 'soda', 'chips', 'water', 'soda', 'chips', 'apples', 'soda']
stuff = ["item0","item1","item2"]
numbers = [1,3,45,3,2,67,8,5,34,89,76]
chosen_word = "chips"
user_word = "item1"
fruit_position = fruit.index(chosen_word)
i_before = fruit[fruit_position - 1]
i_after = fruit[fruit_position + 1]



#Use Known Entites In The List To Find The Index Of An Unknown Object
Index_Number_For_Bannas = fruit.index('apples')

for i in range(len(fruit)):
    if fruit[i] == chosen_word:
        # print(type(i_before))
        print(f"the word before: {i_before}, chosen word {fruit[i]}, at possition:{i}, the word after: {i_after}")


#get items before and after the selected word. context
word = stuff.index(user_word)
#assign the index before and after to a variable
a = stuff[word - 1]
b = stuff[word + 1]

# print(type(a))
print(a, user_word, b)



ext_file = open("words13.txt", "r")
print(ext_file)
print(type(ext_file))