text = input("Enter a string: ")

result = ""
word = set()

for x in text:
    if x not in word:
        result += x
        word.add(x)

print("String without duplicates:", result)