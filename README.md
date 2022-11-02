# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This version of the hangman game has used Python and its packages to construct a UI for the player. 

## Milestone 1: Create variables for the game

Milestone 1 was used to create the list of possible words for the hangman game:
- The list was assigned to a variable and the random module was imported and the choice() method was used to selected a random word from the list and these have both been printed to output
- For the hangman game to be initiated, user input was designed to get input from the user of 1 character.
- Conditional logic was then used to determine if the input from the user is a valid input so has to have a length of 1 and in the alphabet.
- To do the above, the string module was imported as it is much more efficient to do this than write all of the alphabet in lower and upper case within a list.
- Code and accompanying description is provided below for Milestone 1, which will be streamlined more as the milestones progress:
  
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

## Milestone 2

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?

[def]: image.png