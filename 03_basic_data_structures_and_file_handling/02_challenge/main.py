import random

rock = 0
scissors = 1
paper = 2

user_choice = int(input("Select your hands by 0 or 1 or 2 (0:Rock, 1:Scissors, 2:Paper):"))
computer_choice = random.randrange(2)

if user_choice == computer_choice :
    print("The result is Draw.")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("You win!")
else :
    print("You lose.")

