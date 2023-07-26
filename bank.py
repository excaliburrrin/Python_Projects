name = input("Your Username: ")
pin = input("Your password: ")
balance = 1000
attempts = 3
while True:
    menu = input("""
    1)Add money
    2)Withdraw Money
    3)See balance
    4)Quit
    """)    
    

    if menu == "1":
        add = int(input("Amount of money to add:"))            
        if add > 1000:
                pinask = input("Submit your password: ")
                while pinask != pin:
                    pinask = input("Submit your password again: ")
                    if pinask != pin:
                        attempts = attempts - 1
                        print("Password is incorrect! \n Attempts left: ", attempts)
                    if attempts == 0:
                        break
                    if pinask == pin:
                        balance = balance + add
        else:
            balance = balance + add
                    
    elif menu == "2":
        withdraw = int(input("Amount of money to withdraw:"))
        if withdraw > 1000:
                pinask = input("Submit your password: ")
                while pinask != pin:
                    pinask = input("Submit your password again: ")
                    if pinask != pin:
                        attempts = attempts - 1
                        print("Password is incorrect! \n Attempts left: ", attempts)
                    if attempts == 0:
                        break
                    if pinask == pin:
                        balance = balance - withdraw
        else:
            balance = balance - withdraw
        
    elif menu == "3":
        print("Your balance:" + str(balance))
    else :
        menu == "4"
        break