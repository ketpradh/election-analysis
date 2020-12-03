# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print(f'Computer picked:{computer_choice}')
# Run Conditionals
if user_choice == 'r' :
    if computer_choice =='r':
        print("Tie")
    elif computer_choice == 'p':
        print("Computer Wins")
    elif computer_choice == 's':
        print("You win")
if user_choice == 'p' :
    if computer_choice =='p':
        print("Tie")
    elif computer_choice == 's':
        print("Computer Wins")
    elif computer_choice == 'r':
        print("You win")
if user_choice == 's' :
    if computer_choice =='s':
        print("Tie")
    elif computer_choice == 'r':
        print("Computer Wins")
    elif computer_choice == 'p':
        print("You win")    
