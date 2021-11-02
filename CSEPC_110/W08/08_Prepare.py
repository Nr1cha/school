items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = range(100)

# for item in items:
#     print(f"The item is: {item}")

for i in range(5):
    print(f"outer loop: {i}")
    for j in range(2,5):
        print(f"inner loop{j}")