# Imports for the script:
import random
import string

# defining the __init__ method for the Hangman class:
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    # Method to check if guess is in the word and to populate word_guessed if so otherwise remove life
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = letter
                    return self.word_guessed
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)


    # Method which asks the user for input (a letter) continuously until the while loop is broken
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter that you think is in the word: ")
            if len(guess) != 1 or guess not in list(string.ascii_letters):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)




# testing the initialisation of attributes: 
# test1 = Hangman(['apple','pineapple','orange'], 5)
# print(test1.word_list)
# print(test1.num_lives)
# print(test1.word)
# print(test1.word_guessed)
# print(test1.num_letters)
# print(test1.list_of_guesses)
# print(test1.num_letters)
# test1.ask_for_input()