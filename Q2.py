import string

text = input("Enter a string: ")
cleaned = ""
for char in text:
    if char in string.ascii_letters or char in string.digits:
        cleaned += char.lower()

if cleaned == cleaned[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")