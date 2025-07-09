print("Welcome to Rock Paper and Scissors game")

import random

rock = '''
    _______
---'    ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
          _______)
          ________)
         _______)
---.__________)

'''

scissor = '''
    _______
---'    ____)____
          _______)
        __________)
      (____)
---.__(___)

'''

game_images = [rock, paper, scissor] # list to store game images
game_names = ["Rock", "Paper", "Scissor"] # list to store names

user_choice = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissor: "))

if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, you lose!")
else:
    # Print user's choice (name and art)
    print(f"You chose: {game_names[user_choice]}")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    # Print computer's choice (name and art)
    print(f"Computer chose: {game_names[computer_choice]}")
    print(game_images[computer_choice])

    # Now, use conditions to determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2): # Rock vs Scissor
        print("You win!")
    elif (user_choice == 1 and computer_choice == 0): # Paper vs Rock
        print("You win!")
    elif (user_choice == 2 and computer_choice == 1): # Scissor vs Paper
        print("You win!")
    else:
        print("You lose!")