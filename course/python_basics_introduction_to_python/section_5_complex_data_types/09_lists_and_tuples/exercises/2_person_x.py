"""
1. Use tuple() and a string literal to create a tuple called my_name that
contains the letters of your name.
2. Check whether the character "x" is in my_name using the in keyword.
3. Create a new tuple containing all but the first letter in my_name using slice
notation.
"""
my_name = tuple("Hudson")

print("x" in my_name)

new_tuple = my_name[1:]
print(new_tuple)