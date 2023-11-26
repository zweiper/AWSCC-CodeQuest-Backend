choice = 0
itemList = []
itemAdd = None

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
        itemAdd = input("Enter the item you want to add: ").lower()
        AddItem(itemAdd)      
    elif choice == 2:
        ViewList()
    elif choice == 3:
        print("")
    elif choice == 4:
        print("")
    else:
        print("")

def AddItem(itemAdd):
    itemList.append(itemAdd)
    print(f"{itemAdd} has been added to your shopping list")

def ViewList():
    if len(itemList) == 0:
        print("Your shopping list is empty")
    else:
        print(f"Your shopping list:\n{itemList}")

options()

