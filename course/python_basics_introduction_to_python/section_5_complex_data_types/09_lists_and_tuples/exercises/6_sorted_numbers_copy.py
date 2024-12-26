"""
1. Create the list [4, 3, 2, 1] and assign it to the variable numbers .
2. Create a copy of the numbers list using the [:] slice notation.
3. Sort the copy of the numbers list in numerical order using .sort() .
4. Display both numbers and its copy to proof that they look dierently
"""
numbers = [4, 3, 2, 1]
numbers_copy = numbers[:]
numbers_copy.sort()
print(f"numbers: {numbers} \n copy: {numbers_copy}")
