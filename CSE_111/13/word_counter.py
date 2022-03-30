# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
import sys

user_text = input("please type in the name of the file. ")
word_from_user = input("what word do you want to search? ").lower()
def main(user_file_name):

    file_contents = read_ext_file(user_file_name)
    word_output = user_input(word_from_user, file_contents)
    print(f" '{word_from_user}' has {word_output} occurances in your file.")


def read_ext_file(filename):

#get file object reference to the file
    try:
        ext_file = open(filename, "r")
#read content of file to string
        file_contents = ext_file.read().lower()
        return file_contents
        
    except FileNotFoundError as fileIssue:
        print(f"incorrect filename. please type in a filename that exists. {fileIssue}")
        sys.exit(1)
        # return fileIssue


    #get number of occurrences of the substring in the string
def user_input(user_word, file_contents):

    word_occurrences = file_contents.count(user_word)

    return word_occurrences

    # print('Number of occurrences of the word :', word_occurrences)

if __name__ == "__main__":

    main(user_text)
