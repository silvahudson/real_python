"""
Write a function called roll() that uses randint() to simulate
rolling a fair die by returning a random integer between 1 and 6 
"""
from random import randint 

def roll() -> int:
    """Return random integer between 1 and 6"""
    return randint(1, 6)

print(roll())