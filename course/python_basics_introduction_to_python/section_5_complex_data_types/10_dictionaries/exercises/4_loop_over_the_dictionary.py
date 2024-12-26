"""
Write a for loop to display the ship and captain names contained in
the dictionary.
For example: "The Enterprise is captained by Picard."
"""
captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

print(captains)

if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
    
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")
    
