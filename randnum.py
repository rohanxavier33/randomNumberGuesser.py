from random import randint

def parameters():
    start = int(0)
    end = int(100)
    guessNum = int(0)
    maxGuesses = int(5)
    return start, end, guessNum, maxGuesses


def main():
    start, end, guessNum, maxGuesses = parameters()
    print(f"Guess the random number between {start} and {end}. You have {maxGuesses} guesses.")
    # set random number
    number = randint(start, end)
    while True:
        if (guessNum < maxGuesses):
            guess = userInput(start, end)
            # if user guessed right
            if guess == number:
                print(f"You got it! The number was {number}!")
                False
                return 0
            # if user's guess was too low
            elif number > guess:
                guessNum += 1
                print(f"The number is higher than {guess}. You have " + str(maxGuesses - guessNum) +" guesses left.")
                True
            # if user's guess was too high
            elif number < guess:
                guessNum += 1
                print(f"The number is lower than {guess}. You have " + str(maxGuesses - guessNum) +" guesses left.")
                True
        elif guessNum == maxGuesses:
            print(f"You used all {maxGuesses} of your guesses. The number was {number}. You lose!")
            False
            return 0


def userInput(start, end):
    # get user input
    while True:
        try:
            guess = int(input("What is your guess? "))
            if guess < start or guess > end:
                raise ValueError
            else:
                False
                return guess
        except ValueError:
            print(f"Input must be between {start} and {end}")
            True


main()
