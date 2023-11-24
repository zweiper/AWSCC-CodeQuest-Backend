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
print("|                             Rock, Paper, n' Scissors!                                        |")
print("|                                                                                              |")
print("================================================================================================")

print("\nWelcome to Rock, Paper, n' Scissors!")
print("\nThe rules are simple:\n\tRock is strong against scissors but weak against paper!\n\tPaper is strong against rock but weak against scissors!\n\tScissors are strong against paper but weak against rock!")

print("Would you like to play against computer? (yes [1] | no [0])")
ans = input("Answer: ")

if ans == 0:
    print(f"\nYour turn {p1}: Rock, Paper, or Scissors?")
    choice = input(f"{p1}: ").lower()
    os.system('cls')
    print(f"Your turn {p2}: Rock, Paper, or Scissors?")
    choice2 = input(f"{p2}: ").lower()
    os.system('cls')

    print(f"{p1}: {choice}")
    print(f"{p2}: {choice2}\n")

    if choice == "Rock" or choice == "rocks":
        if choice2 == "rock" or choice2 == "rocks":
            print("Draw")
        elif choice2 == "Paper" or choice2 == "Papers":
            print(f"{p2} wins!")
        elif choice2 == "Scissors" or choice2 == "Scissor":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "Paper" or choice == "Papers":
        if choice2 == "Paper" or choice2 == "Papers":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p1} wins!")
        elif choice2 == "Scissors" or choice2 == "Scissor":
            print(f"{p2} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "Scissors" or choice == "Scissor":
        if choice2 == "Scissors" or choice2 == "Scissor":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p2} wins!")
        elif choice2 == "Paper" or choice2 == "Papers":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
elif ans == 1:
    print(f"\nYour turn {p1}: Rock, Paper, or Scissors?")
    choice = input(f"{p1}: ").lower()
    print(f"\nYour turn {v_ai}: Rock, Paper, or Scissors?")
    choice2 = random.choice(choices).lower()

    if choice == "Rock" or choice == "rocks":
        if choice2 == "rock" or choice2 == "rocks":
            print("Draw")
        elif choice2 == "Paper" or choice2 == "Papers":
            print(f"{v_ai} wins!")
        elif choice2 == "Scissors" or choice2 == "Scissor":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "Paper" or choice == "Papers":
        if choice2 == "Paper" or choice2 == "Papers":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{p1} wins!")
        elif choice2 == "Scissors" or choice2 == "Scissor":
            print(f"{v_ai} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    elif choice == "Scissors" or choice == "Scissor":
        if choice2 == "Scissors" or choice2 == "Scissor":
            print("Draw")
        elif choice2 == "rock" or choice2 == "rocks":
            print(f"{v_ai} wins!")
        elif choice2 == "Paper" or choice2 == "Papers":
            print(f"{p1} wins!")
        else:
            print("That's not one of the choices! Now the game will end because of you :c")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
else:
    print("Invalid Input: Only choose from 1 or 2")