import string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in string.ascii_letters:   
        consonant_count += 1
    elif char in string.digits:          
        digit_count += 1
    elif char in string.whitespace:      
        space_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Spaces:", space_count)