# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
import sys
import os 
os.system('clear')

#GLOBAL VARIABLES
userFile = input("please type in the name of the file. ")
user_word = input("what word do you want to search? ").lower().capitalize()
#todo add a global list of the contents of the file


def main(user_file_name):#the main function that holds the stuff i want the file to do.

    file_contents = read_ext_file(user_file_name)#this is a string
    word_output = user_input(user_word, file_contents)#this is an integer
    clean_file(file_contents)
    print(f" '{user_word}' has {word_output} occurances in your file.")

def clean_file(file_variable):
    bad_characters = [1,2,3,4,5,6,7,8,9,0,'.',',','"',"'",'',]#list of characters i don't want in my file
    for i in bad_characters:
        clean_line = file_variable.replace(i, '')#replacing them here

def all_text_to_lower(clean_file):#this function will convert all text in the file to lowercase
    print()
    return clean_file

def read_ext_file(filename): #read the text of an external file. 

    try:#surround it with error checking
        #assign file to a variable
        ext_file = open(filename, "r")
        #read content of file to string
        file_contents = ext_file.read()
        return file_contents
        
    except FileNotFoundError as fileIssue:#if the item is incorrect, this will run
        print(f"incorrect filename. please type in a filename that exists. {fileIssue}")
        sys.exit(1)#this is to exit once it runs and stops it from running again
    
def user_input(user_word, file_contents):#get number of occurrences of the substring in the string

    word_occurrences = file_contents.count(user_word)

    return word_occurrences

if __name__ == "__main__":

    main(userFile)
