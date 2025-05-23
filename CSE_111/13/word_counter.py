# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
'''
total hours spent on project 14

step 1 run word_counter.py with "words.txt" in the same directory
step 2 type in words 
step 3 type in the word that you want to search


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
'''
import sys
import os 
os.system('clear')#this just clears the screen when the file is started.

#GLOBAL VARIABLES
gindex_list = []

def main():#the main function that holds the stuff i want the file to do.

    user_file_name = input("please type in the name of the file: ") + ".txt"
    user_word = input("what word do you want to search? ").lower()
    file_contents = read_ext_file(user_file_name)
    file_contents2 = all_text_to_lower(file_contents)
    finished_file = clean_file(file_contents2)
    word_output = get_word_occurances(user_word, finished_file)
    
    print(f" '{user_word}' has {word_output[0]} occurances at position(s) {word_output[1]}")
    return

def clean_file(file_variable):#function for cleaning fluf out of the list
    bad_characters = [1,2,3,4,5,6,7,8,9,0,'.',',','"','{','}','?','(',')','//\\//\\','*',';','1','2','3','4','5','6','7','8','9','0']#list of characters i don't want in my file
    cleaned_file = ''.join((filter(lambda i: i not in bad_characters, file_variable)))#clean stuff
    return cleaned_file

def all_text_to_lower(clean_file):#this function will convert all text in the file to lowercase

    a =   clean_file.lower()#takes file and converts to lowercase
    return a

def read_ext_file(filename): #read the text of an external file. 

    try:#surround it with error checking

        ext_file = open(filename, "r") #assign file to a variable
        file_contents = ext_file.read() #read content of file to string
        return file_contents
        
    except FileNotFoundError as fileIssue:#if the item is incorrect, this will run
        print(f"incorrect filename. please type in a filename that exists. {fileIssue}")
        sys.exit(1)#this is to exit once it runs and stops it from running again
    
def get_word_occurances(user_word, file_contents):#get number of occurrences of the substring in the string
    file_contents_list = list(file_contents.split(" "))
    word_occurrences = file_contents_list.count(user_word)
    for i in range(len(file_contents_list)):
        if file_contents_list[i] == user_word:
            gindex_list.append(i)
    return word_occurrences, gindex_list

if __name__ == "__main__":

    main()
