# this is a guessesNumber game
import random
secretNum = random.randint(1,20)
print("I am thinking a number between 1 and 20")

# Ask the plyer to guess 6 times
for guessesTaken in range(1,7):
    print("take a guesses")
    guess = int(input())

    if guess < secretNum:
        print("Your guesses is too low")
    elif guess > secretNum:
        print("Your guesses is to high")
    else:
        break

if guess == secretNum:
    print("Good job! You guesses my number in " + str(guessesTaken)+" guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNum))