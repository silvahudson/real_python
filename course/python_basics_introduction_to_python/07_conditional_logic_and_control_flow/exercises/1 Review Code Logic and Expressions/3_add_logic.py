"""
Figure out what the result will be ( True or False ) when evaluating
the following expressions, then type them into the interactive window
to check your answers:
(1 <= 1) and (1 != 1)
not (1 != 2)
("good" !=
"bad") or False
("good" !=
"Good") and not (1 == 1)
"""

x = (1 <= 1) and (1 != 1) #False
y = not(1 != 2) #False
z = ("good" != "bad") or False #True 
k = ("good" != "Good") and not( 1 == 1) #False 

print(x, y, z, k) 

