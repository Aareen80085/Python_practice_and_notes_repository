user_input = int(input("Enter a value to find index: "))
my_tuples = (1, 2, 3, 4, 5)
if user_input in my_tuples:
    for x in my_tuples:
        if x == user_input:
            index = my_tuples.index(x)
            print(f"Index of {x} is: {index}")
            break
else:
    print("Value not found in the tuple.")