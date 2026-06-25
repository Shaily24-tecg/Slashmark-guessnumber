import random  # bring in the random number 
import time

number = random.randint(1, 200)  # pick the number between 1 and 200

def intro():
    print("Hello! Welcome to the Guessing Game!")
    print("==== Menu ====")
    print("You have 6 chances. Use them wisely.")
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Let's Go. Guess!")
    return name  # IMPORTANT FIX

def pick(name):  # FIX: name passed here
    guessesTaken = 0
    number = random.randint(1, 200)  # FIX: moved inside function

    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)

            if guess <= 200 and guess >= 1:
                guessesTaken = guessesTaken + 1

                # CHANCES DISPLAY
                print("Remaining chances:", 6 - guessesTaken)

                if guess < number:
                    print("The guess is too low")

                elif guess > number:
                    print("The guess is too high")

                else:
                    break

                if guessesTaken < 6:
                    time.sleep(.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number is out of range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except ValueError:  # FIXED
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    else:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"

while playagain.lower() in ["yes", "y"]:
    name = intro()
    pick(name)

    print("Do you want to play again? yes or no")
    playagain = input()