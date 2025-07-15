import random 

user_wins = 0 
computer_wins = 0 
ties = 0
options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options: 
        print("Invalid input, try again!")
        continue  # keep asking until valid input is given

    random_number = random.randint(0,2)
    # rock : 0, paper: 1, scissors: 2
    comp_input = options[random_number] # pick a random option for computer
    print("You picked", user_input + ".")
    print("Computer picked", comp_input + ".")

    if user_input == "rock" and comp_input == "scissors":
        print("You won!")
        user_wins += 1 
        
    elif user_input == "paper" and comp_input == "rock":
        print("You won!")
        user_wins += 1 
        
    elif user_input == "scissors" and comp_input == "paper":
        print("You won!")
        user_wins += 1 

    elif user_input == comp_input:
        print("Tie!")
        ties += 1

    else:
        print("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("There were", ties, "ties.")
print("Goodbye!")
