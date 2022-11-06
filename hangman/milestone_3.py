# Importing string module
import string

# Creating a while loop 
# while True:
#     # Asking user to guess a character and assigning to variable
#     guess = input("Guess a letter: ")
#     # Checking if guess is valid
#     if len(guess)==1 and guess in list(string.ascii_letters):
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")

# Checking whether the guess is in the word:
# This is an example word but this can be randomly generated from milestone_2.py script
word = "apple"
# Creating a list of individual characters of the word
word_list = list(word)

# if guess in word_list:
#     print(f"Good guess! {guess} is in the word.")
# else:
#     print(f"Sorry, {guess} is not in the word. Try again.")

# Defining functions for the above:
# Checking the guessed letter by the player:
def check_guess(guess):
    letter = guess.lower()
    if letter in word_list:
        print(f"Good guess! {letter} is in the word.")
    else:
        print(f"Sorry, {letter} is not in the word. Try again.")

# Asking the user for input:
def ask_for_input():
    while True:
        # Asking user to guess a character and assigning to variable
        guess = input("Guess a letter: ")
        # Checking if guess is valid
        if len(guess)==1 and guess in list(string.ascii_letters):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

# Testing ask_for_input() function:
ask_for_input()