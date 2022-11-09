# Imports for the script:
import random
import string

# defining the __init__ method for the Hangman class:
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    '''

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f"The mistery word has {self.num_letters} characters.")
        print(self.word_guessed)
    
    # Method to check if guess is in the word and to populate word_guessed if so otherwise remove life
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = letter
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
                print(self.word_guessed)
                break

# Method to play game:
def play_game(word_list):
    game = Hangman(word_list,num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)