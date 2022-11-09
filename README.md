# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This version of the hangman game has used Python and its packages to construct a UI for the player. 

## Milestone 2: Create variables for the game

Milestone 2 was used to create the list of possible words for the hangman game:
- The list was assigned to a variable and the random module was imported and the choice() method was used to selected a random word from the list and these have both been printed to output.
- For the hangman game to be initiated, user input was designed to get input from the user of 1 character.
- Conditional logic was then used to determine if the input from the user is a valid input so has to have a length of 1 and in the alphabet.
- To do the above, the string module was imported as it is much more efficient to do this than write all of the alphabet in lower and upper case within a list.
- Code and accompanying description is provided below for Milestone 2, which will be streamlined more as the milestones progress:
  
```python
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
```

> ![](/readme_files/Milestone1.png)

## Milestone 3: Check if the guessed chracter is in the word

Milestone 3 was used to create 3 functions that will aid in the running of the game:
- The 'check_guess' functons which takes in the guessed string as a parameter, converts this into lower case and then checks if the letter is in the word or not.
- The 'ask_for_input' function asks the user for input until the guessed value is valid (length of 1 and a letter). 
- Once valid, the guess moves on and check_guess method is called to check if the guess is in the word.
- Code and accompanying description is provided below for Milestone 3, which will be streamlined more as the milestones progress:


```python
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
```

> ![](/readme_files/Mileston3.png)

## Milestone 4: Create the Game class

Milestone 4 was used to create the Hangman class, instantiate the attributes and defining the functions check_guess and ask_for_input:
- The random and string modules were imported to support the build of the Hangman class.
- Several attributes were initialised, these include:
    - word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
    - word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
    - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
    - num_lives: int - The number of lives the player has at the start of the game
    - word_list: list - A list of words.
    - list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.
- check_guess instance method was created to check whether the guess was in the word or not and added conditional logic for each scenario
- ask_for_input instance method was created to continuously ask the user for input (of a letter)
- These methods included checks to ensure validity of the guesses and actions for each scenario of whether it was a valid single alphabetical letter, if the letter had already been guessed and then actions for when the guessed letter is in and not in the word
- Code and accompanying description is provided below for Milestone 4, which will be streamlined more as the milestones progress:

```python
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
```
> ![](/readme_files/Milestone4.png)

## Milestone 4: Create the Game class

Milestone 5 was used to compile the Hangman game together:
- All the code from milestone 4 was copied over
- play_game function was created to create an instance of the Hangman class
- The above would then continue until the game was won (lives remain and all letters guessed) or lost (number of lives reaches 0)
- Code and accompanying description is provided below for Milestone 5:

```python
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
```
>![](/readme_files/Milestone5.png)


## Conclusions

The Hangman class was created and its attributes initialised. Within this class methods were created to support the running of the game and then a final method outside of the class was creatd to create an instance of the class everytime a user wanted to play the game. 

The game could be improved through creating a longer list of words that the player can guess from and the use of better visualisations instead of using the terminal. 