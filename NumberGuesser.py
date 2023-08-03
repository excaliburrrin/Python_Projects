import random
a = random.randint(0,100)
for i in range(7):
    b = int(input())
    if a < b:
        print("Enter smaller number")
    elif a > b:
        print("Enter bigger number")
    else:
        print("You won")
print("Your limits over")
