h = int(input('Enter your height: '))
w = int(input('Enter your weight: '))
f = w/h**2 * 10000
if f < 18.5:
    print("You are underweight!")
elif 18.4 < f < 25:
    print("You are normal!")
elif 24.9 < f < 40:
    print("You are overweight!")
else:
    print("Obese!!!")
print(f)
