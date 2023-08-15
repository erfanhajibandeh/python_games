import random
from hangman import Hangman  # Import the Hangman class from the 'hangman' module
from hangman_visual import lives_gallow_dict  # Import the 'lives_gallow_dict' from the 'hangman_visual' module

# Define the main function to run the Hangman game
def main():
    # Read a list of words from a file and select a random word
    with open('words.txt', 'r') as file:
        content = file.read().split(",")
        word_list = [word.strip('"') for word in content]
        selected_word = random.choice(word_list)
    
    # Create an instance of the Hangman class with the selected word and gallows visual
    hangman = Hangman(selected_word, lives_gallow_dict)
    
    # Main game loop: Keep playing until the game status is not 'alive'
    while hangman.status == 'alive':
        # Get a letter guess from the player
        guess = input("Guess a letter: ").strip()
        
        # Process the guess and update the game status
        hangman.game_process(guess)
        
        # Display the current game status
        hangman.display_game_status()

if __name__ == '__main__':
    main()
