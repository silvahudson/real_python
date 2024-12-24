number = int(input("Enter a positive integer: "))
for i in range(1, number//2 + 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")
print(f"{number} is a factor of {number}")
    

