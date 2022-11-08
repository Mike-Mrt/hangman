# Imports for the script:
import random

# defining the __init__ method for the Hangman class:
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(str(self.word))
        self.num_letters = set(str(self.word))
        self.list_of_guessed = []

# testing the initialisation of attributes 
# test1 = Hangman(['apple','pineapple','orange'], 5)
# print(test1.word_list)
# print(test1.num_lives)
# print(test1.word)
# print(test1.word_guessed)
# print(test1.num_letters)
# print(test1.list_of_guessed)