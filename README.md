# 🎯 Number Guessing Game (CLI)

A simple **Command-Line Number Guessing Game** where the computer generates a random number and the player tries to guess it. The game provides hints after each attempt and continues until the correct number is guessed.

## 📌 Objective

Create an interactive guessing game that generates a random number and allows the user to make multiple attempts until they guess the correct number.

## ✨ Features

* 🎲 Generates a random number
* ⌨️ Takes user guesses
* 🔄 Allows multiple attempts
* 💡 Provides hints:

  * **Too High**
  * **Too Low**
* 🔢 Counts the number of attempts
* 🏆 Ends the game when the correct number is guessed

## 🎮 How the Game Works

1. The computer generates a random number.
2. The user enters a guess.
3. The program compares the guess with the random number.
4. The program gives a hint:

   * If the guess is higher → **Too High**
   * If the guess is lower → **Too Low**
   * If the guess is correct → **Correct!**
5. The game continues until the user guesses the correct number.
6. The total number of attempts is displayed.

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Open the project folder:

```bash
cd number-guessing-game
```

Run the program:

```bash
python guessing_game.py
```

## 💡 Example Output

```text
🎯 Number Guessing Game

I have selected a number between 1 and 100.

Enter your guess: 50
Too High! Try again.

Enter your guess: 25
Too Low! Try again.

Enter your guess: 37
Too Low! Try again.

Enter your guess: 43
🎉 Correct! You guessed the number.

Total Attempts: 4
```

## 🛠️ Concepts Used

* Random Number Generation
* User Input
* Variables
* Conditional Statements
* Loops
* Comparison Operators
* Attempt Counter
* Basic CLI Programming

## 🎯 Learning Outcome

By completing this project, you will learn how to generate random numbers, use loops for repeated user interaction, compare values, provide hints, and track the number of attempts.



