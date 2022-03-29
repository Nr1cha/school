# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

user_text = input("please type in the name of the file. ")
def main(user_file_name):

    read_ext_file()
    user_input()


    def read_ext_file(filename):

    #get file object reference to the file
        ext_file = open(filename, "r")

    #read content of file to string
        file_contents = ext_file.read().lower()

        return file_contents


    #get number of occurrences of the substring in the string
    def user_input(user_word, file_contents):

        try:
            word_occurrences = file_contents.count(user_word)
        except PermissionError as Perm_error:
            print(f"please type the in a word correctly{Perm_error}")
        return word_occurrences

    print('Number of occurrences of the word :', word_occurrences)

if __name__ == "__main__":

    main(user_text)
