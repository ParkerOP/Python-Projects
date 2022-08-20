from words_for_hangman import *
import random
import time


def obtain_word():
    selected_word = random.choice(word_list).upper()
    return selected_word


def display(tries):
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


def hangman(word):
    tries = 6
    listletters = list(word)
    listletters2 = list(word)
    alreadyGuessed = []
    alreadyGuessedRightLetters = []
    underscores = ["_"]*len(word)
    win = False
    print("Welcome to Hangman, player! Do you have what it takes to be a pro guesser?\n")
    time.sleep(0.5)
    print("Computer has chosen a word. Can you guess it?\nHint available : You can type type 'hint' to activate it.\n")
    print(f"{display(tries)}\n")
    print(f"Tries remaining :  {tries}")
    underscore_updated = " ".join(underscores)
    print(f"{underscore_updated}\n")
    userInput = None
    acceptedChoice = False
    letterCount = 0
    hintsRemaining = 2

    while(win == False):
        a = False
        if(letterCount != len(listletters) and tries > 0):
            while(acceptedChoice == False):
                userInput = input("Guess a letter from the word : ").upper()
                if(userInput.isalpha() == True and len(userInput) == 1):
                    acceptedChoice = True
                elif(userInput == "HINT"):
                    acceptedChoice = True
                else:
                    print(
                        "Input can be only a single alphabetical character or 'hint'.")

            if(userInput == "HINT"):
                if(letterCount == len(word) - 1):
                    print("Hints can't be used when only the last letter is remaining!")
                    acceptedChoice = False
                elif(letterCount < len(word) - 1 and hintsRemaining > 0):
                    time.sleep(0.2)
                    print(
                        f"The Hint tool has been used.\nA random letter from the word will be filled in for you. Remaining Hints: {hintsRemaining-1}\n")
                    wordFilled = random.choice(listletters2)
                    while(hintsRemaining > 0 and a == False):
                        if(wordFilled not in alreadyGuessedRightLetters):
                            enumerated_list = list(enumerate(listletters))
                            for count, i in enumerated_list:
                                if(enumerated_list[count][1] == wordFilled):
                                    underscores[count] = wordFilled
                                    underscore_updated = " ".join(underscores)
                                    letterCount += 1
                                    listletters[count] = "$"
                                    break
                            alreadyGuessedRightLetters.append(wordFilled)
                            hintsRemaining -= 1
                            acceptedChoice = False
                            time.sleep(0.5)
                            print(f"{underscore_updated}\n")
                            a = True
                        elif(wordFilled in alreadyGuessedRightLetters):
                            wordFilled = random.choice(listletters2)
                            if(wordFilled not in alreadyGuessedRightLetters):
                                enumerated_list = list(enumerate(listletters))
                                for count, i in enumerated_list:
                                    if(enumerated_list[count][1] == wordFilled):
                                        underscores[count] = wordFilled
                                        underscore_updated = " ".join(
                                            underscores)
                                        letterCount += 1
                                        listletters[count] = "$"
                                        break
                                alreadyGuessedRightLetters.append(wordFilled)
                                hintsRemaining -= 1
                                acceptedChoice = False
                                time.sleep(0.5)
                                print(f"{underscore_updated}\n")
                                a = True
                            else:
                                pass

                else:
                    print("Hint has already been used twice.")
                    acceptedChoice = False

            elif(userInput in listletters):
                print(f"\n{display(tries)}\n")
                print("\nYou guessed it right!\n")
                enumerated_list = list(enumerate(listletters))
                for count, i in enumerated_list:
                    if(enumerated_list[count][1] == userInput):
                        underscores[count] = userInput
                        underscore_updated = " ".join(underscores)
                        letterCount += 1
                        listletters[count] = "$"
                        break
                alreadyGuessed.append(userInput)
                alreadyGuessedRightLetters.append(userInput)

                acceptedChoice = False
                print(f"{underscore_updated}\n")
            elif(userInput not in listletters):
                tries -= 1
                print(
                    f"Oops! Letter '{userInput}' is not present in the word.")
                time.sleep(0.5)
                print(f"\n{display(tries)}\n")
                print(f"\nTries remaining : {tries}")
                alreadyGuessed.append(userInput)
                acceptedChoice = False
                print(f"{underscore_updated}\n")
        elif(tries <= 0):
            break
        else:
            print("You guessed the word correctly!")
            win = True

        if(win == True):
            print("Congratulations, you saved the man!")
        elif(tries <= 0):
            print(f"Better luck next time! The word was : {word}.")
            alreadyGuessedString = ", ".join(alreadyGuessed)
            print(
                f"\nYou guesses were the following : {alreadyGuessedString.upper()}")


def play():
    word = obtain_word()
    hangman(word)
    while(True):
        userChoice = input("Do you want to play again? Y/N ").lower()
        if(userChoice == "yes" or userChoice == "y"):
            word = obtain_word()
            hangman(word)

        elif(userChoice == "no" or userChoice == "n"):
            break
        else:
            print("That's not a valid choice.")



if __name__ == "__main__":

    play()



# Success!
