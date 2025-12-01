# x = int(10)

# def sum(x):
#     print(x+1)

# y = int(10)

# sum(x) 
# sum(y)   

x = 10

def sum_with_void(x):
    sayHello()
    print(x+1)

def sayHello():
    print("Hello")

def sum_with_return(x):
    return x+1

y = 10

sum_with_void(x)
print(sum_with_return(y))
