# Week 13
###Program "word_counter.py"
Build a program that takes user input of a word, searches a file, then tells the user how many instances of that word there are and at what positions in the file. <br>
This is similar to when a user searches a word on a web-page but in an external file.
####List of Functions in my program
~~~python
main()
clean_file()
all_text_to_lower()
read_ext_file()
get_word_occurances()
~~~

####List of Test Functions in my program
~~~python
test_read_ext_file()
test_get_word_occurances()
test_clean_file()
test_all_text_to_lower()
~~~



####Documentation and sources I used when building this program
For the following...
    
[converting external file to list and seperating words by spaces](https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/)

[documentation for getting rid of symbols](https://www.geeksforgeeks.org/python-string-strip-2/)

[stoping at the error when it's raised ](https://stackoverflow.com/questions/438894/how-do-i-stop-a-program-when-an-exception-is-raised-in-python)

[list basics](https://www.youtube.com/watch?v=8a9wwsUT-o4)

For referencing
lower(),
list(),
count(),
append(),
I used [this link](https://www.programiz.com) and [this link](https://www.delftstack.com/howto/python/python-lowercase-list/)




<!-- 
For me to print the items in a list, i need to convert the file to a variable.
then i converted the file to a string

~~~python
ext_file = open(filename, "r")
file_contents = ext_file.read()
~~~ -->

<!-- print x positions before and after chosen index
https://stackoverflow.com/questions/52600341/how-do-i-find-index-before-and-after-a-value
~~~python
stuff = ["item0","item1","item2"]
user_word = "item1"
word = stuff.index(user_word)
a = stuff[word - 1]
b = stuff[word + 1]

print(a, user_word, b)
~~~ -->

<!-- 
For the section of the for loop, i take the list and insert it in a for loop and i replace the string with the user input variable.

 ~~~ python
 for i in range(len(fruit)):
    if fruit[i] == 'soda':
        print(i,fruit[i])
~~~ -->

