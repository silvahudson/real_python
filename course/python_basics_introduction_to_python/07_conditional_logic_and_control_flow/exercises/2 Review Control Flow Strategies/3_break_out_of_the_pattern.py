"""
Using continue , write a program that loops over the numbers 1 to
50 and prints all numbers that are not multiples of 3 .
"""
for i in range(1, 51):
    if i % 3 != 0:
        print(i)
    else:
        continue 
    

    