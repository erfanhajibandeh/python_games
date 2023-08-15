# Import necessary functions from the 'rock_paper_scissor' module
from rock_paper_scissor import get_user_input, generate_computer_input, who_wins

# Define the main function for running the game
def main():
    while True:
        # Get user's choice
        user_input = get_user_input()
        
        # Generate computer's choice
        computer_input = generate_computer_input()
        
        # Determine the winner of the game
        who_wins(user_input, computer_input)
    
# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
