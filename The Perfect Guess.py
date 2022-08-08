# PROJECT : THE PERFECT GUESS!

import random
import time

game = input("Do you want to play The Perfect Guess? Yes/No ").lower()

if(game == "yes" or game == "y"):
    gameStarted = True
elif(game == "no" or game == "n"):
    gameStarted = False
    print("Got it. Do come back later!")
else:
    print("Please choose between yes or no!")
    gameStarted = False


if(gameStarted == True):

    computerChoice = random.randint(0, 1000)
    print("Computer has chosen a number! It lies between 0 and 1000...")
    time.sleep(0.5)

    while(True):
        try:
            userChoice = int(input("Can you guess it? Type it below!\n"))
            guessNumber = 1
            break
        except:
            print("That's not a number!")

else:
    pass


while(gameStarted == True):

    if(userChoice < computerChoice and userChoice > 0):

        print("That is not correct. Higher number please!")

        while(True) :

            try:
                userChoice = int(input("Can you guess it?"))
                break
            except:
                print("That's not a number!")

        guessNumber += 1

    elif(userChoice > computerChoice and userChoice < 1000) :

        print("That is not correct. Lower number please!")

        while(True) :

            try:
                userChoice = int(input("Can you guess it?"))
                break
            except:
                print("That's not a number!")

        guessNumber += 1

    elif(userChoice > 1000 or userChoice < 0) :

        print("Number out of range!")

        while(True) :

            try :

                userChoice = int(input("Can you guess it?"))
                break
            except:
                print("That's not a number!")

    elif(userChoice == computerChoice) :

        print(
            f"That is the correct guess. Congratulations! It took you {guessNumber} turns.")

        gameStarted = False



# Success!

