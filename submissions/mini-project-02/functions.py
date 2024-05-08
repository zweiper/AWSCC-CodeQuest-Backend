def Options():
    print("Options:")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search")
    print("4. Delete Account")
    print("5. Update Account")
    print("6. Exit")
    choice = int(input("\nChoice: "))
    switchCase(choice)

def switchCase(choice):
    if choice == 1:
        AddAccount()

def AddAccount():
    name = input("Enter name of website:")
    email = input("Enter email:")
    pw = input("Enter password:")