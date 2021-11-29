shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = None

for item in shopping_cart:
    product_name = item[0]
    price = item[1]
    
    if price > max_price:
        max_price = price
        max_product = product_name
print(f"The product with the highest price is: {product_name} ${max_price}")