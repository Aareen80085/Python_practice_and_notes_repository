import string

text = input("Enter a string: ")
char = input("Enter a character to count: ")

count = 0

for x in text:
    if x == char:   
        count += 1

print(f"Occurrences of '{char}':", count)