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

Milestone 2 was used to create 2 functions that will aid in the running of the game:
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

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?

[def]: image.png
[def2]: /readme_files/Milestone3.png