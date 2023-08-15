import random

# Function to get the user's choice
def get_user_input():
    while True:
        try:
            user_hand = str(input(f"Pick 'r' for rock or 'p' for paper or 's' for scissor: "))
            if user_hand not in ['r', 'p', 's']:
                print("You must insert 'r' or 'p' or 's'")
            else:
                break
        except ValueError:
            print("You must insert 'r' or 'p' or 's'")
    
    return user_hand

# Function to generate the computer's choice
def generate_computer_input():
    return random.choice(['r', 'p', 's'])

# Function to determine the winner
def who_wins(user_hand: str, computer_hand: str):
    if user_hand == computer_hand:
        print("It's a tie! Lucky us!")
    elif user_hand == 'r':
        if computer_hand == 'p':
            print('Computer wins! Hahaha!')
        else:
            print('You win, human!')
    elif user_hand == 'p':
        if computer_hand == 's':
            print('Computer wins! Hahaha!')
        else:
            print('You win, human!')
    else:
        if computer_hand == 'r':
            print('Computer wins! Hahaha!')
        else:
            print('You win, human!')
