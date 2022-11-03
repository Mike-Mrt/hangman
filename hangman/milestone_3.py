# Importing string module
import string

# Creating a while loop 
while True:
    # Asking user to guess a character and assigning to variable
    guess = input("Guess a letter: ")
    if len(guess)==1 and guess in list(string.ascii_letters):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")