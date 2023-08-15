class Word:
    """
    Represents the target word to be guessed in the Hangman game.
    Provides methods to initialize the hidden word and reveal guessed letters.
    """
    
    def __init__(self, game_word):
        """
        Initializes a new Word instance with the given target game word.
        Initializes the hidden word with underscores for unrevealed characters.
        """
        self.game_word = game_word
        self.hidden_word = ['_' for char in self.game_word]

    def reveal_word(self, letter):
        """
        Reveals guessed letters in the hidden word.
        Args:
            letter (str): The guessed letter to reveal in the word.
        """
        for i, char in enumerate(self.game_word):
            if char == letter:
                self.hidden_word[i] = letter


class Hangman:
    """
    Represents the Hangman game, managing game logic and display.
    """
    
    def __init__(self, game_word, gallow_visual, max_lives=7):
        """
        Initializes a new Hangman instance with the target game word, gallows visual,
        maximum allowed lives, and other game state.
        """
        self.word = Word(game_word)
        self.guessed_letters = []
        self.status = 'alive'
        self.lives = max_lives
        self.visual = gallow_visual

    def game_process(self, letter):
        """
        Processes a guessed letter and updates the game state.
        Args:
            letter (str): The guessed letter.
        Returns:
            bool: False if the letter has already been guessed or is not a valid letter.
        """
        if letter in self.guessed_letters or not letter.isalpha() or len(letter) > 1:
            return False
        self.guessed_letters.append(letter)
        if letter.lower() in self.word.game_word:
            self.word.reveal_word(letter.lower())
            if '_' not in self.word.hidden_word:
                self.status = 'You won! :)'
        else:
            self.lives = self.lives - 1
            if self.lives == 0:
                self.status = 'You lost :('

    def display_game_status(self):
        """
        Displays the current game status, including the hidden word, guessed letters,
        remaining lives, game status, and the visual representation of the gallows.
        """
        print('Word: {}'.format(' '.join(self.word.hidden_word)))
        print('Guessed letters: {}'.format(self.guessed_letters))
        print('Number of remaining lives: {}'.format(self.lives))
        print('Status: {}{}'.format(self.status, f', the answer was: {self.word.game_word}' if self.lives == 0 else ''))
        print(self.visual[self.lives])
