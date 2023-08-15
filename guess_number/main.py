from guess_number import computer_guess

def main():
    # Loop until valid lower and higher limits are provided
    while True:
        try:
            lower_limit = int(input('Insert a lower limit integer: '))
            higher_limit = int(input('Insert a higher limit integer: '))
            
            if lower_limit >= higher_limit:
                print('Error: the higher limit must be higher than the lower limit. Try again!')
            else:
                break
            
        except ValueError:
            print('Error: you must select an integer. Try again!')
    
    # Call the computer_guess function with user-defined limits
    computer_guess(lower_limit, higher_limit)

if __name__ == "__main__":
    main()
