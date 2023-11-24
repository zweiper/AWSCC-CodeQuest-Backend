import os
import random

p1 = "Player 1"
p2 = "Player 2"
v_ai = "Computer"
choices = ["rock", "paper", "scissors"]
choice = None
choice2 = None
ans = None

print("================================================================================================")
print("|                                                                                              |")
print("|                             rock, paper, n' scissors!                                        |")
print("|                                                                                              |")
print("================================================================================================")

print("\nWelcome to rock, paper, n' scissors!")
print("\nThe rules are simple:\n\tRock is strong against scissors but weak against paper!\n\tPaper is strong against rock but weak against scissors!\n\tscissors are strong against paper but weak against rock!")

print("\nWould you like to play against computer? (yes [1] | no [0])")
ans = int(input("Answer: "))

if ans == 0:
    print(f"\nYour turn {p1}: rock, paper, or scissors?")
    choice = input(f"{p1}: ").lower()
    os.system('cls')
    print(f"Your turn {p2}: rock, paper, or scissors?")
    choice2 = input(f"{p2}: ").lower()
    os.system('cls')

    print(f"{p1}: {choice}")
    print(f"{p2}: {choice2}\n")

    if choice == "rock" or choice == "rocks":
        if choice2 == "rock" or choice2 == "rocks":
            print("Draw")
        elif choice2 == "paper" or choice2 == "papers":
            print(f"{p2} wins!")
        elif choice2 == "scissors" or choice2 == "scissor":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "paper" or choice == "papers":
        if choice2 == "paper" or choice2 == "papers":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p1} wins!")
        elif choice2 == "scissors" or choice2 == "scissor":
            print(f"{p2} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "scissors" or choice == "scissor":
        if choice2 == "scissors" or choice2 == "scissor":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p2} wins!")
        elif choice2 == "paper" or choice2 == "papers":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
elif ans == 1:
    print(f"\nYour turn {p1}: rock, paper, or scissors?")
    choice = input(f"{p1}: ").lower()
    print(f"\nYour turn {v_ai}: rock, paper, or scissors?")
    choice2 = random.choice(choices)

    print(f"{p1}: {choice}")
    print(f"{v_ai}: {choice2}\n")

    if choice == "rock" or choice == "rocks":
        if choice2 == "rock" or choice2 == "rocks":
            print("Draw")
        elif choice2 == "paper" or choice2 == "papers":
            print(f"{v_ai} wins!")
        elif choice2 == "scissors" or choice2 == "scissor":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "paper" or choice == "papers":
        if choice2 == "paper" or choice2 == "papers":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p1} wins!")
        elif choice2 == "scissors" or choice2 == "scissor":
            print(f"{v_ai} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "scissors" or choice == "scissor":
        if choice2 == "scissors" or choice2 == "scissor":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{v_ai} wins!")
        elif choice2 == "paper" or choice2 == "papers":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
else:
    print("Invalid Input: Only choose from 1 or 2")