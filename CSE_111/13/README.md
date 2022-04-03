## Week 13

List of Functions in my program
~~~python
main()
clean_file()
all_text_to_lower()
read_ext_file()
get_word_occurances()
~~~


taking a file and allowing the user to input a word and then showing how many times that word shows up 
in a file and where. 
stretch feature
    showing words before and after the selected word. 
    showing where a phrase shows up in the file. (if user types in more than one word, then showing where that is in the file)
    
converting external file to list and seperating words by spaces. 
https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/

documentation for getting rid of symbols.
https://www.geeksforgeeks.org/python-string-strip-2/

stoping at the error when it's raised 
https://stackoverflow.com/questions/438894/how-do-i-stop-a-program-when-an-exception-is-raised-in-python

list basics
https://www.youtube.com/watch?v=8a9wwsUT-o4 <br>

For me to print the items in a list, i need to convert the file to a list.

~~~python
ext_file = open(filename, "r")
~~~

print x positions before and after chosen index
https://stackoverflow.com/questions/52600341/how-do-i-find-index-before-and-after-a-value
~~~python
stuff = ["item0","item1","item2"]
user_word = "item1"
word = stuff.index(user_word)
a = stuff[word - 1]
b = stuff[word + 1]

print(a, user_word, b)
~~~


For the section of the for loop, i take the list and insert it in a for loop and i replace the string with the user input variable.

 ~~~ python
 for i in range(len(fruit)):
    if fruit[i] == 'soda':
        print(i,fruit[i])
~~~

