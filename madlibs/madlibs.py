import random 

# Function to get user input for a specific word type
def get_input(word: str): 
    title = input(f'Insert {word}: ')
    return title

# Function to generate and display the filled madlib
def generate_madlib(adj1,adj2,verb1,verb2): 
    # Read madlibs from the text file
    with open('madlibs.txt', 'r') as file:
        madlibs = file.read().splitlines()
        
    # Randomly pick a madlib from the list
    random_madlib = random.choice(madlibs)
    
    # Print the filled madlib using named placeholders
    print(random_madlib.format(adj1=adj1, adj2=adj2, verb1=verb1, verb2=verb2))