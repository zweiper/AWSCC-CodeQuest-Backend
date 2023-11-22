n = "Narrator:"
c = None

print("================================================================================================")
print("|                                                                                              |")
print("|                             Alf's Short Adventure!                                           |")
print("|                                                                                              |")
print("================================================================================================")

print(f"{n} One day, while Alf was walking on the field, a mysterious man in a suit arrived.")

print("\nDo you want to talk to him? (yes [y] | no [n])")
c = input()

if c == "n" or c == "N":
    print(f"\n{n} You disregarded the man and continued the walk.")
    print("The END")
elif c == "y" or c == "Y":
    print("\nAlf: henlo!")
    print(f"{n} The mysterious man heard you and walked towards you. Upon looking at the mysterious man's face, you've noticed that he is bald.")
    print("\nPoint out to him that he is bald? (yes [y] | no [n])")
    c = input()
    
    if c == "y" or c == "Y":
        print("\nThe man laughed and made you his meal.")
        print("You died. The END")
    elif c == "n" or c == "N":
        print(f"\n{n} You didn't say anything...")
        print("Mysterious Man: Hello, you are so cute! What's your name? I'm Jeff Bezos, by the way.")
        print("You: I'm Alf! I'm an alpaca!")
        print("Jeff: Nice to meet you! Since you are cute, I want to offer you a choice. This is a plant that ive been working on, do you want to taste it?")

        print("\nEat the plant? (yes [y] | no [n])")
        c = input()

        if c == "n" or c == "N":
            print("\nYou didn't eat the plant so Jeff ate you instead.")
            print("You died. The END")
        elif c == "y" or c == "Y":
            print(f"\n{n} You have eaten the plant and feel something strange.")
            print("You: I don't feel so good.")
            print("Jeff: That's good, it means that it is working.")
            print(f"\n{n} You have passed out.")
            print(f"{n} You have woken up and saw that Jeff has left.")
            print(f"{n} You walked home and quickly looked at the mirror.")
            print("You: Why do I look so different? I look..")
            print("You: I look suave and cool with this sunglasses and mustache! B)")
            print(f"\n{n} The plant made you a cool Alf.")
            print("The END B)")
        else:
            print("Invalid Input: Only type y or n")
    else:
        print("Invalid Input: Only type y or n")
else:
    print("Invalid Input: Only type y or n")