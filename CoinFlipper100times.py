import random
l = []
for i in range(100):
    a = random.randint(0,1)
    l.append(a)
print('tale =',l.count(0))    
print('head =',l.count(1))
print(l)
