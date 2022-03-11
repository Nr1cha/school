import csv
from datetime import datetime
current_date_and_time=datetime.now()
 
def main():
    try:
        products_dict={}
        product_number_index=0
        
        total_items = 0
        subtotal = 0.0
        total = 0.0    
        
        products_dict=read_dict("products.csv", product_number_index)
    #   print("All Products")
    #   print(products_dict)
 
        print()
        print("Inkom Emporium")
        print()
        
        with open ("request.csv","rt") as csv_file:
            reader=csv.reader(csv_file)
            next(reader)
            
            for row in reader:
                product_number_index = row[0]
                quantity = row[1]
                total_items += int(quantity)
                price= products_dict[product_number_index]
                
                print(f'{price[1]}:  {quantity} @ {price[2]}')
                subtotal+=float(price[2]) * int(quantity)
 
    #Print information
        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {subtotal * 0.06:.2f}")
        print(f"Total: {subtotal * 1.06:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
        print()
 
    except KeyError as key_Error:
        print()
        print(f'Error: Unknown product ID in the file {key_Error}')
    
    
    except FileNotFoundError as noFile_error:
        print()
        print(f"Error: missing file")
        print(f'No such file or directory: {noFile_error}')
 
 
def read_dict(filename, key_column_index):
    products_dict={}
    with open (filename,"rt") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
 
        for row_list in reader:
            product_num_index = row_list[0]
            name = row_list[1]
            price = row_list[2]
            products_dict[product_num_index]=[product_num_index,name,price]
    return products_dict
 
if __name__ == "__main__":
    main()