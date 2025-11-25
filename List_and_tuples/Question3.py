my_list = [1,2,2,2,4,4,5]
unique_list  = []
for x in my_list:
    if x in my_list:
        count = my_list.count(x)
        count += 1
        if count >= 1:
            print(f"{x}:", count)
            