#Netsec Beginner - 3/14/17
#Hangman Terminal Game

#Import OS to clear Terminal; Random to select random word
import os
import random

#Global Variables
WordList = ["apple", "cat", "dog", "hair", "million", "cup", "plate", "orange", "paper", "ten"] #List of Strings for Single Player
CurrentWord = ["", ""] #Stores the current word for comparison and blank version of Current Word
Strikes = 0 #Stores Number of Wrong Answers; 6 Ends the Game
#Banks of Unused and Used Letters
UnusedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UsedLetters = []

#Main Function
def main():
    #Player Decides If Single Player or Two Player
    Mode = SelectMode()

    #If Single, Choose Random Word from List; if Two, Get Word
    if Mode == "Single":
        RandomWord()
    elif Mode == "Multi":
        GetWord()

    #Loop Until Game Over
    while True:
        PrintGameBoard() #Prints Game Board and Gets Input
        CheckForWin() #Checks For Win/Loss

#Prompts the user to select a game mode
def SelectMode():
    #Print Instructions
    print("Please Choose A Mode of Gameplay:")
    print("\t1) Single Player")
    print("\t2) Two Player")

    #Get User Input
    GameMode = str(raw_input(">"))

    #Evaluate Input
    if GameMode == "1":
        return "Single"
    elif GameMode == "2":
        return "Multi"
    else:
        print("\n***Please Enter Number of Selection***\n")
        SelectMode()

#Selects Random Word From List
def RandomWord():
    #Use WordList and CurrentWord Variables
    global WordList

    #Get Random Integer
    Word = random.randint(0, len(WordList))

    #Set Word
    CurrentWord[0] = WordList[Word]
    CurrentWord[1] = BlankWord(WordList[Word])

def GetWord():
    #Clear Terminal
    os.system("clear")

    #Print Instructions
    print("Enter Word Below:")

    #Get Word From Second Player
    Word = str(raw_input(">"))

    #Set Word
    CurrentWord[0] = Word
    CurrentWord[1] = BlankWord(Word)

#Creates Blank Version of Current Word
def BlankWord(Word):
    #Create Temporary Blank Word Variable
    BlankWord = ""

    #Fill In Blank Word Variable
    for i in range(0, len(Word)):
        BlankWord = BlankWord + "*"

    #Return Blank Word Variable
    return BlankWord

#Prints the Game Board
def PrintGameBoard():
    #Clear Terminal
    os.system("clear")

    #Use CurrentWord Variable
    global CurrentWord

    #Print and Check Letter
    PrintGallows() #Print Man and Gallows
    print("Word: " + CurrentWord[1]) #Print Word
    PrintBank() #Print Letter Bank
    PrintUsed() #Print Used Letters
    Letter = SelectLetter() #Get User Input
    CheckLetter(Letter) #Checks Letter Against Word

#Prints The Hanging Man and Gallows
def PrintGallows():
    #Use Strikes Variable
    global Strikes

    #Prints Gallows Based on Number of Strikes
    if Strikes == 0:
        print(" ----\ ")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("-----------")
    elif Strikes == 1:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("-----------")
    elif Strikes == 2:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("-----------")
    elif Strikes == 3:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print(" |\  |")
        print("     |")
        print("     |")
        print("-----------")
    elif Strikes == 4:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("     |")
        print("-----------")
    elif Strikes == 5:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("     |")
        print("-----------")
    elif Strikes == 6:
        print(" ----\ ")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("-----------")

#Prints Unused Letters
def PrintBank():
    #Use UnusedLetters Variable
    global UnusedLetters

    #Print Letter Bank
    print("\nUnused Letters:")
    print(UnusedLetters)
    print("")

#Prints Used Letters
def PrintUsed():
    #Use UsedLetters Variable
    global UsedLetters

    #Print Used Letter Bank
    print("\nUsed Letters:")
    print(UsedLetters)
    print("")

#Gets Letters From User
def SelectLetter():
    #Give Instructions
    print("Enter Letter Below:")

    #Get User Input
    Letter = raw_input(">")

    #Export Letter
    return Letter

#Checks Letter Against Current Word
def CheckLetter(Letter):
    #Use CurrentWord, UnusedLetters, UsedLetters, and Strikes Variables
    global CurrentWord
    global UnusedLetters
    global UsedLetters
    global Strikes

    #Changed to True if Word Changes
    HasChanged = False

    #Check Letter
    for i in range(0, len(CurrentWord[0])):
        if CurrentWord[0][i] == str(Letter):
            List = list(CurrentWord[1]) #Turn String into List to change letter
            List[i] = str(Letter)
            CurrentWord[1] = "".join(List)
            HasChanged = True

    #Check to see if Word Changed
    if HasChanged == False:
        Strikes += 1

    #Update Used/Unused Letters
    for i in range(0, len(UnusedLetters)):
        if UnusedLetters[i] == str(Letter):
            list(UnusedLetters[i]).pop()
    UsedLetters.append(str(Letter))

#Check To See if Player Has Won or Lost
def CheckForWin():
    #Use Strikes and Current Word Variables
    global Strikes
    global CurrentWord

    #Check For Win
    if CurrentWord[0] == CurrentWord[1]:
        PlayerWins()
        PlayAgain()
    elif Strikes == 6: #Checks Number of Strikes
        PlayerLoses()
        PlayAgain()

#Displays Message if Player Wins
def PlayerWins():
    print("You Win!")

#Displays Message if Player Loses
def PlayerLoses():
    print("You Lose!")

#Gives Player option to Play Again
def PlayAgain():
    #Use Strikes, CurrentWord, UsedLetters, and UnusedLetters Variables
    global Strikes
    global CurrentWord
    global UsedLetters
    global UnusedLetters

    #Get Player Input/Print Instructions
    PlayAgain = str(raw_input("Play Again(y/n)>"))

    #If User Wants New Game, Reset, Call Main; Otherwise, Exit
    if PlayAgain == "y" or PlayAgain == "Y":
        for i in range(0, len(CurrentWord)): #Reset CurrentWord
            CurrentWord[i] = ""

        Strikes = 0 #Reset Strikes
        #Reset UnusedLetters and UsedLetters
        UnusedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        UsedLetters = []

        #Call Main
        main()
    #Exit Game
    elif PlayAgain == "n" or PlayAgain == "N":
        print("Goodbye :)")
        exit()

#Call Main Function
main()
