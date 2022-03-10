import csv
from datetime import datetime
current_date_and_time = datetime.now()


def main():

  product_list = {} #dictionary 

  first_index = 0
  second_index = 1
  third_index = 2

  total_items = 0
  subtotal = 0.0
  # total = 0.0

  # PRODUCTS FILE
  products_dict = read_dict("products.csv", first_index)
  for product_key in products_dict:
    row_list = products_dict[product_key]
    product_number = row_list[first_index]
    product_name = row_list[second_index]
    product_price = row_list[third_index]
    update_dictionary = {product_number : (product_name, product_price)}
    product_list.update(update_dictionary)

  # REQUEST FILE 
  request_dict = read_dict("request.csv", first_index)
  for request_key in request_dict:
    row_list = request_dict[request_key]
    product_num = row_list[first_index]
    product_quantity = row_list[second_index]
    list_split = product_list[product_num]
    total_items += int(product_quantity)
    subtotal += float(list_split[second_index]) * float(product_quantity)
    print(f"{list_split[first_index]}: {product_quantity} @ {list_split[second_index]}")


  print(f"Number of Items: {total_items}")
  print(f"Subtotal: {subtotal}")
  print(f"Sales Tax: {round(subtotal * 0.06, 2)}")
  print(f"Total: {round(subtotal * 1.06, 2)}")
  print()
  print(f"{current_date_and_time:%a %b  %d %I:%M:%S %Y}")
  print("Thank you for shopping at the Inkom Emporium.")

def read_dict(filename, key_column_index):
   
    dictionary_list={}
    with open (filename, "rt")as cvs_file:
        reader = csv.reader(cvs_file)
        next(reader)
        for row_list in reader:
            key=row_list[key_column_index]
            dictionary_list[key] = row_list
       
    return dictionary_list

    
if __name__ == "__main__":
    main()