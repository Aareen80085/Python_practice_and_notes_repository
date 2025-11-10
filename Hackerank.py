#Question 1
my_string = "Hello, World!"
print(my_string)
    
#Question 2
import math
import os
import random
import re
import sys


if __name__ == '__main__':
   n = int(input().strip())
   
   if (n%2 != 0):
      print("Weird")
   
   elif (n%2 == 0) and n>=2 and n<=5:
         print("Not Weird")
    
   elif (n % 2 == 0) and n>=6 and n<=20:
         print("Weird")
    
   elif (n%2 == 0) and n>20:
        print("Not Weird") 

   else:
        print("bye")
# Question 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

#Question 4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(int(a//b))
    print(float(a/b))

#Question 5
import math

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
     print(round(math.pow(i, 2)))

#Question 6

def is_leap(year):
    leap = False
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else: 
        return False

year = int(input())
print(is_leap(year))

#Question 7

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1): 
     print(i, end="")

#Question 8

if __name__ == '__main__':
    n = int(input())
    arr = list(map(input().split()))
    runner_up = max(-1)
    print(runner_up)
