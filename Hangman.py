#Netsec Beginner - 3/14/17
#Hangman Terminal Game

#Import OS to clear Terminal; Random to select random word
import os
import random

#List of Strings for Single Player
WordList = ["apple", "cat", "dog", "hair", "million", "cup", "plate", "oranges", "paper", "ten",
			"fly", "song", "car", "truck", "chase", "bug", "cucumber", "pumpkin", "horse", "grass",
			"man", "woman", "child", "hay", "sand", "dirt", "straight", "order", "eleven", "clock",
			"plug", "cord", "can", "bottle", "open", "close", "old", "odd", "tin", "top", "market",
			"handle", "tree", "leaf", "stick", "drink", "tractor", "cannon", "power", "social", "flag",
			"saint", "list", "check", "point", "person", "something", "cop", "police", "officer", "sports",
			"flea", "flee", "free", "cross", "log", "frog", "pond", "water", "pine", "line", "fine",
			"dime", "quarter", "penny", "nickel", "half", "full", "empty", "license", "house", "boat",
			"bobcat", "beaver", "cheap", "cheer", "mascot", "vine", "mine", "fine", "rover", "red",
			"orange", "yellow", "green", "blue", "indigo", "violet", "purple", "purple", "fee", "price",
			"north", "south", "east", "west", "run", "forest", "needle", "thimble", "thin", "think"]
CurrentWord = ["", ""] #Stores the current word for comparison and blank version of Current Word
Strikes = 0 #Stores Number of Wrong Answers; 6 Ends the Game
#Banks of Unused and Used Letters
UnusedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UsedLetters = []

#Main Function
def main():
	#Clear Terminal
	os.system("clear")
	
	#Print Banner
	print("      ____________________________________________________________________")
	print("     |     __   __  _______  ______  _______  __________  _______  ______ |")
	print("     |    / /  / / / ___  / / __  / / ___  / / __  __  / / ___  / / __  / |")
	print("     |   / ___/ / / /__/ / / / / / / /  /_/ / / / / / / / /__/ / / / / /  |")
	print("     |  / /  / / / /  / / / / / / / / ___  / / / / / / / /  / / / / / /   |")
	print("     | /_/  /_/ /_/  /_/ /_/ /_/ /_/__/_/ /_/ /_/ /_/ /_/  /_/ /_/ /_/    |")
	print("     |____________________________________________________________________|\n")
	
    #Player Decides If Single Player or Two Player
	Mode = SelectMode()

    #If Single, Choose Random Word from List; if Two, Get Word
	if Mode == "Single":
		RandomWord()
	elif Mode == "Multi":
		GetWord()
	elif Mode == "Unchosen":
		main()

    #Loop Until Game Over if a Gamemode is Selected
	while Mode != "Unchosen":
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
        return "Unchosen"

#Selects Random Word From List
def RandomWord():
    #Use WordList and CurrentWord Variables
    global WordList

    #Get Random Integer
    Word = random.randint(0, len(WordList) - 1)

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
    for i in range(len(Word)):
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
    for i in range(len(CurrentWord[0])):
        if CurrentWord[0][i] == str(Letter):
            List = list(CurrentWord[1]) #Turn String into List to change letter
            List[i] = str(Letter)
            CurrentWord[1] = "".join(List)
            HasChanged = True

    #Check to see if Word Changed
    if HasChanged == False:
        Strikes += 1

    #Update Used/Unused Letters
    for i in range(len(UnusedLetters)):
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
		os.system("clear") # I know I have all of this in another function, but I can't call it b/c it has input in it;
		PrintGallows()     # and, honestly, I don't feel like rewriting the code, so even though it's sloppy, it's staying like this
		print("Word: " + CurrentWord[1])
		PrintBank()
		PrintUsed()
		PlayerWins()
		PlayAgain()
    elif Strikes == 6: #Checks Number of Strikes
		os.system("clear")
		PrintGallows()
		print("Word: " + CurrentWord[1])
		PrintBank()
		PrintUsed()
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
	Play_Again = str(raw_input("Play Again(y/n)>"))

    #If User Wants New Game, Reset, Call Main; Otherwise, Exit
	if Play_Again == "y" or PlayAgain == "Y":
		for i in range(0, len(CurrentWord)): #Reset CurrentWord
			CurrentWord[i] = ""

		Strikes = 0 #Reset Strikes
		#Reset UnusedLetters and UsedLetters
		UnusedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		UsedLetters = []

		#Call Main
		main()
    #Exit Game
	elif Play_Again == "n" or PlayAgain == "N":
		print("\nGoodbye :)\n")
		exit()
	else:
		print("***Please Enter Selection***")
		PlayAgain()

#Call Main Function
main()
