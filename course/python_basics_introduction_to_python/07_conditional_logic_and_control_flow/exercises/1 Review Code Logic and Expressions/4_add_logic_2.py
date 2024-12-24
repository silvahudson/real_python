"""
Add parentheses where necessary so that each of the following
expressions evaluates to True :
False == not True
True and False == True and False
not True and "A" == "B"
"""

a = False == (not True) 
b = (True and False) == (True and False) 
c = not(True and "A" == "B")

print(a, b, c)
