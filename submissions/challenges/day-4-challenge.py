import os

p1 = "Player 1"
p2 = "Player 2"
choice = None
choice2 = None

print("================================================================================================")
print("|                                                                                              |")
print("|                             Rock, Paper, n' Scissors!                                        |")
print("|                                                                                              |")
print("================================================================================================")

print("\nWelcome to Rock, Paper, n' Scissors!")
print("\nThe rules are simple:\n\tRock is strong against scissors but weak against paper!\n\tPaper is strong against rock but weak against scissors!\n\tScissors are strong against paper but weak against rock!")

print(f"\nYour turn {p1}: Rock, Paper, or Scissors?")
choice = input(f"{p1}: ")
os.system('cls')
print(f"Your turn {p2}: Rock, Paper, or Scissors?")
choice2 = input(f"{p2}: ")
os.system('cls')

print(f"{p1}: {choice}")
print(f"{p2}: {choice2}\n")

if choice == "Rock" or choice == "rock" or choice == "rocks" or choice == "Rocks":
    if choice2 == "Rock" or choice2 == "rock" or choice2 == "rocks" or choice2 == "Rocks":
        print("Draw")
    elif choice2 == "Paper" or choice2 == "Papers" or choice2 == "paper" or choice2 == "papers":
        print(f"{p2} wins!")
    elif choice2 == "Scissors" or choice2 == "Scissor" or choice2 == "scissors" or choice2 == "scissor":
        print(f"{p1} wins!")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
elif choice == "Paper" or choice == "Papers" or choice == "paper" or choice == "papers":
    if choice2 == "Paper" or choice2 == "Papers" or choice2 == "paper" or choice2 == "papers":
        print("Draw")
    elif choice2 == "Rock" or choice2 == "rock" or choice2 == "rocks" or choice2 == "Rocks":
        print(f"{p1} wins!")
    elif choice2 == "Scissors" or choice2 == "Scissor" or choice2 == "scissors" or choice2 == "scissor":
        print(f"{p2} wins!")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
elif choice == "Scissors" or choice == "Scissor" or choice == "scissors" or choice == "scissor":
    if choice2 == "Scissors" or choice2 == "Scissor" or choice2 == "scissors" or choice2 == "scissor":
        print("Draw")
    elif choice2 == "Rock" or choice2 == "rock" or choice2 == "rocks" or choice2 == "Rocks":
        print(f"{p2} wins!")
    elif choice2 == "Paper" or choice2 == "Papers" or choice2 == "paper" or choice2 == "papers":
        print(f"{p1} wins!")
    else:
        print("That's not one of the choices! Now the game will end because of you :c")
else:
    print("That's not one of the choices! Now the game will end because of you :c")