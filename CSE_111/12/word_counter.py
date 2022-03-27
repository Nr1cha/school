# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/




#get file object reference to the file
file = open("/Users/nick/Documents/GitHub/school/CSE_111/11/words2.txt", "r")

#read content of file to string
data = file.read().lower()

#get number of occurrences of the substring in the string
occurrences = data.count("what")

print('Number of occurrences of the word :', occurrences)