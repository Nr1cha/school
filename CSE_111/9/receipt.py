import csv
from datetime import datetime
current_date_and_time = datetime.now()
def main():
    try:
        products = {}
        totalItems = 0
        subtotal = 0.0
        print("Inkom Emporium")
        print()
        with open("products.csv", "rt") as open_file:
            reader = csv.reader(open_file)
            next(reader)
            for row in reader:
                product_number = row[0]
                product_name = row[1]
                product_price = row[2]
                dictionarayUpdate = {product_number : (product_name, product_price)}
                products.update(dictionarayUpdate)
        with open("request.csv", "rt") as open_file:
            reader = csv.reader(open_file)
            next(reader)
            for row in reader:
                product_number = row[0]
                product_quantity = row[1]
                split_line = products[product_number]
                totalItems += int(product_quantity)
                subtotal += float(split_line[1]) * float(product_quantity)
                print(f"{split_line[0]}: {product_quantity} @ {split_line[1]}")
        print()
        print(f"Number of Items: {totalItems}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {subtotal * 0.06:.2f}")
        print(f"Total: {subtotal * 1.06:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium")
        print(f"{current_date_and_time:%a %b  %d %I:%M:%S %Y}")
   
    except (FileNotFoundError, PermissionError) as file_name_error:
        print(file_name_error)
        print("Either you don't have permission to enter the file, or it just isn't real. Get a real file buddy.")
    except KeyError as error:
        print(error)
        print(f"Looks like there is a line in one of your files that has an error in it.")
if __name__ == "__main__":
    main()