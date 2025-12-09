my_tuples = (1, 2, 3, 4, 5)
my_list = [6, 7, 8]
# my_tuples[0] = 10  # This will raise an error because tuples are immutable

#prints a single tuple value
# print(my_tuples[0])
# #print using negative indexing
# print(my_tuples[-1])

# #slicing 
# print(my_tuples[1:4])
# print(my_tuples[0:3])
# print(my_tuples[:3])

# #loop through the tuple using for loop
# for x in my_tuples:
#     print(x)

# #loop through the tuple using while loop
# x = 0

# while x < len(my_tuples):
#     print(my_tuples[x])
#     x = x + 1

#updating lists inside a tuple
# my_list = list(my_tuples)
# my_list[1] = 3
# my_con_tuples = list(my_tuples)
# print(type(my_con_tuples)) # 1,2,3,4,5
# my_con_tuples[0] = 34
# print(my_con_tuples) # 34,2,3,4,5


my_set = {9, 10, 11, True, 6, 7 , 9 }
for x in my_set:
     print(x)   
    
my_set.add(12)
my_set.remove(10)
