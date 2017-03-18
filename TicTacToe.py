#Netsec Beginner - 3/1/17
#Tic Tac Toe Terminal Game

#Import OS To Clear Terminal
import os

#Global Variables
Spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
CurrentPlayer = "X"

#Main Function
def main():
    #Loop Until Game Over
    while True:
        #Print Game Board
        PrintBoard()

        #Get Player Input
        PlayerInput()

        #Print Board Second Time(To Show Last Input On Win)
        PrintBoard()

        #Check To See If Either Player Has Won
        if CheckForWin("X") == "X":
            XWins()
            Replay()
        elif CheckForWin("O") == "O":
            YWins()
            Replay()
        elif CheckForWin("X") == "TIE":
            CatScratch()
            Replay()

#Prints Game Board
def PrintBoard():
    #Use Spaces Variable
    global Spaces

    #Clear Terminal
    os.system("clear")

    #Prints Board
    print(Spaces[0] + " | " + Spaces[1] + " | " + Spaces[2])
    print("---------")
    print(Spaces[3] + " | " + Spaces[4] + " | " + Spaces[5])
    print("---------")
    print(Spaces[6] + " | " + Spaces[7] + " | " + Spaces[8])

#Marks a Space
def Turn(space):
    #Use Spaces and CurrentPlayer Variables
    global Spaces
    global CurrentPlayer

    #If X's Turn
    if CurrentPlayer == "X":
        Spaces[int(space) - 1] = "X"
        #Player Toggled
        CurrentPlayer = "O"

    #If Y's Turn
    elif CurrentPlayer == "O":
        Spaces[int(space) - 1] = "O"
        #Player Toggled
        CurrentPlayer = "X"

#Clears Board After Game
def ClearBoard():
    #Use Spaces Variable
    global Spaces

    #Run Through and Reset Spaces List
    for i in range(0, len(Spaces)):
        Spaces[i] = str(int(i + 1))

#Gets Input For Player's Turns
def PlayerInput():
    #Use CurrentPlayer Variable
    global CurrentPlayer

    #Print Instructions
    print("\nEnter Number of Space Below:")

    #Input
    SpaceChosen = str(raw_input("\n" + CurrentPlayer + ">"))

    #Input Passed To Turn Function
    if int(SpaceChosen) > 0:
        Turn(SpaceChosen)
    else:
        PlayerInput()

#Print X Wins Message
def XWins():
    #Generated With Figlet Command In DuckDuckGo
    print("__  _ __        ___           _ ")
    print("\ \/  \ \      / (_)_ __  ___| |")
    print(" \  /  \ \ /\ / /| | '_ \/ __| |")
    print(" /  \   \ V  V / | | | | \__ |_|")
    print("/_/\_\   \_/\_/  |_|_| |_|___(_)")

#Print Y Wins Message
def YWins():
    #Generated With Figlet Command In DuckDuckGo
    print("  ___  __        ___           _  ")
    print(" / _ \ \ \      / (_)_ __  ___| |")
    print("| | | | \ \ /\ / /| | '_ \/ __| |")
    print("| |_| |  \ V  V / | | | | \__ |_|")
    print(" \___/    \_/\_/  |_|_| |_|___(_)")

#Prints In Case of a Tie
def CatScratch():
    #Generated With Figlet Command In DuckDuckGo
    print("           _                      _       _     ")
    print("  ___ __ _| |_ ___  ___ _ __ __ _| |_ ___| |__  ")
    print(" / __/ _` | __/ __|/ __| '__/ _` | __/ __| '_ \ ")
    print("| (_| (_| | |_\__ | (__| | | (_| | || (__| | | |")
    print(" \___\__,_|\__|___/\___|_|  \__,_|\__\___|_| |_|")

#Option to Replay
def Replay():
    #Use CurrentPlayer Variable
    global CurrentPlayer

    #Print Instructions
    print("Replay")

    #Replay?
    ReplayInput = str(raw_input("(y/n): "))

    #Input Interpreted
    if ReplayInput == "y" or ReplayInput == "Y":
        ClearBoard()
        CurrentPlayer = "X"
        main()
    else:
        ExitMessage()

#Says Goodbye to Players
def ExitMessage():
    os.system("clear")
    print("Goodbye :)")
    exit()

#Checks to see if either player has won
def CheckForWin(Player):
    #Use Spaces Variable
    global Spaces

    #Check To See If The Player Has Won
    if Spaces[0] == Player and Spaces[1] == Player and Spaces[2] == Player: #Top Row
        return Player
    elif Spaces[3] == Player and Spaces[4] == Player and Spaces[5] == Player: #Middle Row
        return Player
    elif Spaces[6] == Player and Spaces[7] == Player and Spaces[8] == Player: #Bottom Row
        return Player

    elif Spaces[0] == Player and Spaces[3] == Player and Spaces[6] == Player: #First Column
        return Player
    elif Spaces[1] == Player and Spaces[4] == Player and Spaces[7] == Player: #Second Column
        return Player
    elif Spaces[2] == Player and Spaces[5] == Player and Spaces[8] == Player: #Third Column
        return Player

    elif Spaces[0] == Player and Spaces[4] == Player and Spaces[8] == Player: #Diagonal(\)
        return Player
    elif Spaces[2] == Player and Spaces[4] == Player and Spaces[6] == Player: #Diagonal(/)
        return Player

    #Check For Tie
    else:
        UsedSpacesCount = 0 #If It Equals Nine, There Is a Tie
        for i in range(0, len(Spaces)):
            if Spaces[i] == "X" or Spaces[i] == "O":
                UsedSpacesCount += 1
        if UsedSpacesCount == 9:
            return "TIE"

#Call Main Function
main()
