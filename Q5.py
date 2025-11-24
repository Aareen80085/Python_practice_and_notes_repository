import string

sentence = input("Enter a sentence: ")

current_word = ""

for x in sentence:
    if x in string.whitespace:   
        if current_word != "":
            print(current_word)
            current_word = ""
    else:
        current_word += x

if current_word != "":
    print(current_word)