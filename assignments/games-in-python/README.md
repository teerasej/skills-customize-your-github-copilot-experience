# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice working with strings, loops, conditionals, and user input while creating a complete game experience.

## 📝 Tasks

### 🛠️	Create the Core Hangman Loop

#### Description
Write a Python program that chooses a secret word from a predefined list and lets the player guess one letter at a time.

#### Requirements
Completed program should:

- Randomly select one word from a predefined word list.
- Display the hidden word progress using underscores for unguessed letters.
- Ask the player for a single-letter guess on each turn.
- Reveal all matching letter positions when the guess is correct.


### 🛠️	Handle Game Rules and End Conditions

#### Description
Add game rules for incorrect guesses and finish the game with a clear result message.

#### Requirements
Completed program should:

- Track remaining incorrect guesses and reduce the count only for incorrect letters.
- Prevent repeated guesses from unfairly reducing attempts.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts run out and show the correct word.
