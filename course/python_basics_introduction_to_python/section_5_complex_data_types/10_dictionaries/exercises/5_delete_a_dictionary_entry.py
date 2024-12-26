"""
Delete "Discovery" from the dictionary.
"""
captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

print(captains)
del captains["Discovery"]
print(captains)
  