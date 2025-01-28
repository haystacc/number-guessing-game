import random
import sys

# setup
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.\n")

try:
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())
except:
    highscore = sys.maxsize

print(f"The current highscore is {highscore}")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)\n")

choice = int(input("Enter your choice: "))
print("")

if choice == 1:
    difficulty = "easy"
    numChances = 10
elif choice == 2:
    difficulty = "medium"
    numChances = 5
elif choice == 3:
    difficulty = "hard"
    numChances = 3
else:
    print("Invalid choice. Please select a number from 1 to 3.")
    quit()

print(f"Great! You have selected the {difficulty} difficulty level.")
print("Let's start the game!\n")

# game
correctNum = 50

numAttempts = 0
while numAttempts < numChances:
    guess = int(input("Enter your guess: "))
    if guess == correctNum:
        print(f"Congratulations! You guessed the correct number in {numAttempts + 1} attempts.")

        if numAttempts < highscore:
            highscore = numAttempts + 1
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            print(f"It's a new highscore! The lowest is now {highscore} attempts.")

        quit()
    elif guess < correctNum:
        print(f"Incorrect! The number is greater than {guess}\n")
    else:
        print(f"Incorrect! The number is less than {guess}\n")
    
    numAttempts += 1

print("You have run out of attempts to guess the correct number :(")