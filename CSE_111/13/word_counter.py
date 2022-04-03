# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
import sys
import os 
os.system('clear')

#GLOBAL VARIABLES
userFile = input("please type in the name of the file: ") + ".txt"
print(userFile)
user_word = input("what word do you want to search? ").lower()
gindex_list = []


def main(user_file_name):#the main function that holds the stuff i want the file to do.

    file_contents = read_ext_file(user_file_name)#this is a string
    file_contents2 = all_text_to_lower(file_contents)
    finished_file = clean_file(file_contents2)
    # print(finished_file, type(finished_file))
    word_output = get_word_occurances(user_word, finished_file)#this is an integer
    
    print(f" '{user_word}' has {word_output[0]} occurances at position(s) {word_output[1]}")
    return

def clean_file(file_variable):#*done
    bad_characters = [1,2,3,4,5,6,7,8,9,0,'.',',','"','{','}','?','(',')','//\\//\\','*',';','1','2','3','4','5','6','7','8','9','0']    #list of characters i don't want in my file
    # for i in bad_characters:
    cleaned_file = ''.join((filter(lambda i: i not in bad_characters, file_variable)))#clean stuff
    return cleaned_file

def all_text_to_lower(clean_file):#* this function will convert all text in the file to lowercase

    a =   clean_file.lower()#takes file and converts to lowercase
    return a

def read_ext_file(filename): #*read the text of an external file. 

    try:#surround it with error checking

        ext_file = open(filename, "r") #assign file to a variable
        file_contents = ext_file.read() #read content of file to string
        return file_contents
        
    except FileNotFoundError as fileIssue:#if the item is incorrect, this will run
        print(f"incorrect filename. please type in a filename that exists. {fileIssue}")
        sys.exit(1)#this is to exit once it runs and stops it from running again
    
def get_word_occurances(user_word, file_contents):#*get number of occurrences of the substring in the string
    file_contents_list = list(file_contents.split(" "))
    word_occurrences = file_contents_list.count(user_word)
    for i in range(len(file_contents_list)):
        if file_contents_list[i] == user_word:
            gindex_list.append(i)
    return word_occurrences, gindex_list

if __name__ == "__main__":

    main(userFile)
