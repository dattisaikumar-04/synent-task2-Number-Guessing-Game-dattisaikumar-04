import random

secret_number = random.randint(1, 100)
attempts = 0

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

# Temporary: show the number for testing
print("Expected number:", secret_number)

while True:

    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations! 🎉")
        print("You guessed the correct number!")
        print("Number:", secret_number)
        print("Total attempts:", attempts)
        break