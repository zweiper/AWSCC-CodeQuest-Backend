choice = 0
itemList = []
item = None

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
        print("")
    else:
        print("")

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

options()

