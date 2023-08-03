n = [2,3,5,7,11]
a = int(input())
b = True
for i in n:
    if a % i == 0:
        print('Not prime')
        b = False
        break
    else:
        continue
if b:
    print('Prime')


