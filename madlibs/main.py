from madlibs import get_input, generate_madlib

def main():
    # Get user input for adjectives and verbs
    adj1 = get_input('an adjective: ')
    adj2 = get_input('another adjective: ')
    verb1 = get_input('a verb: ')
    verb2 = get_input('another verb: ')

    # Generate and display the madlib
    generate_madlib(adj1, adj2, verb1, verb2)

if __name__ == "__main__":
    main()
