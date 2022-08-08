# PROJECT : SNAKE, WATER AND GUN GAME!

import random
import time

userChoice = input("Choose between Snake, Water and Gun :\n").lower()

if(userChoice == "snake" or userChoice == "water" or userChoice == "gun") :
    gameStarted = True
    print("You've entered the Snake, Water and Gun game! Wait for the Computer to play its turn...")
else :
    gameStarted = False
    print("This is not a correct choice. Try again!")

if(gameStarted == True) :
    time.sleep(1)

options = ["snake", "water", "gun"]
computerChoice = random.choice(options)

if(gameStarted == True and userChoice == "snake" and computerChoice == "snake") :
    print("Computer has chosen Snake!\nThe match has been tied!")
elif(gameStarted == True and userChoice == "snake" and computerChoice == "water") :
    print("Computer has chosen Water!\nYou won the match!")
elif(gameStarted == True and userChoice == "snake" and computerChoice == "gun") :
    print("Computer has chosen Gun!\nYou lost the match!")
elif(gameStarted == True and userChoice == "water" and computerChoice == "snake") :
    print("Computer has chosen Snake!\nYou lost the match!")
elif(gameStarted == True and userChoice == "water" and computerChoice == "water") :
    print("Computer has chosen Water!\nThe match has been tied!")
elif(gameStarted == True and userChoice == "water" and computerChoice == "gun") :
    print("Computer has chosen Gun!\nYou won the match!")
elif(gameStarted == True and userChoice == "gun" and computerChoice == "snake") :
    print("Computer has chosen Snake!\nYou won the match!")
elif(gameStarted == True and userChoice == "gun" and computerChoice == "water") :
    print("Computer has chosen Water!\nYou lost the match!")
elif(gameStarted == True and userChoice == "gun" and computerChoice == "gun") :
    print("Computer has chosen Gun!\nThe match has been tied!")

gameStarted = False    



# Success!