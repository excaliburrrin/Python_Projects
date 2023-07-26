import time


class BankAccount():
    def __init__(self,account_number,password = None):
        self.password = password
        self.balance = 1000
        self.transaction_history = []
        self.account_number = account_number
    
    def deposit(self, amount):

        self.balance += amount
        print(f"Deposited {amount}.")
        self.transaction_history.append(f"Deposit {amount}")
        
    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}.")
            self.transaction_history.append(f"Withdrew {amount}")

        else:
            print(f"Insufficient balance. Cannot withdraw {amount}")
            
    def transfer(self, amount, other_account):

        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transferred {amount} to account {other_account.account_number}.")
            self.transaction_history.append(f"Transfered {amount}")
        else:
            print(f"Insufficient balance. Cannot transfer {amount}.")

    def change_password(self, current_password, new_password):

        if current_password == self.password:
            self.password = new_password
            print("Password changed successfully")
            
        else:
            print("Incorrect password")
        
    

username = input("Enter username: ")
password = input("Enter password: ")

account1 = BankAccount(username,password)

username = input("Enter username: ")
password = input("Enter password: ")

account2 = BankAccount(username,password)

current_account = account1

while True:
    user_choice = int(input("1)Deposit\n2)Withdraw\n3)Transfer\n4)History\n5)Balance\n6)Change password\n7)Switch account\n8)Exit\nChoose operation: "))

    if user_choice == 1:
        amount = int(input("Enter amount: "))
        current_account.deposit(amount)
        time.sleep(3)
    
    elif user_choice == 2:
        amount = int(input("Enter amount: "))
        current_account.withdraw(amount)
        time.sleep(3)
    
    elif user_choice == 3:
        amount = int(input("Enter amount: "))
        if amount <= current_account.balance:

            if current_account == account1:
                account1.transfer(amount,account2)

            else:
                account2.transfer(amount,account1)

        else:
            print("Insufficient balance.")
        time.sleep(3)
    
    elif user_choice == 4:

        for i in current_account.transaction_history:
            print(i)
        
        time.sleep(3)
        
    elif user_choice == 5:
        print(f'Your balance is {current_account.balance}')
        time.sleep(3)
    
    elif user_choice == 6:
        cur = input("Enter current password: ")
        new = input("Enter new password: ")
        current_account.change_password(cur, new)
        time.sleep(3)
    
    elif user_choice == 7:
        if current_account == account1:
            current_account = account2
            print(f"Account was successfully changed to {account2.account_number}")
        else:
            current_account == account1
            print(f"Account was successfully changed to {account1.account_number}")
        time.sleep(3)
        
    elif user_choice == 8:
        break








