def main():
    # Create and print a list named fruit.
    fruit_list = ["pear","banana","apple","mango"]
    fruit_list.reverse()
    fruit_list.append("orange")
    fruit_list.insert(1,"cherry")
    fruit_list.remove("banana")
    # popped_item = fruit_list.pop()
    # print(f"last item {popped_item}")
    fruit_list.sort()
    fruit_list.clear()
    print(f"original: {fruit_list}")



if __name__ == "__main__":
    main()