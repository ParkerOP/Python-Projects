import time


def printBoard(xState, oState):
    zero = 'X' if xState[0] else ("O" if oState[0] else 0)
    one = 'X' if xState[1] else ("O" if oState[1] else 1)
    two = 'X' if xState[2] else ("O" if oState[2] else 2)
    three = 'X' if xState[3] else ("O" if oState[3] else 3)
    four = 'X' if xState[4] else ("O" if oState[4] else 4)
    five = 'X' if xState[5] else ("O" if oState[5] else 5)
    six = 'X' if xState[6] else ("O" if oState[6] else 6)
    seven = 'X' if xState[7] else ("O" if oState[7] else 7)
    eight = 'X' if xState[8] else ("O" if oState[8] else 8)

    print(f'''| {zero} | {one} | {two} |
|---|---|---|
| {three} | {four} | {five} |
|---|---|---|
| {six} | {seven} | {eight} |       
''')


def sum(x, y, z=0):
    return x + y + z


def checkWin(xState, oState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8],
            [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    for i in wins:
        if(sum(xState[i[0]], xState[i[1]], xState[i[2]]) == 3):
            return "x"
        elif(sum(oState[i[0]], oState[i[1]], oState[i[2]]) == 3):
            return "o"
    return -1


if(__name__ == "__main__"):
    print("Welcome to the game of Tic Tac Toe, player!")
    time.sleep(1.5)
    print("How do you want to play the game? Please type 'computer' to play with computer or type 'player' to play a 2 player game.")
    gameChoice = None
    while(True):
        gameChoice = input("").lower()
        if(gameChoice == "computer" or gameChoice == "comp"):
            gameChoice = "comp"
            break
        elif(gameChoice == "player" or gameChoice == "two player" or gameChoice == "2 player"):
            gameChoice = "player"
            break
        else:
            print("That's not a valid option. Please type 'computer' or 'player'.")

    if(gameChoice == "player"):
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        chance = 1
        xTurns = 0
        oTurns = 0
        totalTurns = 0
        while(True):
            print("\n")
            printBoard(xState, oState)
            if(chance == 1):
                print("Player 1's turn : ", end="")
                correctChoice = False
                while(correctChoice != True):
                    xChoice = int(input(""))
                    if(xChoice <= 8):

                        if(xState[xChoice] == 0 and oState[xChoice] == 0):
                            xState[xChoice] = 1
                            xTurns += 1
                            totalTurns += 1
                            correctChoice = True
                        else:
                            print(
                                "That position is already occupied! Please choose another one : ", end="")
                    else:
                        print(
                            "Number out of range! Please choose between 0 to 8 : ", end="")

            elif(chance == 0):
                correctChoice = False
                print("Player 2's turn : ", end="")
                while(correctChoice != True):
                    oChoice = int(input(""))
                    if(oChoice <= 8):
                        if(xState[oChoice] == 0 and oState[oChoice] == 0):
                            oState[oChoice] = 1
                            oTurns += 1
                            totalTurns += 1
                            correctChoice = True
                        else:
                            print(
                                "That position is already occupied! Please choose another one : ", end="")

                    else:
                        print(
                            "Number out of range! Please choose between 0 to 8 : ", end="")

            win = checkWin(xState, oState)
            if(win == "x"):
                printBoard(xState, oState)
                print(f"Game Over! PLayer 1 wins in {xTurns} turns!")
                break
            elif(win == "o"):
                printBoard(xState, oState)
                print(f"Game Over! PLayer 2 wins in {oTurns} turns!")
                break
            elif(totalTurns == 9):
                printBoard(xState, oState)
                print("The match has been tied! You both did a great play.")
                break
            chance = 1 - chance

    if(gameChoice == "comp"):
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        chance = 1
        xTurns = 0
        oTurns = 0
        totalTurns = 0
        while(True):
            print("\n")
            printBoard(xState, oState)

            if(chance == 1):
                print("Player's turn : ", end="")
                correctChoice = False
                while(correctChoice != True):
                    xChoice = int(input(""))
                    if(xChoice <= 8):

                        if(xState[xChoice] == 0 and oState[xChoice] == 0):
                            xState[xChoice] = 1
                            xTurns += 1
                            totalTurns += 1
                            correctChoice = True
                        else:
                            print(
                                "That position is already occupied! Please choose another one : ", end="")
                    else:
                        print(
                            "Number out of range! Please choose between 0 to 8 : ", end="")
            else:
                compString = "Computer's turn :  Playing..."
                time.sleep(1)
                print(compString)
                winChances = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
                    0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
                matchFound = False
                winMoveFound = False
                for g in winChances :
                    if(sum(oState[g[0]], oState[g[1]]) == 2 or sum(oState[g[1]], oState[g[2]]) == 2 or sum(oState[g[0]], oState[g[2]]) == 2):
                        if(xState[g[0]] == 0 and oState[g[0]] == 0):
                            oState[g[0]] = 1
                            oTurns += 1
                            totalTurns += 1
                            winMoveFound = True
                            break
                        elif(xState[g[1]] == 0 and oState[g[1]] == 0):
                            oState[g[1]] = 1
                            oTurns += 1
                            totalTurns += 1
                            winMoveFound = True
                            break
                        elif(xState[g[2]] == 0 and oState[g[2]] == 0):
                            oState[g[2]] = 1
                            oTurns += 1
                            totalTurns += 1
                            winMoveFound = True
                            break
                if(winMoveFound == False) :
                    for i in winChances :
                        if(sum(xState[i[0]], xState[i[1]]) == 2 or sum(xState[i[1]], xState[i[2]]) == 2 or sum(xState[i[0]], xState[i[2]]) == 2):
                            if(xState[i[0]] == 0 and oState[i[0]] == 0):
                                oState[i[0]] = 1
                                oTurns += 1
                                totalTurns += 1
                                matchFound = True
                                break
                            elif(xState[i[1]] == 0 and oState[i[1]] == 0):
                                oState[i[1]] = 1
                                oTurns += 1
                                totalTurns += 1
                                matchFound = True
                                break
                            elif(xState[i[2]] == 0 and oState[i[2]] == 0):
                                oState[i[2]] = 1
                                oTurns += 1
                                totalTurns += 1
                                matchFound = True
                                break
                if(matchFound == False and winMoveFound == False) :
                    for k in winChances:
                        if(xState[k[0]] == 0 and oState[k[0]] == 0):
                            oState[k[0]] = 1
                            oTurns += 1
                            totalTurns += 1
                            break
                        elif(xState[k[1]] == 0 and oState[k[1]] == 0):
                            oState[k[1]] = 1
                            oTurns += 1
                            totalTurns += 1
                            break
                        elif(xState[k[2]] == 0 and oState[k[2]] == 0):
                            oState[k[2]] = 1
                            oTurns += 1
                            totalTurns += 1
                            break

            win = checkWin(xState, oState)
            if(win == "x"):
                printBoard(xState, oState)
                print(f"Game Over! PLayer wins in {xTurns} turns!")
                break
            elif(win == "o"):
                printBoard(xState, oState)
                print(f"Game Over! Computer wins in {oTurns} turns!")
                break
            elif(totalTurns == 9):
                printBoard(xState, oState)
                print("The match has been tied! You played well, player.")
                break
            chance = 1 - chance
