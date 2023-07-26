contact = {}

def printContact():
    for name in contact:
        print(f"{name} - {contact[name]}" )



while True:
    choice = int(input("1)Add contact.\n2)See list of contacts.\n3)Edit contact.\n4)Delete a contact.\n5)Exit.\nMake your choice: "))
#CASE 1
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        contact[name] = phone
#CASE 2
    elif choice == 2:
        if len(contact) < 1:
            print("List is empty")
        else:
            printContact()
#CASE 3
    elif choice == 3:
        find = input("Enter the name of contact to be edited: ")
        if find == name:
            contact[name] = input("Change the number to: ")
        else:
            print("Name isn't found in the list.")
#CASE 4
    elif choice == 4:
        find = input("Enter the name contact to delete: ")
        if find == name:
            del contact[name]
            name = ""
            phone = 0
        else:
            print("Contact isn't found in the list.")
    elif choice == 5:
        break


    