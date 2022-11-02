# Importing the random module:
import random
# Importing string module:
import string

# Assigning list above to a variable
word_list = ['strawberry', 'banana', 'pineapple', 'watermelon', 'apple']
# Printing out newly created list
print(word_list)

# Assigning randomly generated word into word variable and print:
word = random.choice(word_list)
print(word)

# Asking user to enter a single ketter and assigning to variable
guess = input("Please guess a single letter: ")

# Checking if length of guess is 1 and an alphabet (lower or upper)
if len(guess) and guess in list(string.ascii_letters):
    print("Good guess!")
else:
    print("Oops! Thats is not a valid input.")