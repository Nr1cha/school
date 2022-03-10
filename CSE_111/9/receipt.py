import csv

def main():
    ProductID_index = 0
    ProductName = 1
    ProductPrice = 2
    products_dict = read_dict("products.csv",ProductID_index)
    print(f"{products_dict}")
    
    with open("")




def read_dict(filename, key_column_index):
        """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

        compound_dictionary = {}

        with open(filename, "rt") as dictionary:
            reader = csv.reader(dictionary)
            next(reader)


            for key, value in compound_dictionary.items():
                totalCost = value[ProductPrice]

        return compound_dictionary
