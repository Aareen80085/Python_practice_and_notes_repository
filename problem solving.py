# # A 3 digit integer number (randomly genrated) the user has to guess the number.
# # After each guess, the program provides feedback on how many digits are correct and in the correct position,
# # and how many digits are correct but in the wrong position. The game continues until 10 attempts.
# import random

# three_digit_number = random.randrange(100, 999) # Example number, in a real game this would be randomly generated
# attempts = 10

# while attempts > 0 and attempts <= 10:
#     guess = input("Enter your 3-digit guess: ")

#     if len(guess) != 3 is not str(guess).isdigit():
#         attempts = attempts - 1
#         print(f"Enter a valid 3-digit number. you entered {len(guess)} digits.")

#         if str(guess) == three_digit_number:
#             print("Congratulations! You've guessed the number correctly.")
#             break

#     else:
#          print(f"Incorrect guess. Try again you have {attempts} attempts left.")
#          for x in list(guess):
#              if x in str(three_digit_number):
#                  if str(three_digit_number).index(x) == guess.index(x):
#                      print(f"Digit {x} is in the correct position.")
#                  if str(three_digit_number).index(x) != guess.index(x):
#                         print(f"Digit {x} is in the wrong position.")

# def is_leap(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

# year = int(input())
# print(is_leap(year))

# if __name__ == '__main__':

#     n = int(input())
#     for i in range(1, n + 1):
#         print(i, end="")

if __name__ == '__main__':
    n = int(input())
    arr = int(input().split())
    runner_up = sorted(set(arr))[-2]
    print(runner_up)