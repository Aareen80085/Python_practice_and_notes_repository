import string

text = input("Enter a sentence: ")

result = ""

for char in text:
    if char in string.whitespace:   
        result += "-"
    else:
        result += char

print(result)