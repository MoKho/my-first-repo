# the first player inputs a word and the second player has to find it using the hints
import re
import msvcrt #for getch
import time # for pauseprintprint
import os #to clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
TheWord = input("\nPlease input the word : ")
print ("\n\n\n\nclearing the screen in ")
for i in range(1,4):
    print(i)
    time.sleep(.2)
os.system("cls" if os.name == "nt" else "clear")
print("Now the second player has to guess the word with ",len(TheWord)," characters.\n")
PlayerGuess = ""

while PlayerGuess != TheWord :
    PlayerGuess = ""
    for i1 in range(0,len(TheWord)):
        PlayerGuess += msvcrt.getche().decode('ASCII')
    print("\n\n")
    for i in range(0,len(TheWord)):
       print("The ", i+1, " character : ", "2" if PlayerGuess[i] == TheWord[i] else "0" if TheWord[i:].find(PlayerGuess[i]) == -1 else "1")

    
    



