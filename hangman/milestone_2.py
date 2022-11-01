# Importing the random module:
import random

# Assigning list above to a variable
word_list = ['strawberry', 'banana', 'pineapple', 'watermelon', 'apple']
# Printing out newly created list
print(word_list)

# Assigning randomly generated word into word variable and print:
word = random.choice(word_list)
print(word)

# Asking user to enter a single ketter and assigning to variable
guess = input("Please guess a single letter: ")