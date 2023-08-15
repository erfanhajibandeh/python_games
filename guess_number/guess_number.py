import random

def computer_guess(lower_limit: int, higher_limit: int):
    # Initialize variables for guess limits and counter
    lower_guess_limit = lower_limit
    higher_guess_limit = higher_limit
    counter = 1

    while True:
        # Generate a random guess within the current limits
        guess = random.randint(lower_guess_limit, higher_guess_limit)

        while True:
            # Ask the user whether the guess is higher (h), lower (l), or correct (c)
            guess_validation = input(f'Is {guess} higher (h) or lower (l) or the correct answer (c)? ')
            if guess_validation not in ['h', 'l', 'c']:
                # Display error message for invalid input
                print("You must answer h, l, or c")
            else:
                break
        
        if guess_validation == 'c':
            # Guessed correctly, display victory message and exit the loop
            print(f'I won after {counter} guesses! Your number is {guess} :)')
            break
        
        elif guess_validation == 'h':
            # Update guess range for the next iteration (guess was too high)
            higher_guess_limit = guess - 1
            counter += 1
            
        elif guess_validation == 'l':
            # Update guess range for the next iteration (guess was too low)
            lower_guess_limit = guess + 1
            counter += 1

        if lower_guess_limit > higher_guess_limit:
            # Invalid range, reset and start a new round of guessing
            print('I cannot guess your number with the provided hints! Let\'s try again :)')
            lower_guess_limit = lower_limit
            higher_guess_limit = higher_limit
            counter = 1

