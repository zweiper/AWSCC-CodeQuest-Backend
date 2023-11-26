choice = 0
itemList = []
itemAdd = None

def options():
    print("Options:")
    print("\t1. Add item to the shopping list")
    print("\t2. View shopping list")
    print("\t3. Remove item from the shopping list")
    print("\t4. Quit")

def switchCase(choice):
    if choice == 1:
        itemAdd = input("Enter the item you want to add: ")
        AddItem(itemAdd)       
    elif choice == 2:
        print("")
    elif choice == 3:
        print("")
    elif choice == 4:
        print("")
    else:
        print("")

def AddItem(itemAdd):
    itemList.append(itemAdd)
    print(f"{itemAdd} has been added to your shopping list")

options()
choice = input("Enter the number of your choice: ")
switchCase(choice)