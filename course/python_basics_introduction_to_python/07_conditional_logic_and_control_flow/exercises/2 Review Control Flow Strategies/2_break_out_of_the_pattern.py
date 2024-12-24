"""
Using break , write a program that repeatedly asks the user for some
input and quits only if the user enters "q" or "Q
"""

while True:
    user_input = input("Enter your input: ")
    if user_input.lower() == 'q':
        break 
    
    
    