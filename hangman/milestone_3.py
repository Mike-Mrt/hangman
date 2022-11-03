# Importing string module
import string

# Creating a while loop 
while True:
    # Asking user to guess a character and assigning to variable
    guess = input("Guess a letter: ")
    # Checking if guess is valid
    if len(guess)==1 and guess in list(string.ascii_letters):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Checking whether the guess is in the word:
# This is an example word but this can be randomly generated from milestone_2.py script
word = "apple"
# Creating a list of individual characters of the word
word_list = list(word)

if guess in word_list:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")