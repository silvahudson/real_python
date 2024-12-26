s = "eggs, fruit, orange juice"
breakfast = s.split(', ')
print(breakfast)
print(len(breakfast))
lengths = [len(i) for i in breakfast]
print(lengths)
