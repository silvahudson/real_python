"""
Write a program that prompts the user to enter a word using the
input() function and compares the length of the word to the number
five. The program should display one of the following outputs,
depending on the length of the user’s input:
"Your input is less than 5 characters long"
"Your input is greater than 5 characters long"
"Your input is 5 characters long
"""

word = input("Enter your input: ")

if len(word) == 5:
    print("Your input is 5 characters long")
elif len(word) > 5:
    print("Your input is greater than 5 characters long")
else:
    print("Your input is less than 5 characters long")
    