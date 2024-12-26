"""
1. Create a tuple literal named location that holds the floating point
numbers 6.51 , 3.39 , and the strings "Lagos" and "Nigeria"
, in that
order.
2. Use index notation and display the string at index 2 in location .
3. In a single line of code, unpack the values in location into four variables
named latitude , longitude , city , and country . Then print each
value on a separate line.
"""
location = (6.51, 3.39, "Lagos", "Nigeria")
print(location[2])
latitude, longitude, city, country = location

print(latitude)
print(longitude)
print(city)
print(country)
