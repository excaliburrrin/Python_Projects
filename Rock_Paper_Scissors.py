import random
while True:
    p = int(input('0 - rock\n1 - paper\n2 - scissors\nChoose one of them: '))
    r = random.randint(0,2)
    
    if p == 0:
        print('You chose: rock ')
    elif p == 1:
        print('You chose: paper ')
    else:
        print('You chose: scissors')
    
    if r == 0:
        print('PC chose: rock ')
    elif r == 1:
        print('PC chose: paper ')
    else:
        print('PC chose: scissors')
        
    if p == r:
        print('Result: TIE!')
    elif p == 0 and r == 1:
        print('Result: You LOSE!')
    elif p == 1 and r == 2:
        print('Result: You LOSE!')
    elif p == 2 and r == 0:
        print('Result: You LOSE!')
        
    elif p == 2 and r == 1:
        print('Result: You WON!')
    elif p == 0 and r == 2:
        print('Result: You WON!')
    elif p == 1 and r == 0:
        print('Result: You WON!')
        
    b = input('Wanna try again (y/n): ')
    if b == 'y':
        continue
    else:
        break
                    
