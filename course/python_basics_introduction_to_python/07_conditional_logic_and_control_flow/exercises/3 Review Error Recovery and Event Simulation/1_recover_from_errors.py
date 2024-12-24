"""
Write a program that repeatedly asks the user to input an integer. If the
user enters something other than an integer, then the program should
catch the ValueError and display the message "Try again."
Once the user enters an integer, the program should display the
number back to the user and end without crashing.
"""
while True:
    try:
        num = int(input("Write an integer: "))
        print(num)
        break
    except ValueError:
        print("Try again")
         