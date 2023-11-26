choice = 0
itemList = []
item = None
confirm = False

def options():
    print("Options:")
    print("\t1. Add item to the shopping list")
    print("\t2. View shopping list")
    print("\t3. Remove item from the shopping list")
    print("\t4. Quit")

    choice = int(input("\nEnter the number of your choice: "))
    switchCase(choice)

def switchCase(choice):
    if choice == 1:
        item = input("Enter the item you want to add: ").lower()
        AddItem(item)      
    elif choice == 2:
        ViewList()
    elif choice == 3:
        item = input("Enter the item you want to remove: ").lower()
        RemoveItem(item)
    elif choice == 4:
        confirm = input("Do you really want to quit? (y/n): ").lower()
        ExitConfirm(confirm)
    else:
        print(f"Invalid Input: {choice} is not one of the choices. Please choose from 1-4 only.")

def AddItem(item):
    itemList.append(item)
    print(f"{item} has been added to your shopping list")

def ViewList():
    if len(itemList) == 0:
        print("Your shopping list is empty")
    else:
        print(f"Your shopping list:\n{itemList}")

def RemoveItem(item):
    itemList.remove(item)
    print(f"{item} has been removed from your shopping list")

def ExitConfirm(confirm):
    if confirm == "y":
        confirm = True
    elif confirm == "n":
        confirm = False
    else:
        print("Invalid Input: Only type 'y' or 'n'")
        
options()

