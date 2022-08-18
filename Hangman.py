from words_for_hangman import *
import random
import time

def obtain_word() :
    selected_word = random.choice(word_list).upper()
    return selected_word

def display(tries) :
    hang_man = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return hang_man[tries]

def hangman(word) :
    tries = 6
    listletters = list(word)
    underscores = ["_"]*len(word)
    win = False
    print("Welcome to Hangman, player! Do you have what it takes to be a pro guesser?\n")
    time.sleep(0.5)
    print("Computer has chosen a word. Can you guess it?\n")
    print(f"{display(tries)}\n")
    print(f"Tries remaining :  {tries}")
    underscore_updated = " ".join(underscores)
    print(f"{underscore_updated}\n")
    userInput = None
    acceptedChoice = False
    letterCount = 0
    while(win == False) :
        if(letterCount != len(word) and tries > 0) :
            while(acceptedChoice == False) :
                userInput = input("Guess a letter from the word : ").upper()
                if(userInput.isalpha() == True and len(userInput) == 1) :
                    acceptedChoice = True
                else :
                    print("Input can be only a single alphabetical character.")

            if(userInput in word) :
                print(f"\n{display(tries)}\n")
                print("\nYou guessed it right!\n")
                enumerated_list = list(enumerate(word))
                for count,i in enumerated_list :
                    if(enumerated_list[count][1] == userInput) :
                        underscores[count] = userInput
                        underscore_updated = " ".join(underscores)
                        letterCount += 1
                acceptedChoice = False      
                print(underscore_updated)
            elif(userInput not in word) :
                tries -= 1
                print(f"Oops! Letter '{userInput}' is not present in the word.")
                time.sleep(0.5)
                print(f"\n{display(tries)}\n")
                print(f"Tries remaining : {tries}")
                acceptedChoice = False
        elif(tries <= 0) :
            break
        else :
            print("You guessed the word correctly!")
            win = True

        if(win == True) :
            print("Congratulations, you saved the man!")
        elif(tries <= 0) :
            print(f"Better luck next time! The word was : {word}.")


def play() :
    word = obtain_word()
    hangman(word)
    print("Do you want to play again? Y/N")
    while(True) :
        userChoice = input("").lower()
        if(userChoice == "yes" or userChoice == "y") :
            word = obtain_word()
            hangman(word)
            break
        elif(userChoice == "no" or userChoice == "n") :
            break
        else :
            print("That's not a valid choice.")


        


if __name__ == "__main__"  :

    play()
    